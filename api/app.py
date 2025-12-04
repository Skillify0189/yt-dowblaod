import yt_dlp
import os
import re
from flask import Flask, render_template, request, send_file, jsonify, abort
from pathlib import Path
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  # 16 GB

# Use /tmp — the only writable directory on Vercel
TMP_DIR = Path("/tmp/downloads")
TMP_DIR.mkdir(exist_ok=True)

def is_valid_youtube_url(url):
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
    return re.match(youtube_regex, url, re.I) is not None

def download_video(url, quality_format):
    try:
        ydl_opts = {
            "format": quality_format,
            "outtmpl": str(TMP_DIR / "%(title)s.%(ext)s"),
            "quiet": True,
            "no_warnings": True,
            "merge_output_format": "mp4",        # avoids needing ffmpeg in most cases
            "socket_timeout": 30,
            "retries": 3,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            filename_only = os.path.basename(filename)

        return {
            "success": True,
            "filename": filename_only,
            "fullpath": filename,                     # we need the full path to serve it
            "message": f"Downloaded: {filename_only}"
        }
    except Exception as e:
        return {
            "success": False,
            "filename": None,
            "fullpath": None,
            "message": f"Error: {str(e)[:150]}"
        }

QUALITY_MAP = { ... }  # ← keep exactly the same as yours

@app.route("/")
def index():
    return render_template("index.html", qualities=QUALITY_MAP)

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url", "").strip()
    quality = request.form.get("quality", "best")

    if not url or not is_valid_youtube_url(url) or quality not in QUALITY_MAP:
        return jsonify({"success": False, "message": "Invalid input"}), 400

    result = download_video(url, QUALITY_MAP[quality]["format"])

    # On Vercel we delete the file right after serving, so return the path now
    if result["success"]:
        return jsonify({
            "success": True,
            "filename": result["filename"],
            "download_url": f"/get/{result['filename']}"
        })
    else:
        return jsonify(result), 500

@app.route("/get/<filename>")
def get_file(filename):
    # Basic security
    if ".." in filename or filename.startswith("/"):
        abort(403)

    file_path = TMP_DIR / filename

    if not file_path.exists():
        abort(404)

    # Stream + delete immediately after (so /tmp never fills up)
    def generate():
        with open(file_path, "rb") as f:
            yield from f
        try:
            os.remove(file_path)   # clean up
        except:
            pass

    return send_file(
        generate(),
        as_attachment=True,
        download_name=filename,
        mimetype="video/mp4"
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

# Remove the if __name__ == "__main__" block completely for Vercel
# (Vercel uses its own handler)
