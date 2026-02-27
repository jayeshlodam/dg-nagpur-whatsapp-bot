# Message Templates for DG Nagpur WhatsApp Chatbot

from config import AGENCY_NAME, AGENCY_LOCATION, AGENCY_PHONE, AGENCY_EMAIL, AGENCY_WEBSITE, AGENCY_BUSINESS_HOURS

# Greeting and Welcome Messages
GREETING_MESSAGE = f"""
Hey there! 👋 

Welcome to Dg Nagpur! I'm here to help you with all your digital marketing needs. We've helped dozens of businesses just like yours grow their online presence and get more customers.

What brings you here today? 😊

Here's what we can do:
📱 Social Media (grow your followers & engagement)
🎯 Ads (Facebook, Instagram, Google - get real customers)
🌐 Website (professional site that converts)
📈 SEO (rank on Google & get free traffic)
🎨 Branding (stand out from competition)
💼 Lead Gen (get qualified leads daily)
✍️ Content (posts, blogs, videos that work)

Pick a number below or just tell me what you need!
""".strip()

MAIN_MENU = """
What would you like to know? 

1️⃣ Tell me about your services
2️⃣ How much does it cost?
3️⃣ I want to book a call with you
4️⃣ Show me your work (case studies)
5️⃣ Connect me with someone from your team

Just reply with 1-5 👇
""".strip()

# Service-related messages
SERVICE_INTRO = """
Cool! Let me walk you through what we do. Each service is designed to solve a specific business problem.

Pick what interests you most:

1️⃣ Social Media - Posts, engagement, community
2️⃣ Meta Ads - Facebook & Instagram ads that convert
3️⃣ Google Ads - Reach people searching for you
4️⃣ Website - Professional site that sells
5️⃣ SEO - Free organic traffic from Google
6️⃣ Branding - Logo, identity, make you memorable
7️⃣ Lead Generation - Get leads automatically
8️⃣ Content - Blogs, videos, sales copies

Type the number and I'll give you all the details! 👇
""".strip()

SERVICE_DETAILS = {
    "social_media": """
📱 **SOCIAL MEDIA MARKETING**

Get more followers, engagement, and real business results from social!

We manage:
✓ Facebook
✓ Instagram
✓ LinkedIn
✓ YouTube

What we do:
💡 Create engaging content
👥 Respond to messages & build community
📊 Track what's working
📈 Grow followers organically

Results: Average 300% engagement growth in 3 months

Starting ₹5,000/month

Ready to dominate social? Let's go! 👇
    """.strip(),
    
    "meta_ads": """
🎯 **META ADS (FACEBOOK & INSTAGRAM)**

Get your ads seen by the right people & watch sales come in!

What we do:
🎯 Target exactly who should see your ads
💡 Design ads that get clicks
🔄 Test different versions & find what works
📈 Track every sale back to the ad
💰 Get you the best price per customer

Results: Average 4-6x return in 30 days

Pricing: Ad spend + 15% management (minimum ₹5,000/month)

Which industry are you in?
1. Ecommerce
2. Real Estate
3. Coaching
4. Local Services
5. Other

Just pick a number 👇
    """.strip()
    
    "google_ads": """
🔍 **GOOGLE ADS (SEM)**

Show up when people are actively searching for what you sell!

What we do:
🔍 Find the right keywords
⚡ Write ads that get clicks
📱 Optimize for mobile
🔄 Keep improving the results
📊 Show you exactly what's working

Results: Average 5-8% conversion rate

Pricing: Ad spend + 15% management (minimum ₹5,000/month)

What type of business are you?
1. Ecommerce
2. Service-based  
3. B2B
4. Local Business
5. Other

Pick one 👇
    """.strip()
    
    "website_dev": """
🌐 **WEBSITE DEVELOPMENT**

Professional websites that look great and actually sell!

What we do:
🎨 Modern, beautiful design that works
💻 Super fast loading times
📱 Perfect on all devices (phone, tablet, desktop)
🔍 Built for Google search
⚙️ Easy to update yourself

Pricing: ₹15,000 - ₹1,00,000+ (depends on what you need)

What kind of website do you need?
1. Portfolio/Service showcase
2. Online store
3. Lead magnet/sign up site
4. Corporate site
5. Blog

Pick one 👇
    """.strip()
    
    "seo": """
📈 **SEO (SEARCH ENGINE OPTIMIZATION)**

Rank #1 on Google and get free customers forever!

What we do:
🔍 Find the keywords your customers search for
📝 Optimize your site for Google
🔗 Build quality backlinks
📊 Track rankings & improvements
💡 Update content for better results

Timeline: First results in 2-3 months
Results: 150-300% more organic traffic

Starting ₹8,000/month (4-month minimum)

What's your main goal?
1. Get more website visitors
2. Get more leads/inquiries
3. Improve search rankings
4. Build online visibility

Just pick one 👇
    """.strip()
    
    "branding": """
🎨 **BRANDING & DESIGN**

Stand out from the crowd with a memorable brand!

What we do:
🎨 Design stunning logos
🌈 Create consistent brand look
📱 Social media graphics
✍️ Your brand story & message
💻 Brand guidelines

Pricing: ₹10,000 - ₹50,000 (depends on scope)

What do you need?
1. Just a logo
2. Full brand identity (logo + colors + fonts)
3. Update existing brand
4. Social media graphics
5. Something else

Pick one 👇
    """.strip()
    
    "lead_gen": """
💼 **LEAD GENERATION**

Get a steady stream of qualified leads delivered to you!

What we do:
🎯 Find your ideal customers
📱 Run campaigns across Facebook, Google, LinkedIn
📝 Create landing pages that convert
✅ Verify & qualify every lead
📞 Deliver them to you ready to close

Results: 20-50 qualified leads/month (varies by industry)

Pricing: ₹2,000 - ₹10,000/month + ad spend

What industry are you in?
1. Real Estate
2. Coaching
3. B2B Services
4. Local Services
5. Other

Pick one 👇
    """.strip()
    
    "content": """
✍️ **CONTENT CREATION**

Get content that actually gets engagement & converts!

What we do:
✍️ Write SEO-friendly blog articles
📸 Create social media posts
🎬 Write video scripts
📰 Email newsletters
💬 Website copy that sells
📊 Plan content for the month

Results: More engagement, shares, and sales

Starting ₹3,000/month

What type of content do you need?
1. Blog articles
2. Social media posts
3. Video scripts
4. Sales page copy
5. All of the above

Pick one 👇
    """.strip(),
}

# Pricing messages
PRICING_HEADER = """
Here's what we offer - all with full support & results:
""".strip()

PRICING_STARTER = """
**🚀 STARTER - ₹8,000/month**
Perfect for small businesses just getting started

What's included:
✓ Social Media (2 platforms)
✓ 4 posts/week
✓ Monthly reports

Great for: Local businesses & startups
""".strip()

PRICING_GROWTH = """
**📊 GROWTH - ₹18,000/month**
For businesses ready to scale up

What's included:
✓ Social Media (3 platforms)
✓ 8 posts/week
✓ Lead generation campaigns
✓ Meta Ads (₹2,000/month)
✓ Bi-weekly calls

Great for: Growing businesses & online stores
""".strip()

PRICING_PREMIUM = """
**👑 PREMIUM - ₹35,000/month**
Complete digital marketing powerhouse

What's included:
✓ Social Media (4 platforms)
✓ Daily content
✓ Meta + Google Ads
✓ SEO optimization
✓ Blog writing
✓ Weekly strategy calls
✓ Full lead nurturing

Great for: Serious growth & scaling fast
""".strip()

PRICING_CUSTOM = """
**🎯 CUSTOM SOLUTIONS**
Need something unique? We build it!

We create custom packages based on:
✓ Your specific goals
✓ Your budget
✓ Timeline  
✓ Current challenges

Perfect for companies with unique needs!

Interested? Let's chat about what you need 👋
""".strip()

# Lead Qualification Messages
LEAD_QUALIFY_START = """
Perfect! I just need to understand your business a bit better so I can give you the best recommendations. Won't take long! 😊

First up - what kind of business are you in?

1️⃣ Real Estate
2️⃣ Ecommerce (selling products online)
3️⃣ Coaching/Training/Education
4️⃣ Local Services (salon, gym, clinic, etc)
5️⃣ B2B Services
6️⃣ Something else

Just pick a number 👇
""".strip()

LEAD_BUDGET = """
Got it! Now, what's your monthly marketing budget? No wrong answer here 😊

1️⃣ Less than ₹5,000/month
2️⃣ ₹5,000 - ₹15,000/month
3️⃣ ₹15,000 - ₹30,000/month
4️⃣ ₹30,000 - ₹50,000/month
5️⃣ More than ₹50,000/month
6️⃣ Not sure yet (we can figure it out)

Shoot your answer 👇
""".strip()

LEAD_GOAL = """
Almost there! Last question - what do you want to achieve?

1️⃣ Get more leads/inquiries
2️⃣ Increase sales/revenue
3️⃣ Build brand awareness
4️⃣ Get more website traffic
5️⃣ All of the above!

Pick one (or more) 👇
""".strip()

# Consultation Booking
CONSULTATION_INTRO = """
Perfect! Let's get you booked in with one of our experts 📅

This is usually a 30-min chat where we:
✓ Understand your current situation
✓ Talk about your goals
✓ Show you exactly what we can do

When works best for you? (Next 7 days)

(Just share a date and time like: 15/02 at 2:00 PM)
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
🎉 You're all set, {name}!

Consultation booked:
📅 {datetime}
🎤 Video call link will be sent 1 hour before

In the meantime, we're putting together some ideas specifically for you. See you soon! 👋
""".strip()

# Contact Information Collection
CONTACT_NAME = """
Awesome! Now let me get your details so we can connect properly 😊

What's your name?
""".strip()

CONTACT_PHONE = """
Got it! And what's the best number to reach you?

(We only use this to follow up with you)
""".strip()

CONTACT_EMAIL = """
Perfect! One more - what's your email? 

(For sending you personalized recommendations & meeting links)
""".strip()

CONTACT_CONFIRMATION = """
✨ Awesome, {name}! We've got all your details:

📱 {phone}
✉️ {email}

Here's what happens next:
👉 Our team will review what you need (this usually takes 1-2 hours)
👉 We'll send you personalized recommendations
👉 Then we'll reach out to discuss strategy

Is there anything else you'd like to know right now? Or I can help you look at a specific service? 👇
""".strip()

# Case Studies / Portfolio Message
PORTFOLIO_MESSAGE = """
Absolutely! Here's what we've done recently:

💼 **Our Work:**
📈 Helped 200+ brands grow on Instagram (some by 10x!)
🔍 Rank #1 on Google for competitive keywords  
💰 Generated $2M+ in sales for our clients
📱 Built engaged communities of 50k+ followers

Want to see case studies from companies like yours? Just let me know what industry you're in! 👈
""".strip()

# Out of hours message
OUT_OF_HOURS = """
Thanks for reaching out! 😊

We're currently offline (outside business hours), but we'll be back soon! ⏰

Our hours:
🕘 Monday - Friday: 9:00 AM - 6:00 PM IST
📍 Closed on weekends

Quick tips while you wait:
✅ Book a consultation - works 24/7 (no waiting!)
✅ Drop a message - we'll reply first thing when we're back
✅ Check www.dgnagpur.com for more info

We appreciate the message and will get back to you ASAP! 🚀
""".strip()

# Thank you message
THANK_YOU_MESSAGE = """
Thanks so much for getting in touch! 🙌

Here's what happens next:
✅ Our team will review what you need (1-2 hours)
✅ We'll put together personalized recommendations
✅ Someone will reach out to you soon

📱 Check your WhatsApp/phone for our message

Anything else you'd like to know in the meantime? I'm here! 😊
""".strip()

# Fallback message
FALLBACK_MESSAGE = """
Hmm, didn't quite catch that! 😅

Just to help - you can:
✅ Reply with a number from the menu (like "1")
✅ Or just type a keyword:
   • "Services"
   • "Pricing"
   • "Book"
   • "Consultation"

**MAIN MENU** (Pick one):

1️⃣ Our Services
2️⃣ Pricing Plans
3️⃣ Book Free Consultation
4️⃣ Our Work
5️⃣ Talk to Expert

What'd you like? 👇
""".strip()

# Closing message
CLOSING_MESSAGE = """
Thanks for chatting! 😊

**Quick reminder:**
📱 We're here whenever you need us
💬 Feel free to ask anything
🎯 Your success is what we care about most

**Keep in touch:**
📞 Phone: {phone}
✉️ Email: {email}
🌐 Website: {website}

Talk soon! 👋
""".strip()

# Expert consultation
EXPERT_MESSAGE = """
Of course! You'll be working with our top strategists:

🎯 **Harshit & Team:**
- 10+ years in digital marketing
- Certified Google & Meta partners
- Led campaigns for 100+ brands
- Experts in SEO, Ads & Social Media  

They'll personally work on your strategy. You're in good hands! 🙌
""".strip()

# Error handling
ERROR_MESSAGE = """
Oops! Something went wrong 😔

No worries - just:
📱 Call us at {phone}
✉️ Or email {email}

We'll get it sorted right away! 🙏
""".strip()
