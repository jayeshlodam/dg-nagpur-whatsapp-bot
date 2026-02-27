"""
Conversation Flows Module for DG Nagpur WhatsApp Chatbot
Handles different conversation states and transitions
"""

from datetime import datetime
import json
from config import (
    STATE_START, STATE_MENU, STATE_SERVICES, STATE_PRICING,
    STATE_CONSULTATION, STATE_LEAD_QUALIFY, STATE_CONTACT_INFO,
    STATE_BOOKING, STATE_THANKS
)
from messages import *
from database import db


class ConversationFlow:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.lead = db.get_lead(phone_number)
        self.user_message = None
        self.current_state = STATE_START
        
        if self.lead:
            self.current_state = STATE_MENU
    
    def process_message(self, user_input):
        """Main message processing function"""
        self.user_message = user_input.strip().lower()
        response = None
        next_state = self.current_state
        
        # Navigation keywords
        if self.user_message in ["menu", "main menu", "back"]:
            return MAIN_MENU, STATE_MENU
        
        if self.user_message in ["exit", "bye", "goodbye", "thanks"]:
            return CLOSING_MESSAGE, STATE_THANKS
        
        # State-based routing
        if self.current_state == STATE_START:
            response, next_state = self.handle_start()
        
        elif self.current_state == STATE_MENU:
            response, next_state = self.handle_menu()
        
        elif self.current_state == STATE_SERVICES:
            response, next_state = self.handle_services()
        
        elif self.current_state == STATE_PRICING:
            response, next_state = self.handle_pricing()
        
        elif self.current_state == STATE_CONSULTATION:
            response, next_state = self.handle_consultation()
        
        elif self.current_state == STATE_LEAD_QUALIFY:
            response, next_state = self.handle_lead_qualify()
        
        elif self.current_state == STATE_CONTACT_INFO:
            response, next_state = self.handle_contact_info()
        
        elif self.current_state == STATE_BOOKING:
            response, next_state = self.handle_booking()
        
        else:
            response = FALLBACK_MESSAGE
            next_state = self.current_state
        
        # Log conversation
        db.add_conversation(self.phone_number, user_input, response, next_state)
        
        # Update current state for next message
        self.current_state = next_state
        
        return response, next_state
    
    # START STATE
    def handle_start(self):
        """Initial greeting"""
        # Create lead if doesn't exist
        if not self.lead:
            db.add_lead(self.phone_number)
        
        db.track_metric("new_conversation")
        return GREETING_MESSAGE + "\n\n" + MAIN_MENU, STATE_MENU
    
    # MENU STATE
    def handle_menu(self):
        """Main menu handling"""
        if self.user_message in ["1", "services", "our services"]:
            return SERVICE_INTRO, STATE_SERVICES
        
        elif self.user_message in ["2", "pricing", "pricing plans"]:
            return self.get_pricing_response(), STATE_PRICING
        
        elif self.user_message in ["3", "consultation", "book", "book consultation", "booking"]:
            return LEAD_QUALIFY_START, STATE_LEAD_QUALIFY
        
        elif self.user_message in ["4", "portfolio", "work", "case studies", "see our work"]:
            db.track_metric("portfolio_viewed")
            return PORTFOLIO_MESSAGE + "\n\n" + MAIN_MENU, STATE_MENU
        
        elif self.user_message in ["5", "expert", "talk to expert", "specialist"]:
            db.track_metric("expert_request")
            return EXPERT_MESSAGE + "\n\n" + MAIN_MENU, STATE_MENU
        
        else:
            return FALLBACK_MESSAGE, STATE_MENU
    
    # SERVICES STATE
    def handle_services(self):
        """Service selection and details"""
        service_map = {
            "1": ("social_media", "Social Media Marketing"),
            "social media": ("social_media", "Social Media Marketing"),
            "2": ("meta_ads", "Meta Ads"),
            "facebook ads": ("meta_ads", "Meta Ads"),
            "meta ads": ("meta_ads", "Meta Ads"),
            "3": ("google_ads", "Google Ads"),
            "google": ("google_ads", "Google Ads"),
            "4": ("website_dev", "Website Development"),
            "website": ("website_dev", "Website Development"),
            "5": ("seo", "SEO"),
            "6": ("branding", "Branding"),
            "branding": ("branding", "Branding"),
            "7": ("lead_gen", "Lead Generation"),
            "leads": ("lead_gen", "Lead Generation"),
            "8": ("content", "Content Creation"),
            "content": ("content", "Content Creation"),
        }
        
        if self.user_message in service_map:
            service_key, service_name = service_map[self.user_message]
            
            # Store service interest
            interested = json.loads(db.get_lead(self.phone_number).get('services_interested', '[]') or '[]')
            if service_name not in interested:
                interested.append(service_name)
            db.update_lead(self.phone_number, services_interested=json.dumps(interested))
            
            # Update lead score
            db.calculate_lead_score(self.phone_number)
            
            # Log metric
            db.track_metric(f"service_viewed_{service_key}")
            
            response = SERVICE_DETAILS.get(service_key, FALLBACK_MESSAGE)
            response += "\n\n" + "Would you like to discuss this service further? Reply 'Yes' or ask about another service (1-8)"
            
            return response, STATE_SERVICES
        
        elif self.user_message in ["yes", "interested", "i'm interested", "tell me more"]:
            return "Great! Let's get you connected with our specialist.\n\n" + LEAD_QUALIFY_START, STATE_LEAD_QUALIFY
        
        else:
            return SERVICE_INTRO, STATE_SERVICES
    
    # PRICING STATE
    def handle_pricing(self):
        """Pricing information"""
        return self.get_pricing_response(), STATE_PRICING
    
    def get_pricing_response(self):
        """Get full pricing response"""
        response = PRICING_HEADER + "\n\n"
        response += PRICING_STARTER + "\n\n"
        response += PRICING_GROWTH + "\n\n"
        response += PRICING_PREMIUM + "\n\n"
        response += PRICING_CUSTOM + "\n\n"
        response += "Want a custom quote for your business? Let's schedule a free consultation!\n"
        response += "Reply 'Consultation' to book your call."
        
        db.track_metric("pricing_viewed")
        return response
    
    # LEAD QUALIFICATION STATE
    def handle_lead_qualify(self):
        """Lead qualification questions"""
        lead = db.get_lead(self.phone_number)
        
        # Ask business type first
        if not lead.get('business_type'):
            if self.user_message in ["1", "real estate", "2", "ecommerce", "3", "coaching", 
                                   "training", "education", "4", "service", "salon", "gym",
                                   "5", "b2b", "6", "other"]:
                business_types = {
                    "1": "Real Estate",
                    "real estate": "Real Estate",
                    "2": "Ecommerce",
                    "ecommerce": "Ecommerce",
                    "3": "Coaching/Training/Education",
                    "coaching": "Coaching/Training/Education",
                    "training": "Coaching/Training/Education",
                    "education": "Coaching/Training/Education",
                    "4": "Service-based (Salon, Gym, etc.)",
                    "service": "Service-based (Salon, Gym, etc.)",
                    "salon": "Service-based (Salon, Gym, etc.)",
                    "gym": "Service-based (Salon, Gym, etc.)",
                    "5": "B2B Services",
                    "b2b": "B2B Services",
                    "6": "Other",
                    "other": "Other"
                }
                business = business_types.get(self.user_message, "Other")
                db.update_lead(self.phone_number, business_type=business)
                return LEAD_BUDGET, STATE_LEAD_QUALIFY
            else:
                return LEAD_QUALIFY_START, STATE_LEAD_QUALIFY
        
        # Ask budget
        elif not lead.get('budget_range'):
            if self.user_message in ["1", "2", "3", "4", "5", "6"]:
                budgets = {
                    "1": "Below ₹5,000",
                    "2": "₹5,000 - ₹15,000",
                    "3": "₹15,000 - ₹30,000",
                    "4": "₹30,000 - ₹50,000",
                    "5": "Above ₹50,000",
                    "6": "Not sure yet"
                }
                budget = budgets.get(self.user_message, "Not sure yet")
                db.update_lead(self.phone_number, budget_range=budget)
                return LEAD_GOAL, STATE_LEAD_QUALIFY
            else:
                return LEAD_BUDGET, STATE_LEAD_QUALIFY
        
        # Ask goal
        elif not lead.get('goal'):
            if self.user_message in ["1", "2", "3", "4", "5"]:
                goals = {
                    "1": "Generate more leads",
                    "2": "Increase sales/revenue",
                    "3": "Build brand awareness",
                    "4": "Improve website visibility",
                    "5": "All of the above"
                }
                goal = goals.get(self.user_message, "Not specified")
                db.update_lead(self.phone_number, goal=goal)
                
                # Calculate lead score
                db.calculate_lead_score(self.phone_number)
                db.track_metric("lead_qualified")
                
                # Get contact info
                return CONTACT_NAME, STATE_CONTACT_INFO
            else:
                return LEAD_GOAL, STATE_LEAD_QUALIFY
        
        return FALLBACK_MESSAGE, STATE_LEAD_QUALIFY
    
    # CONTACT INFO STATE
    def handle_contact_info(self):
        """Contact information collection"""
        lead = db.get_lead(self.phone_number)
        
        # Get name
        if not lead.get('name'):
            if len(self.user_message) < 3:
                return "Please provide your full name:", STATE_CONTACT_INFO
            
            db.update_lead(self.phone_number, name=self.user_message.title())
            return CONTACT_EMAIL, STATE_CONTACT_INFO
        
        # Get email
        elif not lead.get('email'):
            if '@' not in self.user_message:
                return "Please provide a valid email address:", STATE_CONTACT_INFO
            
            db.update_lead(self.phone_number, email=self.user_message)
            
            # Confirmation and next steps
            updated_lead = db.get_lead(self.phone_number)
            lead_category = updated_lead.get('lead_category', 'warm')
            
            response = f"""
✅ *Perfect, {updated_lead['name']}!*

We've saved all your details:
👤 Name: {updated_lead['name']}
📱 Phone: {self.phone_number}
✉️ Email: {updated_lead['email']}
📊 Business: {updated_lead.get('business_type', 'Not provided')}
💰 Budget: {updated_lead.get('budget_range', 'Not provided')}
🎯 Goal: {updated_lead.get('goal', 'Not provided')}

📌 *Next Steps:*
1️⃣ Our team will review your requirements
2️⃣ You'll get a personalized recommendation
3️⃣ We'll reach out within 2 hours

🎉 *Would you like to book a free consultation call?*
Reply "Yes" to schedule, or "Menu" for other options.
            """.strip()
            
            db.track_metric(f"lead_captured_{lead_category}")
            
            return response, STATE_BOOKING
        
        return FALLBACK_MESSAGE, STATE_CONTACT_INFO
    
    # BOOKING STATE
    def handle_booking(self):
        """Consultation booking"""
        lead = db.get_lead(self.phone_number)
        
        if self.user_message in ["yes", "book", "consultation", "schedule", "time"]:
            return CONSULTATION_INTRO, STATE_CONSULTATION
        
        elif self.user_message in ["no", "skip", "later"]:
            response = f"""
No problem! 😊

We'll still follow up with personalized recommendations for your business.

📌 You can also:
✅ Check our portfolio - Reply "4" or "Work"
✅ See pricing - Reply "2" or "Pricing"
✅ Chat anytime - We're always here!

Anything else I can help with?
            """.strip()
            db.track_metric("consultation_declined")
            return response, STATE_MENU
        
        else:
            return FALLBACK_MESSAGE, STATE_BOOKING
    
    # CONSULTATION STATE
    def handle_consultation(self):
        """Schedule consultation"""
        lead = db.get_lead(self.phone_number)
        
        if not lead.get('consultation_date'):
            # Validate date format (DD/MM/YYYY or similar)
            if self.validate_date(self.user_message):
                db.update_lead(self.phone_number, consultation_date=self.user_message)
                
                response = """
📍 Got it! Now, what time would you prefer?

⏰ Please share your preferred time:
(Format: HH:MM AM/PM)

Example: 02:00 PM or 14:00
                """.strip()
                return response, STATE_CONSULTATION
            else:
                return "Please provide date in DD/MM/YYYY format. Example: 01/03/2026", STATE_CONSULTATION
        
        elif not lead.get('consultation_time'):
            if self.validate_time(self.user_message):
                db.update_lead(self.phone_number, consultation_time=self.user_message)
                
                # Create booking
                slot_datetime = f"{lead['consultation_date']} {self.user_message}"
                
                response = CONSULTATION_CONFIRMATION.format(
                    name=lead['name'],
                    phone=self.phone_number,
                    email=lead['email'],
                    datetime=slot_datetime
                )
                
                db.track_metric("consultation_booked")
                return response, STATE_THANKS
            else:
                return "Please provide time in HH:MM AM/PM format. Example: 02:00 PM", STATE_CONSULTATION
        
        return FALLBACK_MESSAGE, STATE_CONSULTATION
    
    # UTILITY METHODS
    
    def validate_date(self, date_string):
        """Validate date format"""
        try:
            datetime.strptime(date_string, "%d/%m/%Y")
            return True
        except:
            return False
    
    def validate_time(self, time_string):
        """Validate time format"""
        try:
            # Try 24-hour format
            datetime.strptime(time_string, "%H:%M")
            return True
        except:
            try:
                # Try 12-hour format
                datetime.strptime(time_string, "%I:%M %p")
                return True
            except:
                return False
