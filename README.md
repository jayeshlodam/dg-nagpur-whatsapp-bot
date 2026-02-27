# DG Nagpur WhatsApp Chatbot

A professional, intelligent WhatsApp chatbot for Dg Nagpur digital marketing agency. Designed to generate leads, qualify prospects, book consultations, and provide information about digital marketing services.

## 📋 Features

✅ **Intelligent Conversation Management**
- Multiple conversation states and flows
- Context-aware responses
- Natural language understanding
- Lead qualification system

✅ **Lead Management**
- Automatic lead scoring (Cold/Warm/Hot)
- Lead qualification questions
- Contact information collection
- Lead history and analytics

✅ **Service Information**
- Detailed service descriptions
- Service-specific recommendations
- Pricing information
- Case studies and portfolio

✅ **Consultation Booking**
- Date and time availability
- Automatic confirmation
- Calendar integration ready
- Reminder system

✅ **Analytics & Reporting**
- Message tracking
- Conversation metrics
- Lead conversion tracking
- Admin dashboard ready

✅ **WhatsApp Business API Integration**
- Full WhatsApp Business API support
- Message sending and receiving
- Template message support
- Media handling

## 🎯 Services Offered

The chatbot provides information about:
- 📱 Social Media Marketing
- 🎯 Meta Ads (Facebook & Instagram)
- 🔍 Google Ads
- 🌐 Website Development
- 📈 SEO
- 🎨 Branding & Design
- 💼 Lead Generation
- ✍️ Content Creation

## 💰 Pricing Plans

1. **Starter Pack** - ₹8,000/month
2. **Growth Pack** - ₹18,000/month
3. **Premium Pack** - ₹35,000/month
4. **Custom Solutions** - Tailored pricing

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Flask
- WhatsApp Business Account
- Ngrok (for local testing)

### Installation

1. **Clone and setup:**
```bash
cd "dg nagpur whatsapp bot"
python -m venv venv
source venv/Scripts/activate  # On Windows
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your WhatsApp credentials
```

4. **Initialize database:**
```python
python -c "from database import db; print('Database initialized')"
```

5. **Run the server:**
```bash
python app.py
```

The server will start on `http://localhost:5000`

## 🔧 Environment Configuration

Create a `.env` file based on `.env.example`:

```env
# WhatsApp Configuration
WHATSAPP_VERIFY_TOKEN=your_verify_token
WHATSAPP_ACCESS_TOKEN=your_access_token
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
WHATSAPP_BUSINESS_ACCOUNT_ID=your_business_account_id

# Server Configuration
DEBUG=False
PORT=5000

# Agency Details
AGENCY_PHONE=+91XXXXXXXXXX
AGENCY_EMAIL=info@dgnagpur.com
AGENCY_WEBSITE=www.dgnagpur.com
```

## 📱 WhatsApp Business API Setup

### 1. Get Your Credentials

1. Go to [Meta for Developers](https://developers.facebook.com/)
2. Create an app (Business type)
3. Add WhatsApp product
4. Generate access token
5. Get your Phone Number ID and Business Account ID

### 2. Configure Webhook

1. In your Meta Developer app settings:
   - Go to WhatsApp → Configuration
   - Add webhook URL: `https://yourdomain.com/webhook`
   - Verify token: Use the token from your `.env`

2. Subscribe to webhook events:
   - messages
   - message_status
   - message_template_status_update

### 3. Test Locally

```bash
# Install ngrok
# Run ngrok
ngrok http 5000

# Use ngrok URL as webhook URL
# Example: https://xxxxx.ngrok.io/webhook
```

## 📊 Conversation Flow

```
Start
  ↓
Greeting & Main Menu
  ├→ Services → Service Details → Lead Qualification → Consultation
  ├→ Pricing → Custom Quote → Consultation
  ├→ Book Consultation → Lead Qualification → Consultation Booking
  ├→ Portfolio → Main Menu
  └→ Expert → Main Menu
```

## 💾 Database Schema

### Leads Table
- `id`: Unique identifier
- `phone_number`: WhatsApp phone
- `name`: Customer name
- `email`: Email address
- `business_type`: Type of business
- `budget_range`: Marketing budget
- `goal`: Main marketing goal
- `lead_score`: 0-100 score
- `lead_category`: Hot/Warm/Cold
- `services_interested`: Services selected
- `consultation_date`: Booked date
- `consultation_time`: Booked time
- `status`: new/contacted/converted/lost
- `created_at`: Timestamp
- `updated_at`: Timestamp

### Conversations Table
- `id`: Message ID
- `phone_number`: Sender
- `user_message`: User input
- `bot_response`: Bot response
- `session_state`: Conversation state
- `created_at`: Timestamp

### Bookings Table
- `id`: Booking ID
- `lead_id`: Associated lead
- `consultation_date`: Date
- `consultation_time`: Time
- `duration`: Duration (minutes)
- `status`: pending/confirmed/completed
- `meeting_link`: Calendar link
- `notes`: Additional notes

## 🔌 API Endpoints

### Webhook
- **POST** `/webhook` - Receive messages from WhatsApp
- **GET** `/webhook` - Webhook verification

### Leads Management
- **GET** `/api/leads` - Get all leads
- **GET** `/api/leads?filter=hot` - Filter by category
- **GET** `/api/leads/<phone>` - Get lead details
- **PUT** `/api/leads/<phone>` - Update lead

### Other Endpoints
- **GET** `/api/analytics` - Get analytics data
- **POST** `/api/send-message` - Send manual message
- **GET** `/api/bookings/<date>` - Get bookings for date
- **GET** `/health` - Health check

## 📈 Lead Scoring

Lead score is calculated based on:
- Contact information provided (20 points)
- Business details (15 points)
- Budget and goals (40 points)
- Engagement level (15 points)
- Service interest (10 points)

**Categories:**
- 🔴 **Cold**: 0-49 points
- 🟡 **Warm**: 50-79 points
- 🟢 **Hot**: 80-100 points

## 🎯 Sample Conversation

```
User: Hi
Bot: 👋 Welcome to Dg Nagpur!
     [Shows main menu]

User: 1
Bot: [Shows all services]

User: 2
Bot: [Shows Meta Ads details]

User: Yes
Bot: [Starts lead qualification]

User: Real Estate
Bot: [Asks about budget]

User: 2 (₹5,000 - ₹15,000)
Bot: [Asks about goal]

User: 1 (Generate leads)
Bot: [Calculates lead score and asks for contact info]

User: John Sharma
Bot: [Asks for email]

User: john@example.com
Bot: [Offers consultation booking]
```

## 🔐 Security

- Access tokens stored in environment variables
- Webhook verification with token
- Input validation and sanitization
- SQL injection prevention (using parameterized queries)
- CORS enabled for trusted domains
- Error logging without sensitive data

## 📝 Customization

### Change Agency Details
Edit `config.py`:
```python
AGENCY_NAME = "Your Agency Name"
AGENCY_LOCATION = "City, Country"
AGENCY_PHONE = "+91XXXXXXXXXX"
AGENCY_EMAIL = "email@domain.com"
```

### Add New Services
In `config.py` SERVICES dict:
```python
"service_key": {
    "name": "Service Name",
    "description": "Service description",
    "price_range": "Pricing"
}
```

### Customize Messages
Edit `messages.py` and add/modify message templates

### Add New Flows
Extend `ConversationFlow` class in `flows.py`

## 📊 Monitoring & Logging

- Logs stored in console output
- Configure file logging by updating logging config in `app.py`
- Metrics tracked in database (analytics table)
- Analytics API available at `/api/analytics`

## 🚢 Deployment

### Using Gunicorn (Recommended)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

### Environment: Heroku, AWS, Google Cloud, Azure
- Set environment variables
- Configure webhook URL
- Scale as needed

## 📚 Document Structure

```
dg nagpur whatsapp bot/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── messages.py            # Message templates
├── flows.py               # Conversation flows
├── database.py            # Database management
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── README.md             # Documentation
└── dg_nagpur_leads.db    # SQLite database (generated)
```

## 🐛 Troubleshooting

### Webhook not receiving messages
- Check webhook URL is accessible
- Verify token matches
- Check event subscriptions
- Review server logs

### Messages not sending
- Verify access token is valid
- Check phone number format (include country code)
- Ensure account is approved for messaging
- Check rate limits

### Lead data not saving
- Verify database permissions
- Check database file location
- Review error logs
- Ensure phone_number is unique

## 📞 Support & Contact

For issues or customization:
- 📧 Email: info@dgnagpur.com
- 📱 WhatsApp: [Campaign messages via bot]
- 🌐 Website: www.dgnagpur.com

## 📄 License

This chatbot is proprietary software for Dg Nagpur. All rights reserved.

## 🎉 Success Metrics

This chatbot is designed to:
- ✅ Generate 20-50+ qualified leads per month
- ✅ Automate 80% of initial customer interactions
- ✅ Reduce response time to under 1 minute
- ✅ Improve lead qualification accuracy
- ✅ Increase consultation booking rate by 40%

---

**Made with ❤️ for Dg Nagpur** 🚀🎯
