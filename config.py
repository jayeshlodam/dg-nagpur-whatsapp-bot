# Configuration for DG Nagpur WhatsApp Chatbot

# Agency Details
AGENCY_NAME = "Dg Nagpur"
AGENCY_LOCATION = "Nagpur, India"
AGENCY_PHONE = "+91 XXXXXXXXXX"  # Replace with actual phone
AGENCY_EMAIL = "info@dgnagpur.com"  # Replace with actual email
AGENCY_WEBSITE = "www.dgnagpur.com"  # Replace with actual website
AGENCY_INSTAGRAM = "@dgnagpur"
AGENCY_BUSINESS_HOURS = "9:00 AM - 6:00 PM IST (Mon-Fri)"

# Services offered
SERVICES = {
    "social_media": {
        "name": "📱 Social Media Marketing",
        "description": "Strategic content creation and community management for Facebook, Instagram, LinkedIn",
        "price_range": "Starting ₹5,000/month"
    },
    "meta_ads": {
        "name": "🎯 Meta Ads (Facebook & Instagram)",
        "description": "Targeted ad campaigns for lead generation and sales conversion",
        "price_range": "Ad spend + 15% management fee"
    },
    "google_ads": {
        "name": "🔍 Google Ads (SEM)",
        "description": "Search and display ads to drive qualified traffic to your website",
        "price_range": "Ad spend + 15% management fee"
    },
    "website_dev": {
        "name": "🌐 Website Development",
        "description": "Professional, responsive websites optimized for conversions",
        "price_range": "₹15,000 - ₹1,00,000"
    },
    "seo": {
        "name": "📈 SEO (Search Engine Optimization)",
        "description": "Organic growth strategy to rank your website on Google",
        "price_range": "Starting ₹8,000/month"
    },
    "branding": {
        "name": "🎨 Branding & Design",
        "description": "Logo, brand identity, and visual design services",
        "price_range": "₹10,000 - ₹50,000"
    },
    "lead_gen": {
        "name": "💼 Lead Generation",
        "description": "Customized campaigns to generate qualified leads for your business",
        "price_range": "₹2,000 - ₹10,000/month"
    },
    "content": {
        "name": "✍️ Content Creation",
        "description": "Engaging blogs, social media posts, videos, and copywriting",
        "price_range": "Starting ₹3,000/month"
    }
}

# Pricing Plans
PRICING_PLANS = {
    "starter": {
        "name": "🚀 Starter Pack",
        "price": "₹8,000/month",
        "services": ["Social Media Marketing", "Content Creation"]
    },
    "growth": {
        "name": "📊 Growth Pack",
        "price": "₹18,000/month",
        "services": ["Social Media Marketing", "Content Creation", "Meta Ads", "Lead Generation"]
    },
    "premium": {
        "name": "👑 Premium Pack",
        "price": "₹35,000/month",
        "services": ["Social Media Marketing", "Meta Ads", "Google Ads", "Content Creation", "SEO", "Lead Generation"]
    },
    "custom": {
        "name": "🎯 Custom Solutions",
        "price": "Tailor-made",
        "services": ["We create a custom plan based on your needs"]
    }
}

# Lead Categories
LEAD_SCORES = {
    "hot": {"min": 80, "description": "Immediate follow-up needed"},
    "warm": {"min": 50, "description": "Follow-up within 24 hours"},
    "cold": {"min": 0, "description": "Follow-up within a week"}
}

# Conversation States
STATE_START = "start"
STATE_MENU = "menu"
STATE_SERVICES = "services"
STATE_PRICING = "pricing"
STATE_CONSULTATION = "consultation"
STATE_LEAD_QUALIFY = "lead_qualify"
STATE_CONTACT_INFO = "contact_info"
STATE_BOOKING = "booking"
STATE_THANKS = "thanks"

# API Configuration
WHATSAPP_API_VERSION = "v17.0"  # Update based on actual version
PHONE_NUMBER_ID = ""  # Replace with actual Phone Number ID
BUSINESS_ACCOUNT_ID = ""  # Replace with actual Business Account ID
WHATSAPP_TOKEN = ""  # Replace with actual access token

# Database Settings
DB_PATH = "dg_nagpur_leads.db"

# Message timing (in seconds)
MESSAGE_DELAY = 1
TYPING_INDICATOR_DURATION = 2
