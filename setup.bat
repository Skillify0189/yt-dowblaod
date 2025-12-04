@echo off
REM YouTube Downloader - Installation Script for Windows
REM This script automates the setup process

setlocal enabledelayedexpansion

echo.
echo ======================================
echo YouTube Downloader - Setup Script
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python is installed: 
python --version
echo.

REM Check if we're in the right directory
if not exist "app.py" (
    echo ERROR: app.py not found!
    echo Please run this script from the project root directory.
    pause
    exit /b 1
)

echo [OK] Found app.py - project directory correct
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

if not exist "venv" (
    echo ERROR: Failed to create virtual environment!
    pause
    exit /b 1
)

echo [OK] Virtual environment created
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo [OK] Virtual environment activated
echo.

REM Install requirements
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)

echo [OK] Dependencies installed successfully
echo.

REM Display Python version in venv
echo Verifying installation...
python --version
pip list | findstr /I "Flask yt-dlp Werkzeug" >nul

echo.
echo ======================================
echo SETUP COMPLETE!
echo ======================================
echo.
echo To start the application, run:
echo   python app.py
echo.
echo Then open your browser to:
echo   http://127.0.0.1:5000
echo.
echo Press any key to continue...
pause
