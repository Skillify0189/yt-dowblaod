# 🎥 YouTube Video & Audio Downloader

A modern, responsive Flask web application for downloading YouTube videos and audio in multiple quality formats.

## Features

✨ **Core Features:**
- 🎬 Download full videos in best quality
- 🎵 Extract audio as MP3 (bestaudio format)
- 📺 Multiple quality options: 360p, 480p, 720p, 1080p
- 📱 Fully responsive design (mobile, tablet, desktop)
- ⚡ Fast and intuitive user interface
- 💾 Browser "Save As" dialog for file downloads
- ✅ Input validation and error handling
- 🔒 Security features (path traversal prevention)

## Project Structure

```
yt video downloader/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore file
├── README.md                       # This file
│
├── templates/                      # Jinja2 templates
│   ├── base.html                   # Base template with navbar & footer
│   ├── index.html                  # Main download form page
│   └── result.html                 # Result page (reference)
│
├── static/                         # Static files
│   └── css/
│       └── style.css               # Custom responsive CSS
│
└── downloads/                      # Downloaded files (auto-created)
```

## Prerequisites

- **Python 3.8+** (recommended: Python 3.10+)
- **pip** (Python package manager)

## Installation

### Step 1: Clone or Extract the Project

```bash
cd "c:\Users\hi\Documents\py\webapps\yt video downloader"
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# On Windows Command Prompt
python -m venv venv
venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Flask 3.0.0** - Web framework
- **yt-dlp 2024.12.2** - YouTube downloader library
- **Werkzeug 3.0.1** - WSGI utilities

## Running the Application

### Start the Flask Development Server

```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
 * Restarting with reloader
```

### Access the Application

Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

1. **Enter a YouTube URL** in the input field
   - Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

2. **Select a Quality Option:**
   - Best Quality (Video + Audio) - Full video with sound
   - Audio Only (.mp3) - Extract just the audio
   - 360p, 480p, 720p, 1080p - Specific video qualities

3. **Click "Download"**
   - The app will process the request
   - You'll see a downloading message

4. **Save the File**
   - Browser will show "Save As" dialog
   - Choose your preferred location
   - File will be downloaded with original YouTube title

## Supported YouTube URL Formats

All of these URL formats are supported:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://www.youtube-nocookie.com/...`

## Quality Formats Explained

| Format | Description | Use Case |
|--------|-------------|----------|
| **Best Quality** | Video + Audio combined, best quality available | Full videos with sound |
| **Audio Only** | Extracts audio as .mp3 format | Music extraction, podcasts |
| **360p** | Video at 360p resolution | Low bandwidth, smaller file |
| **480p** | Video at 480p resolution | Mobile viewing |
| **720p** | Video at 720p resolution | Standard HD |
| **1080p** | Video at 1080p resolution | Full HD quality |

## Troubleshooting

### Issue: "Invalid YouTube URL"
**Solution:** Make sure the URL is complete and from YouTube:
- ✅ Correct: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- ❌ Incorrect: `youtube.com` or just the video ID

### Issue: "Download failed"
**Possible causes:**
- Video is age-restricted or unavailable in your region
- Video has been deleted or made private
- Network connectivity issue - try again
- Content ID claim that prevents downloading

### Issue: Port 5000 already in use
**Solution:** Either:
1. Stop other applications using port 5000
2. Or modify the port in `app.py` line 135:
   ```python
   app.run(debug=True, host="127.0.0.1", port=5001)  # Change to 5001
   ```

### Issue: Module not found (ImportError)
**Solution:** Make sure virtual environment is activated:
```bash
# PowerShell
.\venv\Scripts\Activate.ps1

# Command Prompt
venv\Scripts\activate.bat
```

Then reinstall packages:
```bash
pip install -r requirements.txt
```

## Development

### Adding New Features

To extend the app:

1. **Add new routes** in `app.py`
2. **Create new templates** in `templates/`
3. **Style with CSS** in `static/css/style.css`
4. **Test thoroughly** with different URLs

### Common Customizations

**Change the title:**
Edit the navbar brand text in `templates/base.html` line 21

**Change colors:**
Edit CSS variables in `static/css/style.css` lines 7-13

**Add more quality options:**
Edit `QUALITY_MAP` in `app.py` around line 78

## Security Notes

✅ **Implemented Security Features:**
- Input validation for YouTube URLs
- Path traversal prevention in file serving
- File extension and location validation
- No user code execution
- Safe download serving with proper mime types

⚠️ **Legal Considerations:**
- Respect YouTube's Terms of Service
- Only download content you have permission to download
- Respect copyright and creator rights
- This tool is for personal, non-commercial use

## Performance Tips

- **First download may be slow** while yt-dlp downloads the video
- **Larger qualities take longer** - 1080p videos require more processing
- **Audio extraction is faster** than video downloads
- Keep your internet connection stable during downloads

## Browser Compatibility

- ✅ Chrome/Chromium 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## API Endpoints

### GET `/`
Returns the main download page (HTML form)

### POST `/download`
**Request:** Form data with `url` and `quality`
**Response:** JSON
```json
{
  "success": true,
  "filename": "video_title.mp4",
  "message": "✅ File downloaded successfully: video_title.mp4"
}
```

### GET `/download-file/<filename>`
Serves the file for download with "Save As" dialog

### GET `/health`
Health check endpoint, returns `{"status": "ok"}`

## Storage

Downloaded files are stored in the `downloads/` folder at the project root. You can:
- Access files directly from the file system
- Delete old downloads manually
- Organize by moving to other folders

## Dependencies

All dependencies are pinned to specific versions for stability:

```
Flask==3.0.0              # Web framework
yt-dlp==2024.12.2         # YouTube downloader (maintained fork of youtube-dl)
Werkzeug==3.0.1           # WSGI utilities
```

## Updates

To update dependencies to latest versions:
```bash
pip install --upgrade -r requirements.txt
```

## Stopping the Server

Press `CTRL+C` in the terminal where Flask is running.

## Future Enhancements

Possible future features:
- [ ] Real-time download progress visualization
- [ ] Download queue management
- [ ] Playlist support
- [ ] Auto-conversion to other formats
- [ ] Download history
- [ ] Batch downloads
- [ ] WebSocket-based real-time updates

## License

This project is provided as-is for educational and personal use.

## Support

For issues with:
- **Flask:** https://flask.palletsprojects.com/
- **yt-dlp:** https://github.com/yt-dlp/yt-dlp
- **This app:** Check the troubleshooting section above

## Credits

- **Flask** - Lightweight Python web framework
- **yt-dlp** - Active YouTube downloader library
- **Bootstrap** - Responsive CSS framework

---

**Happy downloading! 🎥**
