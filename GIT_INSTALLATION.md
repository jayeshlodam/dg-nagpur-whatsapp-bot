# 🔧 Install Git on Windows - Step by Step

## Option 1: Install Git (Recommended - 5 minutes)

### Step 1: Download Git
1. Go to **[git-scm.com](https://git-scm.com/)**
2. Click **"Download for Windows"** (blue button)
3. The `.exe` file will download automatically

### Step 2: Run the Installer
1. Find the downloaded file (usually in Downloads folder)
   - Look for: `Git-2.x.x-64-bit.exe`
2. Double-click it
3. Click **"Yes"** when asked for permission

### Step 3: Installation Setup Wizard
Go through these prompts (defaults are fine):

1. **Select Components** → Click **"Next"**
   - (Keep defaults checked)

2. **Choose Default Editor** → Click **"Next"**
   - (Vim is fine, or choose Notepad)

3. **Name your initial branch** → Click **"Next"**
   - (Select "main" if option available)

4. **Adjust PATH** → Click **"Next"**
   - Important! Select: **"Git from the command line and also from 3rd-party software"**

5. **HTTPS library** → Click **"Next"**

6. **Line ending** → Click **"Next"**
   - Select: **"Checkout Windows-style, commit Unix-style"**

7. **Terminal emulator** → Click **"Next"**

8. **Git pull behavior** → Click **"Next"**

9. **Credential helper** → Click **"Next"**

10. **Extra options** → Click **"Install"**
    - Keep defaults (file caching, git credential manager)

### Step 4: Finish Installation
- Uncheck "View Release Notes"
- Click **"Finish"**

✅ **Git is now installed!**

---

## Step 5: Verify Installation

**Open a new PowerShell terminal:**
1. Press `Windows Key + X`
2. Select **"Windows PowerShell"** or **"Terminal"**
3. Type:
```powershell
git --version
```

**You should see:**
```
git version 2.x.x (or similar)
```

✅ **If you see this, Git is working!**

---

## Now You Can Deploy!

Go back to your terminal and run:

```powershell
cd "c:\Users\manish\.vscode\dg nagpur whatsapp bot"

git init

git config user.name "Your Name"

git config user.email "your@email.com"

git add .

git commit -m "Initial commit: DG Nagpur WhatsApp Bot"

git remote add origin https://github.com/YOUR-USERNAME/dg-nagpur-whatsapp-bot.git

git branch -M main

git push -u origin main
```

---

## Option 2: Quick Install via PowerShell (Alternative)

If you have admin access, you can use Winget:

```powershell
# Run PowerShell as Administrator, then:
winget install Git.Git
```

Then restart PowerShell and verify:
```powershell
git --version
```

---

## Troubleshooting

### "git: The term 'git' is not recognized" (after install)

**Solution:**
1. Close PowerShell completely
2. Open **New** PowerShell window
3. Git should work now

If still doesn't work:
```powershell
# Check if git is in PATH
$env:Path -split ";"
# Look for a line with "Git\cmd"
```

### Git installed but PATH not set

**Solution:**
1. Press `Windows Key`, search for **"Environment Variables"**
2. Click **"Edit the system environment variables"**
3. Click **"Environment Variables..."** button
4. Under "User variables", click **"New..."**
5. Variable name: `PATH`
   Variable value: `C:\Program Files\Git\cmd`
6. Click **"OK"** multiple times
7. Restart PowerShell

---

## Verify Git Setup

After installing, verify:

```powershell
# Check git version
git --version

# Check git config
git config --list

# Should show your name and email
```

---

## You're Ready!

Once you see `git version 2.x.x`, you can:

```powershell
cd "c:\Users\manish\.vscode\dg nagpur whatsapp bot"
git init
```

And continue with the Railway deployment steps! 🚀

---

## Need Help?

If you still get errors:
1. Restart your computer
2. Open PowerShell again
3. Try `git --version`

If it still doesn't work, you might need to:
- Uninstall Git
- Delete the Git folder: `C:\Program Files\Git`
- Restart computer
- Reinstall using the steps above

---

**Done installing?** Let me know and we'll continue with deployment! 👍
