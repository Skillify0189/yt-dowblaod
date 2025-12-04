import yt_dlp
import os
import re
from flask import Flask, render_template, request, send_file, jsonify
from pathlib import Path

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  # 16GB max file size

# Directories
BASE_DIR = Path(__file__).parent
DOWNLOADS_DIR = BASE_DIR / "downloads"
DOWNLOADS_DIR.mkdir(exist_ok=True)


def is_valid_youtube_url(url):
    """
    Basic validation to check if URL looks like a YouTube link.
    Accepts: youtube.com, youtu.be, youtube-nocookie.com variations
    """
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
    return re.match(youtube_regex, url) is not None


def download_video(url, quality_format):
    """
    Download video from YouTube URL and return metadata about the download.
    Adapted for web context - returns dict with status and file info instead of printing.
    
    Args:
        url: YouTube URL
        quality_format: Format string (best, bestaudio/best, best[height<=360], etc.)
    
    Returns:
        dict with keys: success (bool), filename (str), message (str)
    """
    try:
        # Prepare yt-dlp options
        ydl_opts = {
            "format": quality_format,
            "outtmpl": str(DOWNLOADS_DIR / "%(title)s.%(ext)s"),
            "quiet": False,
            "no_warnings": False,
            "socket_timeout": 30,
        }

        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            filename_only = os.path.basename(filename)
            
        return {
            "success": True,
            "filename": filename_only,
            "message": f"✅ File downloaded successfully: {filename_only}"
        }

    except yt_dlp.utils.DownloadError as e:
        return {
            "success": False,
            "filename": None,
            "message": f"❌ Download error: Invalid URL or video not available. ({str(e)[:100]})"
        }
    except Exception as e:
        return {
            "success": False,
            "filename": None,
            "message": f"❌ An error occurred: {str(e)[:150]}"
        }


# Quality format mapping (same as CLI version)
QUALITY_MAP = {
    "best": {
        "label": "Best Quality (Video + Audio)",
        "format": "best"
    },
    "audio": {
        "label": "Audio Only (.mp3)",
        "format": "bestaudio/best"
    },
    "360p": {
        "label": "360p",
        "format": "best[height<=360]"
    },
    "480p": {
        "label": "480p",
        "format": "best[height<=480]"
    },
    "720p": {
        "label": "720p",
        "format": "best[height<=720]"
    },
    "1080p": {
        "label": "1080p",
        "format": "best[height<=1080]"
    },
}


@app.route("/")
def index():
    """Render the main download page."""
    return render_template("index.html", qualities=QUALITY_MAP)


@app.route("/download", methods=["POST"])
def download():
    """
    Handle download request from the form.
    Expects: url (str), quality (str)
    Returns: JSON with download status and result
    """
    url = request.form.get("url", "").strip()
    quality = request.form.get("quality", "best")

    # Validate input
    if not url:
        return jsonify({
            "success": False,
            "message": "❌ Please enter a YouTube URL."
        }), 400

    if not is_valid_youtube_url(url):
        return jsonify({
            "success": False,
            "message": "❌ Please enter a valid YouTube URL."
        }), 400

    if quality not in QUALITY_MAP:
        return jsonify({
            "success": False,
            "message": "❌ Invalid quality selection."
        }), 400

    # Perform download
    quality_format = QUALITY_MAP[quality]["format"]
    result = download_video(url, quality_format)

    return jsonify(result)


@app.route("/download-file/<filename>")
def download_file(filename):
    """
    Serve the downloaded file for browser download with 'Save As' dialog.
    Security: Only allow filenames from the downloads folder to prevent directory traversal.
    """
    # Security check: ensure filename doesn't contain path traversal attempts
    if "/" in filename or "\\" in filename or filename.startswith("."):
        return "Invalid filename", 403

    file_path = DOWNLOADS_DIR / filename

    # Security check: ensure file exists in downloads folder
    if not file_path.exists() or not file_path.is_file():
        return "File not found", 404

    try:
        return send_file(
            str(file_path),
            as_attachment=True,
            download_name=filename,
            mimetype='application/octet-stream'
        )
    except Exception as e:
        return f"Error downloading file: {str(e)}", 500


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True, host="127.0.0.1", port=5000)
