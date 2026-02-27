# Message Templates for DG Nagpur WhatsApp Chatbot

from config import AGENCY_NAME, AGENCY_LOCATION, AGENCY_PHONE, AGENCY_EMAIL, AGENCY_WEBSITE, AGENCY_BUSINESS_HOURS

# Greeting and Welcome Messages
GREETING_MESSAGE = f"""
👋 Welcome to {AGENCY_NAME}!

I'm your digital marketing assistant. I'm here to help you grow your business with proven strategies in:

✨ What we do:
📱 Social Media Marketing
🎯 Meta Ads & Google Ads
🌐 Website Development
📈 SEO
🎨 Branding
💼 Lead Generation
✍️ Content Creation

How can I help you today?
""".strip()

MAIN_MENU = """
📋 *MAIN MENU*

1️⃣ *Our Services* - Explore what we offer
2️⃣ *Pricing Plans* - See our packages
3️⃣ *Book Free Consultation* - Schedule a call
4️⃣ *See Our Work* - View case studies
5️⃣ *Talk to Expert* - Chat with specialist

👉 Just reply with the number (1-5) or the option name.
""".strip()

# Service-related messages
SERVICE_INTRO = """
🎯 *OUR SERVICES*

Let me show you what we offer. Reply with the number to learn more:

1️⃣ Social Media Marketing
2️⃣ Meta Ads (Facebook & Instagram)
3️⃣ Google Ads
4️⃣ Website Development
5️⃣ SEO
6️⃣ Branding & Design
7️⃣ Lead Generation
8️⃣ Content Creation

📌 Or reply "Back" to return to main menu.
""".strip()

SERVICE_DETAILS = {
    "social_media": """
📱 *SOCIAL MEDIA MARKETING*

We create a complete social media strategy for your brand on:
✅ Facebook
✅ Instagram
✅ LinkedIn
✅ YouTube

What we do:
💡 Content planning & creation
👥 Community management
📊 Monthly performance reports
💬 Engagement & follower growth

📊 *Results:* Average 300% growth in engagement within 3 months

💰 *Pricing:* Starting ₹5,000/month

Ready to grow your social presence? Let's chat! 👇
    """.strip(),
    
    "meta_ads": """
🎯 *META ADS (FACEBOOK & INSTAGRAM)*

Get your ads in front of the right people at the right time!

What we do:
🎯 Audience targeting & segmentation
💡 Creative ad design
🔄 A/B testing & optimization
📈 Conversion tracking & reporting
💰 Budget optimization

📊 *Results:* Average 4-6x ROI within 30 days

💵 *Pricing:* Ad spend + 15% management fee (minimum ₹5,000/month)

Which industry are you in?
1. Ecommerce
2. Real Estate
3. Coaching/Education
4. Local Services
5. Other

📌 Reply with number or type your industry.
    """.strip(),
    
    "google_ads": """
🔍 *GOOGLE ADS (SEM)*

Be found by customers actively searching for your products/services!

What we do:
🔍 Keyword research & strategy
⚡ High-converting ad copy
📱 Mobile-optimized campaigns
🔄 Continuous optimization
📊 Detailed ROI tracking

📊 *Results:* Average 5-8% conversion rate

💵 *Pricing:* Ad spend + 15% management fee (minimum ₹5,000/month)

Which type of business are you in?
1. Ecommerce
2. Service-based
3. B2B
4. Local Business
5. Other

📌 Reply with number.
    """.strip(),
    
    "website_dev": """
🌐 *WEBSITE DEVELOPMENT*

Professional, fast-loading websites that convert visitors into customers!

What we do:
🎨 Modern, responsive design
💻 Mobile-friendly & fast
🔍 SEO optimized
🔗 Easy integration with marketing tools
⚙️ Ongoing support & updates

💰 *Pricing:* ₹15,000 - ₹1,00,000+ (depending on complexity)

Website types we create:
1. Portfolio/Service Business
2. Ecommerce Store
3. Lead Generation Website
4. Corporate Website
5. Blog/Content Site

📌 Which type do you need?
    """.strip(),
    
    "seo": """
📈 *SEO (SEARCH ENGINE OPTIMIZATION)*

Rank on Google and attract organic traffic 24/7!

What we do:
🔍 Keywords & competitor research
📝 On-page & technical SEO
🔗 Link building strategy
📊 Monthly ranking reports
💡 Content strategy & optimization

📊 *Timeline:* First results in 2-3 months
📈 *Results:* 150-300% organic traffic increase

💰 *Pricing:* Starting ₹8,000/month (4-month minimum)

What's your main goal?
1. More website traffic
2. More leads/inquiries
3. Better rankings
4. Increase online visibility

📌 Reply with number.
    """.strip(),
    
    "branding": """
🎨 *BRANDING & DESIGN*

Build a memorable brand that stands out from competitors!

What we do:
🎨 Logo design
🌈 Brand identity guidelines
📱 Social media graphics
✍️ Brand messaging & positioning
📊 Brand audit & strategy

💰 *Pricing:* ₹10,000 - ₹50,000 (depending on scope)

What do you need?
1. Logo design only
2. Complete brand identity
3. Rebrand existing business
4. Graphics for social media
5. Other

📌 Reply with number.
    """.strip(),
    
    "lead_gen": """
💼 *LEAD GENERATION*

Get qualified leads delivered to your business consistently!

What we do:
🎯 Target ideal customer profiles
📱 Multi-channel campaigns (Facebook, Google, LinkedIn)
📝 High-converting landing pages
📊 Lead verification & qualification
📞 CRM integration

📊 *Results:* 20-50 qualified leads/month (varies by industry)

💰 *Pricing:* ₹2,000 - ₹10,000/month + ad spend

What industry are you in?
1. Real Estate
2. Coaching/Training
3. B2B Services
4. Local Services
5. Other

📌 Reply with number.
    """.strip(),
    
    "content": """
✍️ *CONTENT CREATION*

Engage your audience with compelling, professional content!

What we do:
✍️ Blog articles (SEO optimized)
📸 Social media captions & posts
🎬 Video scripts & YouTube content
📰 Email newsletters
💬 Website copy
📊 Content calendar planning

📊 *Results:* Increased engagement, shares, and conversions

💰 *Pricing:* Starting ₹3,000/month

What type of content do you need most?
1. Blog articles
2. Social media posts
3. Video scripts
4. Sales page copy
5. All of the above

📌 Reply with number.
    """.strip(),
}

# Pricing messages
PRICING_HEADER = """
💰 *OUR PRICING PLANS*

We offer flexible packages for every budget:
""".strip()

PRICING_STARTER = """
🚀 *STARTER PACK - ₹8,000/month*
Perfect for small businesses just starting out

Includes:
✅ Social Media Management (2 platforms)
✅ 4 posts per week
✅ Monthly report

📌 Ideal for: Local businesses, startups
""".strip()

PRICING_GROWTH = """
📊 *GROWTH PACK - ₹18,000/month*
For businesses ready to scale

Includes:
✅ Social Media Management (3 platforms)
✅ 8 posts per week
✅ Lead Generation campaigns
✅ Meta Ads (₹2,000/month ad spend)
✅ Bi-weekly performance calls

📌 Ideal for: Growing businesses, ecommerce
""".strip()

PRICING_PREMIUM = """
👑 *PREMIUM PACK - ₹35,000/month*
Complete digital marketing solution

Includes:
✅ Social Media Management (4 platforms)
✅ Daily content
✅ Meta Ads + Google Ads
✅ SEO optimization
✅ Blog writing
✅ Weekly strategy calls
✅ Lead nurturing campaigns

📌 Ideal for: Scaling businesses, serious growth
""".strip()

PRICING_CUSTOM = """
🎯 *CUSTOM SOLUTIONS*
Everything else (Website Dev, Branding, etc.)

We create tailor-made packages based on your:
✅ Business goals
✅ Budget
✅ Timeline
✅ Current challenges

💡 Perfect for businesses with unique needs!

Would you like a custom quote? Let's schedule a call! ☎️
""".strip()

# Lead Qualification Messages
LEAD_QUALIFY_START = """
Great! To find the perfect solution for your business, I'd like to ask a few quick questions.

📌 This takes just 2 minutes!

First question:
*What is your business type?*

1️⃣ Real Estate
2️⃣ Ecommerce
3️⃣ Coaching/Training/Education
4️⃣ Service-based (Salon, Gym, etc.)
5️⃣ B2B Services
6️⃣ Other
""".strip()

LEAD_BUDGET = """
*What is your monthly marketing budget?*

1️⃣ Below ₹5,000
2️⃣ ₹5,000 - ₹15,000
3️⃣ ₹15,000 - ₹30,000
4️⃣ ₹30,000 - ₹50,000
5️⃣ Above ₹50,000
6️⃣ Not sure yet
""".strip()

LEAD_GOAL = """
*What is your main goal?*

1️⃣ Generate more leads
2️⃣ Increase sales/revenue
3️⃣ Build brand awareness
4️⃣ Improve website visibility
5️⃣ All of the above
""".strip()

# Consultation Booking
CONSULTATION_INTRO = """
📞 *BOOK YOUR FREE CONSULTATION*

During this 30-minute call, we'll:
✅ Assess your current marketing
✅ Identify growth opportunities
✅ Suggest a personalized strategy
✅ Answer all your questions
✅ No obligation or sales pressure

When would you like to meet?

📅 Please share your preferred date and time
(Format: DD/MM/YYYY and HH:MM AM/PM)

Example: 01/03/2026 at 2:00 PM
""".strip()

CONSULTATION_READY = """
✅ *Perfect!*

Before we finalize your slot, just need your contact details:

📝 What's your name?
""".strip()

CONSULTATION_CONTACT = """
📞 What's your phone number?

(We'll use this to send you the meeting link and reminder)
""".strip()

CONSULTATION_EMAIL = """
✉️ What's your email address?

(We'll send you calendar invite and meeting details)
""".strip()

CONSULTATION_CONFIRMATION = """
✅ *BOOKING CONFIRMED!*

📋 *Your Details:*
👤 Name: {name}
📱 Phone: {phone}
✉️ Email: {email}
📅 Date & Time: {datetime}

📌 What happens next:
1️⃣ You'll receive a calendar invite
2️⃣ A reminder 24 hours before
3️⃣ Meeting link will be shared on WhatsApp

🎉 We're excited to help you grow your business!

Any questions? Just reply here 👇
""".strip()

# Contact Information Collection
CONTACT_NAME = """
Great! Let's connect.

👤 *What's your name?*
""".strip()

CONTACT_PHONE = """
📱 *Your phone number?*
(So we can follow up with you)
""".strip()

CONTACT_EMAIL = """
✉️ *Your email address?*
(For detailed proposals and updates)
""".strip()

CONTACT_CONFIRMATION = """
✅ *Thanks {name}!*

We've saved your details:
📱 {phone}
✉️ {email}

📌 Here's what happens next:
1️⃣ Our team will review your request
2️⃣ We'll reach out in 2-4 hours
3️⃣ We'll send you a customized proposal

Is there anything else I can help you with? Reply "Menu" to see all options 👇
""".strip()

# Case Studies / Portfolio Message
PORTFOLIO_MESSAGE = """
🏆 *SEE OUR WORK*

Here are some of our success stories:

📊 *Case Study 1: Real Estate Client*
❌ Before: 20 leads/month
✅ After: 200+ leads/month (10x growth!)
🕐 Timeline: 3 months
💡 Strategy: Meta Ads + Lead Generation

📊 *Case Study 2: Ecommerce Store*
❌ Before: ₹50,000 monthly revenue
✅ After: ₹5,00,000+ monthly revenue
🕐 Timeline: 6 months
💡 Strategy: Google Ads + Social Media

📊 *Case Study 3: Coaching Institute*
❌ Before: 5 enrollments/month
✅ After: 50+ enrollments/month
🕐 Timeline: 4 months
💡 Strategy: Targeted Facebook Ads + Landing Pages

🎯 Ready to be our next success story?

👉 Let's schedule your free consultation!
""".strip()

# Out of hours message
OUT_OF_HOURS = """
🕐 *Out of Business Hours*

Hello! Thanks for reaching out to Dg Nagpur.

⏰ We're currently offline!

Our business hours are:
🕘 Monday - Friday: 9:00 AM - 6:00 PM IST
📞 Saturday - Sunday: Closed

📌 What you can do:
✅ Leave us a message - we'll reply within 2 hours (during business hours)
✅ Book a consultation - automatic scheduling available 24/7
✅ Check our website - www.dgnagpur.com

We look forward to helping you grow! 🚀
""".strip()

# Thank you message
THANK_YOU_MESSAGE = """
🙏 *Thank You!*

We appreciate you reaching out to Dg Nagpur!

📋 What we're doing:
✅ Reviewing your requirements
✅ Preparing personalized recommendations
✅ Scheduling a callback from our specialist

⏱️ Expected timeframe: 2-4 hours

📌 You'll hear from us on:
📱 WhatsApp
📞 Phone call
✉️ Email

If you have any urgent questions, feel free to message us anytime!

🌟 Looking forward to helping you succeed!
""".strip()

# Fallback message
FALLBACK_MESSAGE = """
Sorry, I didn't quite understand that. 🤔

Could you please:
✅ Reply with a number from the menu
✅ Or use clear keywords like:
   - "Services"
   - "Pricing"
   - "Consultation"
   - "Menu"

📋 *MAIN MENU* (Reply with number)

1️⃣ Our Services
2️⃣ Pricing Plans
3️⃣ Book Free Consultation
4️⃣ See Our Work
5️⃣ Talk to Expert

🤖 I'm here to help! What do you need? 👇
""".strip()

# Closing message
CLOSING_MESSAGE = """
😊 Thanks for chatting with us!

📌 *Remember:*
✨ We're always here to help
✨ No question is too small
✨ Your success is our priority

📞 *Quick Contact:*
📱 Phone: {phone}
✉️ Email: {email}
🌐 Website: {website}
📍 Location: {location}

💬 Feel free to reach out anytime!

*Let's grow your business together!* 🚀🎯
""".strip()

# Expert consultation
EXPERT_MESSAGE = """
👨‍💼 *TALK TO AN EXPERT*

Want to speak directly with our specialist?

Our team includes:
✅ Digital Marketing Specialist
✅ Google & Meta Ads Expert
✅ Web Developer
✅ SEO Strategist
✅ Social Media Manager

📞 Best way to connect:

Option 1️⃣: **Schedule a Free Call** - Choose your time ☎️
Option 2️⃣: **Chat with us now** - Message your question 💬
Option 3️⃣: **Call directly** - {phone} ☎️

Which would you prefer?
""".strip()

# Error handling
ERROR_MESSAGE = """
Oops! Something went wrong 😔

Please try again or:
📱 Call us: {phone}
✉️ Email us: {email}

We'll get back to you shortly! 🙏
""".strip()
