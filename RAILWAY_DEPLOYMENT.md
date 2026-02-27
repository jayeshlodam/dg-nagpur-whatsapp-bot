# 🚀 Deploy DG Nagpur WhatsApp Chatbot on Railway

Railway is a modern, easy-to-use cloud platform. Perfect for deploying your chatbot!

**Deployment Time**: 15-20 minutes  
**Cost**: Free tier available ($5/month minimal)  
**Difficulty**: Beginner-friendly

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Create Railway Account](#create-railway-account)
3. [Prepare Your Project](#prepare-your-project)
4. [Deploy via GitHub](#deploy-via-github)
5. [Configure Environment](#configure-environment)
6. [Test Your Deployment](#test-your-deployment)
7. [Setup WhatsApp Webhook](#setup-whatsapp-webhook)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

✅ **You need:**
- [Git](https://git-scm.com/) installed on your computer
- GitHub account (free at github.com)
- WhatsApp Business Account credentials (phone ID, access token)
- Your chatbot code (already created!)

✅ **Check if you have them:**
```bash
git --version
# Should show: git version 2.xx.x
```

---

## Create Railway Account

### Step 1: Sign Up
1. Go to **[railway.app](https://railway.app/)**
2. Click **"Start Free"** button (top right)
3. Choose: **Sign up with GitHub**
   - Click "Authorize railway-app"
   - Complete GitHub authorization

### Step 2: Create New Project
1. After login, click **"Create New Project"**
2. Select **"GitHub Repo"**
   - (Or "Deploy from Repo" if you see it)

✅ **Done!** You now have a Railway account.

---

## Prepare Your Project

### Step 1: Create GitHub Repository

1. Go to **[github.com/new](https://github.com/new)**
2. Create repository:
   - **Name**: `dg-nagpur-whatsapp-bot`
   - **Description**: "WhatsApp Chatbot for Digital Marketing"
   - **Public** (for free deployment)
   - Click **"Create repository"**

3. Copy the HTTPS URL shown (looks like: `https://github.com/YOUR-USERNAME/dg-nagpur-whatsapp-bot.git`)

### Step 2: Push Code to GitHub

**On your computer:**

```bash
# Navigate to your project
cd "c:\Users\manish\.vscode\dg nagpur whatsapp bot"

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: DG Nagpur WhatsApp Chatbot"

# Add remote (replace with YOUR URL from step 1)
git remote add origin https://github.com/YOUR-USERNAME/dg-nagpur-whatsapp-bot.git

# Push to GitHub
git branch -M main
git push -u origin main
```

✅ Your code is now on GitHub!

---

## Deploy via GitHub

### Step 1: Connect GitHub to Railway

1. Go back to **[railway.app](https://railway.app/)**
2. Click **"New Project"**
3. Select **"GitHub Repo"**
4. Click **"Configure GitHub App"** (if prompted)
   - Authorize Railway to access your repos
5. Select your repo: **`dg-nagpur-whatsapp-bot`**

### Step 2: Railway Auto-Deploys

Railway will:
- ✅ Detect Python project
- ✅ Install requirements.txt
- ✅ Start the app automatically

**You should see:**
```
✓ Build successful
✓ Deployment complete
```

### Step 3: Get Your Railway URL

1. In Railway dashboard, click your project
2. Go to **Deployments** tab
3. Find the public URL (looks like: `https://dg-nagpur-whatsapp-bot-production.up.railway.app/`)

✅ **Save this URL!** You'll need it for WhatsApp webhook.

---

## Configure Environment

### Step 1: Add Environment Variables

1. In Railway dashboard, go to **Variables** tab
2. Click **"Add Variable"**
3. Add these variables one by one:

```
WHATSAPP_VERIFY_TOKEN = your_random_verify_token_123
WHATSAPP_ACCESS_TOKEN = your_actual_whatsapp_token_here
WHATSAPP_PHONE_NUMBER_ID = 1234567890123456
WHATSAPP_BUSINESS_ACCOUNT_ID = 1234567890123456
DEBUG = False
PORT = 8000
AGENCY_PHONE = +919999999999
AGENCY_EMAIL = info@dgnagpur.com
AGENCY_WEBSITE = www.dgnagpur.com
```

### Step 2: Get WhatsApp Credentials

If you don't have them yet:

1. Go to [Meta Developers](https://developers.facebook.com/)
2. Create App → Add WhatsApp product
3. Get:
   - **Phone Number ID**: WhatsApp → Phone Numbers
   - **Access Token**: WhatsApp → API Setup → Generate Token
   - **Business Account ID**: Settings → Business Accounts

### Step 3: Save Variables

- Click **"Save"** after each variable
- Railway will auto-restart your app

✅ Variables are now configured!

---

## Test Your Deployment

### Step 1: Test Health Endpoint

```bash
# Replace with YOUR Railway URL
curl https://your-railway-url/health

# Should return:
# {"status": "healthy", "timestamp": "...", "service": "DG Nagpur WhatsApp Chatbot"}
```

Or open in browser:
```
https://your-railway-url/health
```

### Step 2: Check Logs

In Railway dashboard:
1. Go to **Logs** tab
2. Should see: `Starting DG Nagpur WhatsApp Chatbot`
3. No errors = ✅ Good!

### Step 3: View Leads API

```bash
# Replace with YOUR Railway URL
curl https://your-railway-url/api/leads

# Should return:
# {"status": "success", "leads": []}
```

✅ Your app is running!

---

## Setup WhatsApp Webhook

### Step 1: Configure in Meta Dashboard

1. Go to [Meta Developers](https://developers.facebook.com/)
2. Open your WhatsApp app
3. Go to **WhatsApp → Configuration**
4. In **Webhook URL**, enter:
   ```
   https://your-railway-url/webhook
   ```
   (Replace with your actual Railway URL)

5. In **Verify Token**, enter:
   ```
   your_random_verify_token_123
   ```
   (Must match the token in Railway Variables)

### Step 2: Click "Verify and Save"

Meta will:
- ✅ Send a verification request to your webhook
- ✅ Your app will respond with the challenge
- ✅ Meta confirms and saves

**If it doesn't work:**
- Check the URL is correct (include `https://`)
- Check verify token matches exactly
- Check Railway logs for errors: `python app.py` logs

### Step 3: Subscribe to Events

In Meta dashboard:
1. Scroll down to **"Webhook fields"**
2. Select these checkboxes:
   - ✅ messages
   - ✅ message_status
   - ✅ message_template_status_update

3. Click **"Save"**

✅ Webhook is configured!

---

## Test WhatsApp Messages

### Step 1: Send Test Message

1. Open WhatsApp on your phone
2. Message the bot phone number
3. Wait 2-3 seconds

### Step 2: Check Response

You should receive:
```
👋 Welcome to Dg Nagpur!

I'm your digital marketing assistant...

📋 MAIN MENU

1️⃣ Our Services
2️⃣ Pricing Plans
...
```

### Step 3: Check Logs

In Railway dashboard → **Logs** tab:
- You should see:
  ```
  Message from +919876543210: [your message]
  Response sent to +919876543210: State=menu
  ```

✅ **Live!** Your chatbot is working!

---

## Monitor Your Deployment

### View Dashboard

In Railway:
1. **Deployments** - See active versions
2. **Logs** - Real-time logs
3. **Variables** - View all environment settings
4. **Metrics** - CPU, Memory, Network usage

### Admin Commands (Still Work!)

Even deployed on Railway, you can run local commands:

```bash
# From your computer (with venv activated):
python utils.py list              # View all leads
python utils.py analytics         # View statistics
python utils.py backup            # Backup database
python utils.py export            # Export leads to CSV
```

The local database queries a file locally. For production, add remote database access if needed.

### Check Leads Online

```bash
# Replace with YOUR Railway URL
curl https://your-railway-url/api/leads

# Returns all leads in JSON format
```

---

## Troubleshooting

### Problem: "Deployment Failed"

**Solution:**
1. Check Railway logs (Logs tab)
2. Common reason: Missing `Procfile`
3. Create `Procfile` in project root:
   ```
   web: gunicorn -w 4 -b 0.0.0.0:$PORT app:app
   ```
4. Push to GitHub: `git add . && git commit -m "Add Procfile" && git push`
5. Railway auto-redeploys

### Problem: "Webhook not verifying"

**Solution:**
1. Check URL is correct (with `https://`)
2. Check verify token matches exactly
3. Ensure `PORT` variable is not set too high
4. Try in Railway logs: `curl -X GET http://localhost:5000/webhook?hub.verify_token=... &hub.challenge=...`

### Problem: "Receiving messages but no response"

**Solution:**
1. Check `WHATSAPP_ACCESS_TOKEN` is correct
2. Ensure phone number format is correct (with country code, no spaces)
3. Check Railway logs for errors
4. Restart deployment: Click the deploy action → Redeploy

### Problem: "Database says 'leads.db not found'"

**Solution:**
- SQLite file is created automatically on first run
- Check Railway logs for any database errors
- If issue persists: Add this to startup
  ```python
  from database import db
  print("Database initialized")
  ```

### Problem: "Can't connect with ngrok locally"

**Solution:**
- For Railway, you don't need ngrok!
- Railway gives you a real HTTPS URL
- Use the Railway URL for WhatsApp webhook

---

## What's Running on Railway?

✅ Your Flask app (`app.py`)  
✅ SQLite database (`dg_nagpur_leads.db`)  
✅ Automatic Gunicorn server  
✅ Free SSL/HTTPS certificate  
✅ Always-on (24/7)  

---

## Pricing on Railway

**Free Tier:**
- $5/month free credit
- Perfect for starting
- No credit card required initially

**When you scale:**
- Additional usage: $0.50/hour for compute
- Database storage: Included free
- Bandwidth: $1/GB after free tier

**Estimated monthly cost:** $0-5/month for your chatbot

---

## Update Your Chatbot

To deploy new changes:

```bash
# Make changes to your code
# Edit files, test locally

# Push to GitHub
git add .
git commit -m "Update: [description]"
git push origin main

# Railway auto-detects changes and redeploys
# Within 1-2 minutes, new version is live!
```

---

## Enable Advanced Features

### Enable Persistent Storage

After reaching a few hundred leads, add a database:

1. In Railway, go to **Plugins**
2. Click **"Add Plugin"**
3. Select **"PostgreSQL"**
4. Railway automatically adds connection URL to Variables

Change in `database.py` to use PostgreSQL URL instead of SQLite.

### Scale to Multiple Instances

For high volume (1000+ leads):
1. In Railway, go to **Settings**
2. Increase **"Replicas"** to 2-3
3. Railway load-balances automatically

---

## Keep It Secure

✅ **Already done:**
- Environment variables (secrets safe)
- HTTPS automatic
- No password in code
- Webhook verification enabled

✅ **Recommended:**
- Change `WHATSAPP_VERIFY_TOKEN` regularly
- Keep access tokens private
- Use Railway's built-in secrets
- Enable 2FA on your accounts

---

## Monitoring & Alerts

Set up alerts (Premium feature):
1. Go to **Settings** → **Alerts**
2. Enable: "Deployment Failed" notifications
3. You'll get email if something breaks

---

## Rollback (Undo Deployment)

If something breaks:

1. In Railway, go to **Deployments**
2. Find the previous working version
3. Click the ⋯ menu → **"Revert to this deployment"**
4. Previous version goes live immediately

✅ **All your leads are safe** - database is kept!

---

## Next: Add More Features

**Optional upgrades:**
- Email confirmations: Add Sendgrid
- Calendar integration: Add Google Calendar API
- CRM connection: Add HubSpot API
- Payment: Add Stripe

See the main README for integration guides.

---

## Success Indicators

✅ You've successfully deployed when:

- [ ] Railway dashboard shows "live" status
- [ ] Health endpoint returns OK
- [ ] WhatsApp messages get instant responses
- [ ] Leads appear in `/api/leads` endpoint
- [ ] Admin commands work (`python utils.py list`)
- [ ] No errors in Railway logs
- [ ] Webhook shows as "verified" in Meta dashboard

---

## Final Checklist Before Going Live

- [ ] Create GitHub account & repo
- [ ] Push code to GitHub
- [ ] Create Railway account
- [ ] Deploy from GitHub
- [ ] Add WhatsApp variables
- [ ] Configure webhook URL
- [ ] Test with WhatsApp message
- [ ] See lead captured in dashboard
- [ ] Check logs are clean
- [ ] Note down Railway URL
- [ ] Celebrate! 🎉

---

## Support

**If something doesn't work:**

1. **Check Railway Logs** - Most clues are there
2. **Check WhatsApp configuration** - Webhook URL matches exactly
3. **Restart deployment** - Click Redeploy
4. **View this guide again** - Troubleshooting section
5. **Contact Railway support** - Very responsive

---

## You're All Set! 🎉

Your chatbot is now:
✅ Running 24/7 on Railway
✅ Receiving real WhatsApp messages
✅ Generating qualified leads
✅ Ready for production
✅ Secure with HTTPS
✅ Scalable for growth

---

## Next Steps

1. **Monitor first few days** - Check logs daily
2. **Listen to leads** - What questions are they asking?
3. **Optimize messages** - Improve responses based on feedback
4. **Add features** - Calendar booking, email confirmations, etc.
5. **Scale up** - Add more instances when traffic grows

---

## Enjoy Your Live Chatbot! 🚀

Your WhatsApp chatbot for Dg Nagpur is now live and working 24/7!

Every message generates a lead. Every lead is qualified automatically.

**Start generating results!** 💼📱

---

**Questions about Railway?** Check [railway.app/docs](https://railway.app/docs)

**WhatsApp issues?** Check [developers.facebook.com/docs/whatsapp](https://developers.facebook.com/docs/whatsapp)

**Chatbot problems?** Check the main [README.md](README.md)

---

*Last updated: February 27, 2026*

*Deploying your DG Nagpur chatbot on Railway = Success! 🎯*
