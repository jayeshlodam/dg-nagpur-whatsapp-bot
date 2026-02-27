# Deployment & Setup Guide for DG Nagpur WhatsApp Chatbot

## 📋 Table of Contents
1. [Local Development Setup](#local-development-setup)
2. [WhatsApp Business API Setup](#whatsapp-business-api-setup)
3. [Production Deployment](#production-deployment)
4. [Testing & Validation](#testing--validation)
5. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Local Development Setup

### Step 1: Prerequisites
```bash
# Windows
python --version  # Should be 3.8+
pip --version
```

### Step 2: Create Virtual Environment
```bash
# Navigate to project folder
cd "dg nagpur whatsapp bot"

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
# Copy example to actual config
copy .env.example .env
# Or on Mac/Linux:
cp .env.example .env

# Edit .env with your credentials
# (For local testing, you can use dummy values)
```

### Step 5: Initialize Database
```bash
python -c "from database import db; print('Database initialized')"
# This creates dg_nagpur_leads.db
```

### Step 6: Test Locally
```bash
# Option 1: Run test suite
python test_chatbot.py
# Choose interactive mode (option 8) to test manually

# Option 2: Start the server
python app.py
# Server will run on http://localhost:5000
```

---

## WhatsApp Business API Setup

### Phase 1: Create Meta Developer Account

1. **Go to [Meta Developers](https://developers.facebook.com/)**
   - Sign in with your Facebook account
   - Create new account if needed

2. **Create an App**
   - Click "Create App"
   - Choose "Business" as app type
   - Fill in app details:
     - App Name: "DG Nagpur Chatbot"
     - App Contact Email: your@email.com
     - App Type: Business

### Phase 2: Add WhatsApp Product

1. **In your App Dashboard**
   - Click "Add Product"
   - Search for "WhatsApp"
   - Click "Set Up"
   - Choose "WhatsApp Business API"

2. **Select Business Account**
   - Create or select existing WhatsApp Business Account
   - Confirm phone number to use

### Phase 3: Get Credentials

1. **Find Phone Number ID**
   - Go to WhatsApp → Phone Numbers
   - Copy your Phone Number ID
   - Add to .env: `WHATSAPP_PHONE_NUMBER_ID=xxx`

2. **Generate Access Token**
   - Go to WhatsApp → API Setup
   - Click "Generate Token"
   - Copy token
   - Add to .env: `WHATSAPP_ACCESS_TOKEN=xxx`

3. **Find Business Account ID**
   - Go to Settings → Business Accounts
   - Copy Business Account ID
   - Add to .env: `WHATSAPP_BUSINESS_ACCOUNT_ID=xxx`

### Phase 4: Configure Webhook

#### For Local Testing (Using Ngrok)

1. **Install Ngrok**
   ```bash
   # Download from https://ngrok.com/download
   # Or via package manager
   ```

2. **Start Ngrok**
   ```bash
   ngrok http 5000
   # You'll get a URL like: https://xxxx-xx-xxx-xxx.ngrok.io
   ```

3. **Configure Webhook in Meta**
   - Go to WhatsApp → Configuration
   - In Webhook URL, enter: `https://xxxx-xx-xxx-xxx.ngrok.io/webhook`
   - In Verify Token, enter your custom token
   - Add to .env: `WHATSAPP_VERIFY_TOKEN=your_token_here`

4. **Subscribe to Events**
   - In "Webhook Fields", select:
     - messages
     - message_status
     - message_template_status_update

5. **Verify Webhook**
   - Click "Verify and Save"
   - Meta will send a verification request
   - Your app will respond with the challenge

#### For Production (Using Real Server)

1. **Get Domain**
   - Purchase domain (e.g., dg-nagpur-bot.com)
   - Point to your server IP

2. **Configure Webhook**
   - Webhook URL: `https://dg-nagpur-bot.com/webhook`
   - Verify Token: Generate secure random token
   - Add to .env

3. **Use HTTPS**
   - Get SSL certificate (Let's Encrypt free)
   - Configure on your server

### Phase 5: Test Connection

1. **Start Your Server**
   ```bash
   python app.py
   ```

2. **Send Test Message**
   - Use WhatsApp on your phone
   - Message your bot number
   - You should receive automated response

3. **Check Logs**
   ```bash
   # Look for logs showing:
   # - Message received
   # - Response sent
   # - Conversation logged
   ```

---

## Production Deployment

### Option 1: Deploy to Heroku

1. **Create Heroku Account**
   - Go to [Heroku](https://www.heroku.com/)
   - Sign up free

2. **Install Heroku CLI**
   ```bash
   # Windows: Download installer
   # Mac: brew tap heroku/brew && brew install heroku
   heroku --version
   ```

3. **Create Procfile**
   - In project root, create `Procfile`:
   ```
   web: gunicorn -w 4 -b 0.0.0.0:$PORT app:app
   ```

4. **Create runtime.txt**
   ```
   python-3.9.0
   ```

5. **Deploy**
   ```bash
   heroku login
   heroku create dg-nagpur-bot
   git push heroku main
   heroku config:set WHATSAPP_ACCESS_TOKEN=your_token
   # Add all .env variables similarly
   ```

6. **Configure Webhook**
   - Webhook URL: `https://dg-nagpur-bot.herokuapp.com/webhook`

### Option 2: Deploy to AWS

1. **Create EC2 Instance**
   - Choose Ubuntu 20.04 LTS
   - Create security group (open port 443 for HTTPS)
   - Create key pair and download

2. **Connect to Instance**
   ```bash
   ssh -i key.pem ubuntu@your-instance-ip
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   sudo apt install nginx
   ```

4. **Deploy Application**
   ```bash
   git clone your-repo.git
   cd dg-nagpur-whatsapp-bot
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Configure Nginx**
   ```nginx
   server {
       listen 443 ssl;
       server_name your-domain.com;
       
       ssl_certificate /path/to/cert.pem;
       ssl_certificate_key /path/to/key.pem;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
       }
   }
   ```

6. **Run Application**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

### Option 3: Deploy to Google Cloud

1. **Create Cloud Run Service**
   - Go to Google Cloud Console
   - Enable Cloud Run API
   - Enable Artifact Registry

2. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:$PORT", "app:app"]
   ENV PORT=5000
   ```

3. **Deploy**
   ```bash
   gcloud run deploy dg-nagpur-bot --source .
   ```

### Option 4: Deploy to AWS Lambda (Serverless)

1. **Create Lambda Function**
   - Runtime: Python 3.9
   - Handler: app.lambda_handler

2. **Use Zappa**
   ```bash
   pip install zappa
   zappa init
   zappa deploy production
   ```

---

## Testing & Validation

### Manual Testing

```bash
# Start test suite
python test_chatbot.py

# Choose:
# 1 = Full lead flow
# 2 = Service inquiry
# 3 = Pricing
# 4 = Portfolio
# 5 = Expert connect
# 6 = Error handling
# 7 = Booking
# 8 = Interactive mode
```

### Admin Commands

```bash
# View all leads
python utils.py list

# View specific lead
python utils.py lead +919876543210

# View hot leads
python utils.py hot

# View analytics
python utils.py analytics

# Export leads
python utils.py export

# Backup database
python utils.py backup
```

### API Testing

```bash
# Health check
curl -X GET http://localhost:5000/health

# Get all leads
curl -X GET http://localhost:5000/api/leads

# Get specific lead
curl -X GET http://localhost:5000/api/leads/+919876543210

# Get analytics
curl -X GET http://localhost:5000/api/analytics?metric=message_received

# Send test message
curl -X POST http://localhost:5000/api/send-message \
  -H "Content-Type: application/json" \
  -d '{
    "phone": "+919876543210",
    "message": "Test message"
  }'
```

---

## Monitoring & Maintenance

### Daily Tasks

```bash
# Check application status
# Monitor error logs
# Verify webhook connectivity

# View leads dashboard
python utils.py analytics

# Check today's bookings
python utils.py bookings
```

### Weekly Tasks

```bash
# Export lead data
python utils.py export

# Review conversation logs
# Check lead conversion rates
# Analyze engagement metrics

# Backup database
python utils.py backup
```

### Monthly Tasks

```bash
# Full database optimization
# Analyze performance
# Plan follow-up strategies
# Update service information
# Review pricing
```

### Troubleshooting

**Issue: Webhook not receiving messages**
```bash
# Check:
1. Webhook URL is accessible
2. Verify token matches
3. Events are subscribed
4. HTTPS certificate is valid
5. Check application logs
```

**Issue: Database locked**
```bash
# Solution:
rm dg_nagpur_leads.db
# Reinitialize
python -c "from database import db; print('Reinitialized')"
```

**Issue: Messages not sending**
```bash
# Check:
1. Access token is valid
2. Phone number format (with country code)
3. Account has message permissions
4. No rate limiting

# Check logs
tail -f app.log  # or check terminal output
```

**Issue: High response time**
```bash
# Solutions:
1. Increase Gunicorn workers
   gunicorn -w 8 -b 0.0.0.0:5000 app:app
2. Enable caching
3. Optimize database queries
4. Use CDN for static content
```

### Performance Optimization

```python
# In config.py, for production:
DEBUG = False
MESSAGE_DELAY = 0.5  # Reduce delay
SESSION_TIMEOUT = 60  # Increase timeout
```

### Security Checklist

- [ ] All credentials in environment variables
- [ ] HTTPS enabled
- [ ] Rate limiting configured
- [ ] Input validation active
- [ ] SQL injection prevention (using parameterized queries)
- [ ] CORS properly configured
- [ ] Access logs enabled
- [ ] Error logging doesn't expose secrets
- [ ] Regular security updates
- [ ] Backup strategy in place

---

## Support & Resources

**Documentation**
- [WhatsApp Business API Docs](https://developers.facebook.com/docs/whatsapp)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

**Tools**
- Postman - API testing
- Ngrok - Local tunneling
- WhatsApp Business Manager - Lead management
- Google Analytics - Website tracking

**Contact Support**
- Email: info@dgnagpur.com
- WhatsApp: Via chatbot
- Website: www.dgnagpur.com

---

## Checklist: Ready for Production

- [ ] All environment variables configured
- [ ] Database initialized and tested
- [ ] WhatsApp Business API credentials verified
- [ ] Webhook URL configured and verified
- [ ] SSL certificate installed
- [ ] Backup strategy implemented
- [ ] Monitoring and logging enabled
- [ ] Team trained on admin commands
- [ ] Test messages sent and verified
- [ ] Analytics dashboard accessible
- [ ] Lead scoring tested
- [ ] Consultation booking tested
- [ ] Pricing and service info updated
- [ ] Database backed up
- [ ] Performance tested under load

---

✅ **All set? Your chatbot is ready to generate leads!** 🚀

For questions or issues, reach out to your development team.
