# 🚀 Quick Start Guide - DG Nagpur WhatsApp Chatbot

Get your chatbot running in 5 minutes!

## ⚡ Fastest Setup (Local Testing)

### Step 1: Open Terminal (2 minutes)
```bash
# Navigate to project
cd "c:\Users\manish\.vscode\dg nagpur whatsapp bot"

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Initialize Database (30 seconds)
```bash
python -c "from database import db; print('✅ Database ready')"
```

### Step 3: Test the Chatbot (2-3 minutes)
```bash
# Run interactive test
python test_chatbot.py

# Choose option 8 (Interactive Chat Mode)
# Type messages and see responses!
# Example messages:
#   "Hi"
#   "1" (to see services)
#   "3" (to book consultation)
```

✅ **Done!** Your chatbot is working locally.

---

## 📱 Send Real WhatsApp Messages (Add 15-20 minutes)

### Requirements:
- WhatsApp Business Account
- Meta Developer Account

### Quick Setup:

1. **Get WhatsApp Credentials**
   - Go to: https://developers.facebook.com/
   - Create app → Add WhatsApp product
   - Get: Phone Number ID, Access Token, Business Account ID

2. **Configure .env**
   ```bash
   # Copy template
   copy .env.example .env
   
   # Edit .env and add:
   - WHATSAPP_ACCESS_TOKEN=your_token
   - WHATSAPP_PHONE_NUMBER_ID=your_id
   - WHATSAPP_VERIFY_TOKEN=anything_random
   ```

3. **Setup Webhook (with Ngrok)**
   ```bash
   # Download ngrok from https://ngrok.com/
   
   # In new terminal:
   ngrok http 5000
   # You get: https://xxxx-xx-xxx-xxx.ngrok.io
   
   # In Meta Dashboard:
   # - Add webhook: https://xxxx-xx-xxx-xxx.ngrok.io/webhook
   # - Verify token: match your .env value
   # - Save
   ```

4. **Start Server**
   ```bash
   python app.py
   # Server running on http://localhost:5000
   ```

5. **Test!**
   - Send message from your WhatsApp to the bot number
   - Should get instant response

✅ **Running live!**

---

## 📊 Admin Commands

### View Leads
```bash
python utils.py list          # Show all leads
python utils.py lead +919876543210  # Show lead details
python utils.py hot           # Show hot leads
python utils.py analytics     # Show statistics
```

### Manage Data
```bash
python utils.py backup        # Backup database
python utils.py export        # Export to CSV
python utils.py manage status +919876543210 contacted
```

### Get Help
```bash
python utils.py help
```

---

## 📂 Project Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Main Flask server + WhatsApp API |
| `config.py` | Settings (services, pricing, etc.) |
| `messages.py` | All bot responses |
| `flows.py` | Conversation logic |
| `database.py` | Lead storage & management |
| `test_chatbot.py` | Test & sandbox mode |
| `utils.py` | Admin commands |
| `.env` | Your configuration secrets |

---

## 🎯 Typical User Conversation

```
👤 User: Hi
🤖 Bot: Welcome to Dg Nagpur! How can I help?
         1. Services | 2. Pricing | 3. Book Consultation

👤 User: 1
🤖 Bot: [Shows all services] Which are you interested in?

👤 User: 2
🤖 Bot: [Meta Ads info] Interested?

👤 User: Yes
🤖 Bot: Great! Let me ask you a few quick questions...

👤 User: [Answers qualification questions]

👤 User: [Provides name & email]

👤 User: [Books consultation slot]

🤖 Bot: ✅ Booking confirmed! You'll get meeting details.
```

---

## 🐛 Common Issues & Fixes

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "Port 5000 already in use"
```bash
# Use different port
set PORT=5001
python app.py

# Or kill existing process
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "Webhook not receiving messages"
```bash
# Check:
1. ngrok is running
2. .env has correct VERIFY_TOKEN
3. Meta webhook URL matches ngrok URL
4. Try again (sometimes takes 1-2 minutes)
```

### "Database errors"
```bash
# Reset database
del dg_nagpur_leads.db
python -c "from database import db; print('Reset')"
```

---

## 📞 Quick Reference

| Action | Command |
|--------|---------|
| Start chatbot | `python app.py` |
| Run tests | `python test_chatbot.py` |
| View leads | `python utils.py list` |
| View analytics | `python utils.py analytics` |
| Backup data | `python utils.py backup` |
| Export to CSV | `python utils.py export` |

---

## 🎓 Next Steps

1. **Customize Messages** (messages.py)
   - Change agency name
   - Update service descriptions
   - Modify pricing

2. **Customize Services** (config.py)
   - Add/remove services
   - Update pricing plans
   - Change target audience

3. **Add More Features**
   - Email confirmations
   - Calendar integration
   - CRM connection
   - Payment integration

4. **Deploy to Production**
   - See DEPLOYMENT_GUIDE.md
   - Setup real server
   - Configure SSL
   - Go live!

---

## 💡 Pro Tips

✅ **Customize agency details**: Edit `config.py` top section

✅ **Add more services**: Add to `SERVICES` dict in `config.py`

✅ **Change pricing**: Update `PRICING_PLANS` in `config.py`

✅ **Modify messages**: Edit `messages.py`

✅ **Track leads**: Use `python utils.py` commands

✅ **Backup regularly**: `python utils.py backup`

✅ **Monitor performance**: `python utils.py analytics`

---

## 📚 Documentation Links

- Full docs: See `README.md`
- Deployment guide: See `DEPLOYMENT_GUIDE.md`
- WhatsApp API: https://developers.facebook.com/docs/whatsapp
- Flask docs: https://flask.palletsprojects.com/

---

## ✨ Features at a Glance

✅ Automatic lead qualification
✅ Service information delivery
✅ Pricing information
✅ Consultation booking
✅ Portfolio/case studies
✅ Lead scoring (Hot/Warm/Cold)
✅ Conversation history tracking
✅ Analytics dashboard
✅ Admin commands
✅ WhatsApp Business API ready

---

## 🎯 Success Metrics

Once deployed, track:

📊 **Leads Generated**: Check via `python utils.py list`

💬 **Conversations**: View analytics

📈 **Conversion Rate**: Database tracks all stages

⏰ **Response Time**: Under 1 second (WhatsApp instant)

🎯 **Booking Rate**: See consultation_date in database

---

## 🚀 You're Ready!

Your professional WhatsApp chatbot for Dg Nagpur is ready to:
- ✅ Welcome customers 24/7
- ✅ Answer questions instantly
- ✅ Qualify leads automatically
- ✅ Book consultations
- ✅ Generate reports

**Next: Start the server and send your first message!** 🎉

---

**Questions?** Check README.md or DEPLOYMENT_GUIDE.md

**Ready to go live?** Follow DEPLOYMENT_GUIDE.md → Production Deployment

**Happy selling!** 🚀💼
