# 🔧 Fix WhatsApp Webhook Verification Error

## Error Details
```
The callback URL or verify token couldn't be validated. 
Please verify the provided information or try again later.
(#N/A:WBxP-1185920206-751885558)
```

This means Meta can't reach your webhook or the token doesn't match.

---

## ✅ Step-by-Step Fix

### Check #1: Is Your Server Running?

**If using Railway:**
```
1. Go to railway.app
2. Click your project
3. Check Deployments tab
4. Status should say "Live" (green checkmark)
```

**If running locally with ngrok:**
```powershell
# Open PowerShell and run:
python app.py

# You should see:
# Starting DG Nagpur WhatsApp Chatbot on port 5000
# * Running on http://127.0.0.1:5000
```

❌ **If not running:** Start your server first!

---

### Check #2: Verify Token Matches EXACTLY

**In Meta Dashboard:**
1. Go to WhatsApp → Configuration
2. Find the "Verify Token" field
3. Copy the value exactly (including capitalization, spaces, everything)

**In Railway Variables (or .env):**
1. Go to Variables tab
2. Find `WHATSAPP_VERIFY_TOKEN`
3. Make sure it matches EXACTLY

⚠️ **Common mistakes:**
- Extra spaces before/after
- Different capitalization (Test vs test vs TEST)
- Accidental characters like dashes or underscores
- Copied wrong token

**Solution: Copy-paste from Railway to Meta to ensure exact match**

---

### Check #3: Test the URL

**If using Railway:**

Open this in your browser (replace YOUR-URL):
```
https://YOUR-RAILWAY-URL/health
```

You should see:
```json
{"status": "healthy", "timestamp": "...", "service": "DG Nagpur WhatsApp Chatbot"}
```

❌ **If you get an error or blank page:**
- URL is wrong
- Server is down
- Railway deployment failed

---

### Check #4: Manual Webhook Test

**If using ngrok (local testing):**

1. Make sure ngrok is running:
```powershell
ngrok http 5000
```
You'll see: `Forwarding https://xxxx-xx-xxx-xxx.ngrok.io -> http://localhost:5000`

2. Test the webhook manually:
```powershell
$url = "https://xxxx-xx-xxx-xxx.ngrok.io/webhook?hub.verify_token=YOUR_TOKEN&hub.challenge=test_challenge_123"
$response = Invoke-WebRequest -Uri $url
$response.Content
```

You should see: `test_challenge_123`

If you don't see this, there's an issue with your app.

---

### Check #5: Verify Token Format in Code

Open: `app.py`

Find this line (around line 30):
```python
VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "your_verify_token")
```

If you see the default value `"your_verify_token"`, that's the problem!

**Solution:**
1. Go to Railway Variables (or .env file)
2. Add: `WHATSAPP_VERIFY_TOKEN=your_random_token_here`
3. Restart the server
4. Use that same token in Meta Dashboard

---

### Check #6: Common URL Issues

**Using Railway:**
```
❌ WRONG: https://dg-nagpur-whatsapp-bot.railway.app/webhook
           (missing -production)

✅ CORRECT: https://dg-nagpur-whatsapp-bot-production.up.railway.app/webhook
```

**Using Ngrok:**
```
❌ WRONG: https://xxxx-xx-xxx-xxx.ngrok.io  (without /webhook)

✅ CORRECT: https://xxxx-xx-xxx-xxx.ngrok.io/webhook
```

**Check:**
- URL starts with `https://` (not http://)
- URL ends with `/webhook`
- URL has no trailing spaces
- URL is complete and correct

---

## The Complete Fix Checklist

### Step 1: Configure Railway Variables
```
Go to railway.app → Your Project → Variables tab
Add these EXACTLY:

WHATSAPP_VERIFY_TOKEN = create_random_string_like_abc123xyz

WHATSAPP_ACCESS_TOKEN = your_actual_whatsapp_token_from_meta

WHATSAPP_PHONE_NUMBER_ID = your_phone_id

WHATSAPP_BUSINESS_ACCOUNT_ID = your_business_id

DEBUG = False
```

### Step 2: Check Server Status
```
Go to railway.app → Deployments tab
Status should be: "Live" (green)

If not: Click "Redeploy" button
```

### Step 3: Copy Railway URL
```
railway.app → Deployments tab

Copy the public URL
Should look like: https://dg-nagpur-whatsapp-bot-production.up.railway.app
```

### Step 4: Go to Meta Dashboard
```
developers.facebook.com
Your App → WhatsApp → Configuration

Webhook URL: https://YOUR-RAILWAY-URL/webhook
            (Don't forget /webhook at the end!)

Verify Token: create_random_string_like_abc123xyz
             (Must match Railway variable exactly!)
```

### Step 5: Click "Verify and Save"

**Wait:** Should say ✅ "Webhook verified"

---

## If Still Not Working

### Debug #1: Check Railway Logs

1. Go to railway.app
2. Go to your project
3. Click **"Logs"** tab
4. Look for any error messages

Send screenshot of logs and I can help!

### Debug #2: Check App is Running

```powershell
# Test the health endpoint
$url = "https://YOUR-RAILWAY-URL/health"
$response = Invoke-WebRequest -Uri $url
$response.Content

# Should return JSON like:
# {"status": "healthy", "timestamp": "2026-02-27T...", "service": "DG Nagpur WhatsApp Chatbot"}
```

### Debug #3: Test with Ngrok Locally

If Railway isn't working, test locally with ngrok:

```powershell
# Terminal 1: Start your app
python app.py

# Terminal 2: Start ngrok (new terminal)
ngrok http 5000
```

Then in Meta:
- Webhook URL: `https://xxxx-xx-xxx-xxx.ngrok.io/webhook`
- Verify Token: `test_token_123`
- Click Verify and Save

If this works locally, Railway URL is wrong or server is down.

---

## Most Common Causes & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| Timeout | Server not running | Start `python app.py` or check Railway Deployments |
| URL wrong | Typo in webhook URL | Copy-paste from Railway exactly |
| Token wrong | Token doesn't match | Make sure Railway variable matches Meta field |
| 403 error | Access denied | Check WHATSAPP_ACCESS_TOKEN is correct |
| Missing /webhook | URL incomplete | Add `/webhook` to end of URL |

---

## Step-by-Step from Scratch

**If everything fails, start fresh:**

### 1. Delete Old Webhook Configuration
- In Meta Dashboard → WhatsApp → Configuration
- Clear the Webhook URL field
- Clear the Verify Token field
- Click "Save" (if button available)

### 2. In Railway, Update Variables
```
WHATSAPP_VERIFY_TOKEN = my_secure_token_2026_feb27

WHATSAPP_ACCESS_TOKEN = [your actual token]

WHATSAPP_PHONE_NUMBER_ID = [your actual ID]

WHATSAPP_BUSINESS_ACCOUNT_ID = [your actual ID]

DEBUG = False
```

Click "Save" for each

### 3. Redeploy on Railway
- Go to Deployments tab
- Click the ⋯ menu on latest deployment
- Click "Redeploy"
- Wait for "Live" status

### 4. Test Health Endpoint
```powershell
$url = "https://YOUR-RAILWAY-URL/health"
Invoke-WebRequest -Uri $url
# Should see status: healthy
```

### 5. Configure Webhook Again
- Webhook URL: `https://YOUR-RAILWAY-URL/webhook`
- Verify Token: `my_secure_token_2026_feb27`
- Click "Verify and Save"

### 6. Subscribe to Events
- Select: messages, message_status
- Click "Save"

✅ Should work now!

---

## Verify Success

After webhook is verified, you should see:
- ✅ "Webhook verified" message in Meta
- ✅ Green checkmarks next to subscribed events
- ✅ Status shows "Active"

Then send a test message:
1. Open WhatsApp
2. Message your bot number
3. Should get instant response

If you get response = ✅ **Everything is working!**

---

## Alternative Solutions

### Solution A: Use Ngrok for Local Testing
```powershell
# Install ngrok (if not done)
winget install ngrok

# Start ngrok
ngrok http 5000

# In another terminal
python app.py

# Use ngrok URL in Meta (temporary, for testing only)
```

### Solution B: Restart Railway App
1. Go to Railway dashboard
2. Deployments tab
3. Click ⋯ menu
4. Click "Restart"
5. Wait for "Live" status
6. Try webhook verification again

### Solution C: Check Access Token
Make sure your WhatsApp access token is correct:
1. Go to Meta Developer Dashboard
2. WhatsApp → API Setup
3. Generate new token if needed
4. Copy and add to Railway Variables
5. Redeploy

---

## Real Example

**What should work:**

Meta Dashboard:
```
Webhook URL: https://dg-nagpur-whatsapp-bot-production.up.railway.app/webhook
Verify Token: abc123xyz789_secure_token
```

Railway Variables:
```
WHATSAPP_VERIFY_TOKEN = abc123xyz789_secure_token
WHATSAPP_ACCESS_TOKEN = EAAxxxxyyyyzzzzz...
WHATSAPP_PHONE_NUMBER_ID = 1234567890123456
WHATSAPP_BUSINESS_ACCOUNT_ID = 9876543210987654
DEBUG = False
```

**Result:** ✅ "Webhook verified successfully"

---

## Still Stuck?

Provide these details and I'll help:

1. Is your server on Railway or local?
2. What's the exact error number? (WBxP-xxxx)
3. Can you access `https://YOUR-URL/health` in browser?
4. What's in Railway logs? (See Logs tab)
5. Does `WHATSAPP_VERIFY_TOKEN` exactly match Meta Verify Token?

---

## Next: After Webhook Verified

Once webhook is verified:
1. Send WhatsApp message to your bot
2. Should get instant response
3. Lead captured automatically
4. Check leads: `python utils.py list` or via API

---

**Common Next Step:** After webhook works, test with 👇

```powershell
# Send test message to your bot
# Check response
# View in database:
python utils.py list
```

---

**You'll get it!** Most commonly it's just a typo in the token or URL. 💪

Let me know the exact issue and we'll fix it fast! 🚀
