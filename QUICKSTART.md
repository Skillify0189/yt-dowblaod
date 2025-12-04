# QUICK START GUIDE

## 30-Second Setup

### 1. Open PowerShell in the project directory
```powershell
cd "c:\Users\hi\Documents\py\webapps\yt video downloader"
```

### 2. Create & Activate Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Run the App
```powershell
python app.py
```

### 5. Open in Browser
Navigate to: **http://127.0.0.1:5000**

---

## What You Get

✅ **Main Features:**
- Modern, responsive web interface
- Download YouTube videos in multiple qualities
- Extract audio as MP3
- Browser "Save As" dialog for downloads
- Real-time status feedback
- Mobile-friendly design

✅ **Quality Options:**
- Best Quality (video + audio)
- Audio Only (mp3)
- 360p, 480p, 720p, 1080p

---

## Project Files

```
📁 yt video downloader/
├── 📄 app.py              ← Main Flask application
├── 📄 requirements.txt    ← Dependencies (Flask, yt-dlp)
├── 📄 README.md           ← Full documentation
├── 📄 QUICKSTART.md       ← This file
│
├── 📁 templates/
│   ├── base.html          ← Base layout with navbar
│   ├── index.html         ← Main form page
│   └── result.html        ← Result page template
│
├── 📁 static/css/
│   └── style.css          ← Custom responsive styling
│
└── 📁 downloads/          ← Downloaded files go here
```

---

## Troubleshooting

**PowerShell execution policy error?**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Port 5000 already in use?**
Edit `app.py` line 135:
```python
app.run(debug=True, host="127.0.0.1", port=5001)  # Use 5001 instead
```

**Module not found?**
Verify virtual environment is activated:
```powershell
# Should show (venv) prefix in terminal
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Next Steps

1. ✅ Open http://127.0.0.1:5000
2. ✅ Paste a YouTube URL
3. ✅ Select quality
4. ✅ Click Download
5. ✅ Save file to your device

**That's it! You're ready to download.** 🎥

