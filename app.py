"""
DG Nagpur - WhatsApp Cloud API Bot
Single File Production Version
"""

from flask import Flask, request, jsonify
import os
import requests
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# ===============================
# ENV VARIABLES (SET IN RAILWAY)
# ===============================
VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
API_VERSION = os.getenv("WHATSAPP_API_VERSION", "v18.0")

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===============================
# WEBHOOK VERIFICATION (GET)
# ===============================
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        logger.info("✅ Webhook verified successfully")
        return challenge, 200

    logger.warning("❌ Webhook verification failed")
    return "Verification failed", 403


# ===============================
# RECEIVE MESSAGES (POST)
# ===============================
@app.route("/webhook", methods=["POST"])
def receive_message():
    data = request.get_json()
    logger.info(f"📩 Incoming Data: {data}")

    try:
        if data.get("object") == "whatsapp_business_account":
            entry = data["entry"][0]
            changes = entry["changes"][0]
            value = changes["value"]

            if "messages" in value:
                message = value["messages"][0]
                sender = message["from"]
                message_type = message["type"]

                if message_type == "text":
                    user_message = message["text"]["body"]
                else:
                    user_message = f"Received {message_type}"

                logger.info(f"📨 Message from {sender}: {user_message}")

                # Auto reply
                reply_text = generate_reply(user_message)

                send_whatsapp_message(sender, reply_text)

        return jsonify({"status": "ok"}), 200

    except Exception as e:
        logger.error(f"❌ Error processing message: {str(e)}")
        return jsonify({"error": str(e)}), 500


# ===============================
# GENERATE BOT RESPONSE
# ===============================
def generate_reply(user_message):
    user_message = user_message.lower()

    if "hi" in user_message or "hello" in user_message:
        return "Hello 👋 Welcome to *DG Nagpur* 🚀\n\nWe help businesses grow with:\n• Social Media Marketing\n• Meta & Google Ads\n• Website Development\n• SEO\n\nHow can we help you today?"

    elif "price" in user_message or "cost" in user_message:
        return "Our pricing depends on your business needs.\n\nPlease tell us:\n1️⃣ Your business type\n2️⃣ Your monthly budget\n3️⃣ Your goal (Leads / Sales / Branding)"

    elif "contact" in user_message:
        return "📞 Call: +91-XXXXXXXXXX\n📧 Email: info@dgnagpur.com\n🌐 Website: www.dgnagpur.com"

    else:
        return "Thank you for contacting *DG Nagpur* 🙌\n\nOur team will connect with you shortly."


# ===============================
# SEND MESSAGE FUNCTION
# ===============================
def send_whatsapp_message(recipient, message):
    if not ACCESS_TOKEN or not PHONE_NUMBER_ID:
        logger.error("❌ Missing ACCESS_TOKEN or PHONE_NUMBER_ID")
        return

    url = f"https://graph.facebook.com/{API_VERSION}/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": recipient,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    logger.info(f"📤 Send Status: {response.status_code}")
    logger.info(f"📤 Response: {response.text}")


# ===============================
# HEALTH CHECK
# ===============================
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "DG Nagpur Bot Running 🚀"}), 200


# ===============================
# RUN APP
# ===============================
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)