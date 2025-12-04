# YouTube Downloader - Installation Script for Windows PowerShell
# Run from project root directory

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "YouTube Downloader - Setup Script" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "[OK] Python is installed: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python is not installed or not in PATH!" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Check if we're in the right directory
if (-not (Test-Path "app.py")) {
    Write-Host "[ERROR] app.py not found!" -ForegroundColor Red
    Write-Host "Please run this script from the project root directory." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Found app.py - project directory correct" -ForegroundColor Green
Write-Host ""

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

if (-not (Test-Path "venv")) {
    Write-Host "[ERROR] Failed to create virtual environment!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Virtual environment created" -ForegroundColor Green
Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
Write-Host ""

# Install requirements
Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to install dependencies!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Dependencies installed successfully" -ForegroundColor Green
Write-Host ""

# Verify installation
Write-Host "Verifying installation..." -ForegroundColor Yellow
python --version
pip list | Select-String -Pattern "Flask", "yt-dlp", "Werkzeug"

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "SETUP COMPLETE!" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start the application, run:" -ForegroundColor Yellow
Write-Host "  python app.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "Then open your browser to:" -ForegroundColor Yellow
Write-Host "  http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Enter to exit..." -ForegroundColor Gray
Read-Host
