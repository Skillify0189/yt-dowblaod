# 🚀 COMPLETE INSTALLATION & STARTUP GUIDE

## ⚡ FASTEST WAY TO START (PowerShell)

### Option 1: Automated Setup Script (Recommended)

```powershell
# Navigate to project directory
cd "c:\Users\hi\Documents\py\webapps\yt video downloader"

# Run setup script
.\setup.ps1
```

The script will automatically:
1. ✅ Create virtual environment
2. ✅ Activate it
3. ✅ Install all dependencies
4. ✅ Verify installation

Then simply run:
```powershell
python app.py
```

---

## 📋 MANUAL INSTALLATION (Step-by-Step)

### Step 1: Open PowerShell Terminal

```powershell
# Navigate to project
cd "c:\Users\hi\Documents\py\webapps\yt video downloader"
```

### Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

This creates a `venv/` folder with isolated Python environment.

### Step 3: Activate Virtual Environment

```powershell
# On PowerShell
.\venv\Scripts\Activate.ps1

# You should see (venv) prefix in your terminal
```

**If you get execution policy error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again.

### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

Expected output:
```
Successfully installed Flask-3.0.0 yt-dlp-2024.12.2 Werkzeug-3.0.1
```

### Step 5: Verify Installation

```powershell
pip list
```

Should show:
```
Flask                    3.0.0
yt-dlp                   2024.12.2
Werkzeug                 3.0.1
```

---

## 🎮 RUNNING THE APPLICATION

### Start Flask Server

```powershell
python app.py
```

You should see output like:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Open in Browser

Click this link: **http://127.0.0.1:5000**

Or manually type in address bar:
```
http://127.0.0.1:5000
```

---

## ✅ VERIFICATION CHECKLIST

After starting the app, verify:

- [ ] Webpage loads successfully
- [ ] Title shows "YouTube Video & Audio Downloader"
- [ ] URL input field is visible
- [ ] Quality dropdown shows all 6 options
- [ ] Download button is visible and styled
- [ ] Page is responsive (try browser resize)
- [ ] Mobile view works (press F12, toggle device mode)

---

## 🧪 FIRST TEST DOWNLOAD

### Test with Public YouTube Video

1. Go to: https://www.youtube.com/watch?v=jNQXAC9IVRw
2. Copy the URL
3. Paste in app form
4. Select "Best Quality"
5. Click Download
6. Save file when prompted

**Note:** First download takes 30-60 seconds while yt-dlp processes.

---

## ❌ TROUBLESHOOTING

### Issue: "Python not found"

**Solution:**
```powershell
# Check if Python is installed
python --version

# If not, install from: https://www.python.org/downloads/
```

### Issue: "Execution policy" error when activating venv

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### Issue: "Module not found" or "No module named Flask"

**Solution:**
1. Make sure virtual environment is activated (should see `(venv)` prefix)
2. Reinstall dependencies:
```powershell
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"

**Solution A - Change port in app.py:**
```python
# Line 135 in app.py
app.run(debug=True, host="127.0.0.1", port=5001)  # Changed to 5001
```

Then access: http://127.0.0.1:5001

**Solution B - Find and stop existing process:**
```powershell
# Find process using port 5000
Get-Process | Where-Object {$_.ProcessName -match "python"} | Format-List

# Then stop it
Stop-Process -ProcessName python -Force
```

### Issue: "Download fails with error"

**Check:**
- Is URL correct? (Must be full YouTube URL)
- Is video age-restricted?
- Is video available in your region?
- Try another video to test

---

## 🎯 HOW TO USE THE APP

### Complete User Flow

1. **Open Application**
   - Visit http://127.0.0.1:5000
   - See form with title and instructions

2. **Enter YouTube URL**
   - Paste URL in the "YouTube URL" field
   - Example: `https://www.youtube.com/watch?v=VIDEO_ID`

3. **Select Quality**
   - Click quality dropdown
   - Choose from:
     - ✅ Best Quality (Video + Audio)
     - 🎵 Audio Only (.mp3)
     - 📺 360p, 480p, 720p, 1080p

4. **Click Download**
   - Page shows "Downloading..." message
   - Loading spinner appears
   - Be patient (30-120 seconds depending on size)

5. **Save File**
   - Browser shows "Save As" dialog
   - Choose location on your computer
   - File saves with YouTube video title

---

## 📱 MOBILE & TABLET USAGE

The app is fully responsive!

### On iPhone/iPad:
- Open Safari
- Type: http://YOUR_COMPUTER_IP:5000
- Form adapts to touch screen
- All buttons are touch-friendly

### Find Your Computer's IP:
```powershell
ipconfig

# Look for "IPv4 Address" under your network adapter
# Example: 192.168.1.100
```

Then on mobile:
```
http://192.168.1.100:5000
```

---

## 🛑 STOPPING THE APPLICATION

To stop the Flask server:

Press `CTRL+C` in the terminal where Flask is running.

You'll see:
```
KeyboardInterrupt
* Shutting down Flask development server
```

---

## 🔄 RESTARTING AFTER COMPUTER RESTART

```powershell
# Navigate to project
cd "c:\Users\hi\Documents\py\webapps\yt video downloader"

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the app
python app.py
```

---

## 📁 FILES DOWNLOADED

All downloaded files go to:
```
c:\Users\hi\Documents\py\webapps\yt video downloader\downloads\
```

You can:
- Open this folder in Windows Explorer
- Delete old downloads
- Organize by moving files elsewhere

---

## 📝 CONFIGURATION

### Customize Port
Edit `app.py` line 135:
```python
app.run(debug=True, host="127.0.0.1", port=5001)
```

### Customize Title
Edit `templates/base.html` line 21:
```html
<span class="navbar-brand mb-0 h1">
    YouTube Downloader
</span>
```

### Customize Colors
Edit `static/css/style.css` lines 7-13:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    /* ... more colors ... */
}
```

---

## 🔐 SECURITY NOTES

✅ Safe to use for:
- Personal video downloads
- Music extraction
- Offline viewing

⚠️ Respect:
- YouTube Terms of Service
- Copyright laws
- Creator permissions
- Age-restricted content

---

## 📚 USEFUL COMMANDS

### Deactivate Virtual Environment
```powershell
deactivate
```

### Check Python Packages
```powershell
pip list
```

### Update Packages
```powershell
pip install --upgrade -r requirements.txt
```

### Check Flask Version
```powershell
python -c "import flask; print(flask.__version__)"
```

---

## 🆘 GETTING HELP

### For Flask Issues:
https://flask.palletsprojects.com/

### For yt-dlp Issues:
https://github.com/yt-dlp/yt-dlp

### For This Application:
- Read README.md for detailed docs
- Check PROJECT_SUMMARY.md for overview
- Review code comments in app.py

---

## ✨ ADVANCED OPTIONS

### Run on Different Host
Edit `app.py`:
```python
# Allow access from other computers
app.run(debug=True, host="0.0.0.0", port=5000)
```

### Disable Debug Mode (Production)
Edit `app.py`:
```python
app.run(debug=False, host="127.0.0.1", port=5000)
```

### Use Production Server (Gunicorn)
```powershell
pip install gunicorn
gunicorn --bind 127.0.0.1:5000 app:app
```

---

## 🎉 YOU'RE READY!

Your YouTube Downloader is now fully set up and ready to use.

**Next Step:** Start the app with `python app.py` and enjoy!

---

**Happy Downloading! 🎥**
