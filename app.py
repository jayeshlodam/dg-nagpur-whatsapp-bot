"""
Main Flask Application for DG Nagpur WhatsApp Chatbot
Handles WhatsApp Business API integration
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from dotenv import load_dotenv
from config import (
    WHATSAPP_API_VERSION,
    AGENCY_PHONE, AGENCY_EMAIL, AGENCY_WEBSITE, AGENCY_LOCATION
)
from flows import ConversationFlow
import logging
from datetime import datetime
import requests

# Load environment variables
load_dotenv()

# Import database after environment is loaded
try:
    from database import db
    from messages import OUT_OF_HOURS, THANK_YOU_MESSAGE, ERROR_MESSAGE
    logger_temp = logging.getLogger(__name__)
    logger_temp.info("✅ Database and messages imported successfully")
except Exception as e:
    logger_temp = logging.getLogger(__name__)
    logger_temp.error(f"❌ Failed to import database or messages: {e}")
    # Continue anyway - db will be initialized lazily
    db = None

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Get tokens from environment
VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "your_verify_token")
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN", "")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
BUSINESS_ACCOUNT_ID = os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID", "")

# Log initialization
logger = logging.getLogger(__name__)
logger.info("="*60)
logger.info("🔐 WhatsApp Configuration Check:")
logger.info(f"✅ Verify Token: {'SET' if VERIFY_TOKEN else 'MISSING'}")
logger.info(f"✅ Access Token: {'SET' if ACCESS_TOKEN else 'MISSING'}")
logger.info(f"✅ Phone Number ID: {PHONE_NUMBER_ID if PHONE_NUMBER_ID else 'MISSING'}")
logger.info(f"✅ Business Account ID: {BUSINESS_ACCOUNT_ID if BUSINESS_ACCOUNT_ID else 'MISSING'}")
logger.info("="*60)


# ===== WEBHOOK ENDPOINTS =====

@app.route('/webhook', methods=['GET'])
def webhook_get():
    """
    Webhook verification endpoint for WhatsApp Business API
    """
    verify_token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if verify_token == VERIFY_TOKEN:
        logger.info("Webhook verified successfully")
        return challenge
    
    logger.warning("Webhook verification failed")
    return "Invalid token", 403


@app.route('/webhook', methods=['POST'])
def webhook_post():
    """
    Main webhook endpoint for receiving messages from WhatsApp
    """
    try:
        data = request.get_json()
        logger.info(f"Received webhook data: {json.dumps(data)}")
        
        # Extract message data
        if data.get("object") == "whatsapp_business_account":
            entries = data.get("entry", [])
            
            for entry in entries:
                changes = entry.get("changes", [])
                for change in changes:
                    value = change.get("value", {})
                    messages = value.get("messages", [])
                    
                    for message in messages:
                        handle_incoming_message(message, value)
        
        return jsonify({"status": "ok"}), 200
    
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500


def handle_incoming_message(message, value):
    """
    Process incoming message and generate response
    """
    sender_phone = None
    try:
        # Extract sender phone and message text
        sender_phone = message.get("from")
        message_text = None
        message_type = message.get("type")
        
        logger.info(f"🔍 Processing message type: {message_type} from {sender_phone}")
        
        # Handle different message types
        if message_type == "text":
            message_text = message.get("text", {}).get("body", "")
        
        elif message_type == "button":
            # Handle button responses
            button_payload = message.get("button", {}).get("payload", "")
            message_text = button_payload
        
        elif message_type in ["image", "video", "document", "audio"]:
            # Handle media
            message_text = f"[Media: {message_type}]"
        
        else:
            logger.warning(f"⚠️ Unsupported message type: {message_type}")
            return
        
        if not message_text:
            logger.warning("⚠️ No message text extracted")
            return
        
        logger.info(f"📨 Message from {sender_phone}: {message_text}")
        
        # Track incoming message
        try:
            db.track_metric("message_received")
        except Exception as e:
            logger.warning(f"⚠️ Could not track metric: {e}")
        
        # Process message through conversation flow
        try:
            flow = ConversationFlow(sender_phone)
            bot_response, next_state = flow.process_message(message_text)
        except Exception as e:
            logger.error(f"❌ Error in conversation flow: {str(e)}", exc_info=True)
            bot_response = "Sorry, something went wrong. Please try again."
            next_state = "error"
        
        # Send response
        logger.info(f"📤 About to send response to {sender_phone}")
        send_result = send_whatsapp_message(sender_phone, bot_response)
        
        if send_result:
            logger.info(f"✅ Response sent successfully to {sender_phone}: State={next_state}")
        else:
            logger.error(f"❌ Failed to send response to {sender_phone}")
        
    except Exception as e:
        logger.error(f"❌ Error handling message: {str(e)}", exc_info=True)
        # Send error message
        if sender_phone:
            try:
                error_msg = ERROR_MESSAGE.format(
                    phone=AGENCY_PHONE,
                    email=AGENCY_EMAIL
                )
                send_whatsapp_message(sender_phone, error_msg)
            except Exception as err:
                logger.error(f"❌ Could not send error message: {err}")


def send_whatsapp_message(recipient_phone, message_text):
    """
    Send message via WhatsApp Business API
    """
    try:
        # Validate credentials
        if not ACCESS_TOKEN:
            logger.error("❌ ACCESS_TOKEN not set in environment variables!")
            return False
        
        if not PHONE_NUMBER_ID:
            logger.error("❌ PHONE_NUMBER_ID not set in environment variables!")
            return False
        
        url = f"https://graph.instagram.com/{WHATSAPP_API_VERSION}/{PHONE_NUMBER_ID}/messages"
        
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient_phone,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message_text
            }
        }
        
        logger.info(f"📤 Sending message to {recipient_phone}")
        logger.info(f"📍 API Endpoint: {url}")
        
        response = requests.post(url, json=payload, headers=headers)
        
        logger.info(f"📊 Response status: {response.status_code}")
        
        if response.status_code in [200, 201]:
            logger.info(f"✅ Message sent successfully to {recipient_phone}")
            db.track_metric("message_sent")
            return True
        else:
            logger.error(f"❌ Failed to send message: HTTP {response.status_code}")
            logger.error(f"❌ Response: {response.text}")
            return False
    
    except Exception as e:
        logger.error(f"❌ Error sending WhatsApp message: {str(e)}", exc_info=True)
        return False


def send_whatsapp_template(recipient_phone, template_name, language="en", **params):
    """
    Send template message via WhatsApp Business API
    (Requires pre-approved templates)
    """
    try:
        url = f"https://graph.instagram.com/{WHATSAPP_API_VERSION}/{PHONE_NUMBER_ID}/messages"
        
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        
        body = [{"type": "text", "text": param} for param in params.values()]
        
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient_phone,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language
                },
                "body": {
                    "parameters": body
                }
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            logger.info(f"Template message sent to {recipient_phone}")
            return True
        else:
            logger.error(f"Failed to send template: {response.text}")
            return False
    
    except Exception as e:
        logger.error(f"Error sending template: {str(e)}", exc_info=True)
        return False


# ===== API ENDPOINTS FOR ADMIN =====

@app.route('/api/leads', methods=['GET'])
def api_get_leads():
    """Get all leads"""
    try:
        filter_by = request.args.get('filter', None)
        leads = db.get_all_leads(filter_by=filter_by)
        return jsonify({"status": "success", "leads": leads}), 200
    except Exception as e:
        logger.error(f"Error fetching leads: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/leads/<phone>', methods=['GET'])
def api_get_lead(phone):
    """Get specific lead details"""
    try:
        lead = db.get_lead(phone)
        if not lead:
            return jsonify({"error": "Lead not found"}), 404
        
        # Get additional data
        conversations = db.get_conversation_history(phone)
        bookings = db.get_conversation_count(phone)
        
        lead_data = dict(lead)
        lead_data['conversation_count'] = bookings
        lead_data['recent_messages'] = conversations
        
        return jsonify({"status": "success", "lead": lead_data}), 200
    except Exception as e:
        logger.error(f"Error fetching lead: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/leads/<phone>', methods=['PUT'])
def api_update_lead(phone):
    """Update lead information"""
    try:
        data = request.get_json()
        db.update_lead(phone, **data)
        
        # Recalculate lead score if info changed
        db.calculate_lead_score(phone)
        
        updated_lead = db.get_lead(phone)
        return jsonify({"status": "success", "lead": dict(updated_lead)}), 200
    except Exception as e:
        logger.error(f"Error updating lead: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/analytics', methods=['GET'])
def api_get_analytics():
    """Get analytics data"""
    try:
        metric_type = request.args.get('metric', 'message_received')
        days = request.args.get('days', 30, type=int)
        
        analytics = db.get_analytics(metric_type, days)
        total_leads = len(db.get_all_leads())
        hot_leads = len(db.get_all_leads(filter_by='hot'))
        warm_leads = len(db.get_all_leads(filter_by='warm'))
        cold_leads = len(db.get_all_leads(filter_by='cold'))
        
        return jsonify({
            "status": "success",
            "analytics": analytics,
            "summary": {
                "total_leads": total_leads,
                "hot_leads": hot_leads,
                "warm_leads": warm_leads,
                "cold_leads": cold_leads
            }
        }), 200
    except Exception as e:
        logger.error(f"Error fetching analytics: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/send-message', methods=['POST'])
def api_send_message():
    """Send manual message to a lead"""
    try:
        data = request.get_json()
        phone = data.get('phone')
        message = data.get('message')
        
        if not phone or not message:
            return jsonify({"error": "Phone and message required"}), 400
        
        if send_whatsapp_message(phone, message):
            return jsonify({"status": "success", "message": "Message sent"}), 200
        else:
            return jsonify({"error": "Failed to send message"}), 500
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/bookings/<date>', methods=['GET'])
def api_get_bookings(date):
    """Get bookings for a specific date"""
    try:
        bookings = db.get_bookings_by_date(date)
        return jsonify({"status": "success", "bookings": bookings}), 200
    except Exception as e:
        logger.error(f"Error fetching bookings: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    # Try to ensure database is initialized
    try:
        if db is None:
            from database import db as db_fresh
            db_list = db_fresh
        else:
            db_list = db
    except:
        db_list = None
    
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "DG Nagpur WhatsApp Chatbot",
        "database": "connected" if db_list else "initializing"
    }), 200


@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # For production, use a production WSGI server like Gunicorn
    # Example: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    
    try:
        debug_mode = os.getenv("DEBUG", "False") == "True"
        port = int(os.getenv("PORT", 5000))
        
        logger.info("="*60)
        logger.info("🚀 Starting DG Nagpur WhatsApp Chatbot")
        logger.info(f"📍 Port: {port}")
        logger.info(f"🔧 Debug Mode: {debug_mode}")
        logger.info(f"📧 Agency: info@dgnagpur.com")
        logger.info("="*60)
        
        app.run(
            host='0.0.0.0',
            port=port,
            debug=debug_mode,
            use_reloader=False
        )
    except Exception as e:
        logger.error(f"❌ Failed to start application: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise
