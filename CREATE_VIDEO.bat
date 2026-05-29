@echo off
echo ========================================
echo Smart Task Hub - Video Creator
echo ========================================
echo.
echo This script will automatically create a demo video with:
echo - Professional slides
echo - Text-to-speech narration
echo - 11 slides covering all features
echo - Duration: ~90 seconds (1.5 minutes)
echo.
echo Requirements:
echo - Python 3.8 or higher
echo - Internet connection (for text-to-speech)
echo - 500MB free disk space
echo.
echo Time needed: 5-10 minutes
echo.
echo ⏰ NOTIFICATION: You will be notified when complete!
echo    - Sound alert
echo    - Popup message
echo    - File explorer opens
echo.
pause

echo.
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python found!
echo.
echo Installing required packages...
echo This may take 2-3 minutes on first run...
echo.

pip install moviepy Pillow gTTS --quiet

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install packages
    echo.
    echo Please try running as Administrator:
    echo 1. Right-click CREATE_VIDEO.bat
    echo 2. Select "Run as administrator"
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Starting video creation...
echo ========================================
echo.
echo ⏰ Started at: %TIME%
echo.
echo Please wait 5-10 minutes...
echo The script will show progress for each slide.
echo.
echo 💡 TIP: You can minimize this window and do other work.
echo        You'll get a notification when it's done!
echo.

python create_demo_video.py

if errorlevel 1 (
    echo.
    echo ========================================
    echo ERROR: Video creation failed
    echo ========================================
    echo.
    echo Possible solutions:
    echo 1. Check your internet connection
    echo 2. Make sure you have 500MB free disk space
    echo 3. Try running as Administrator
    echo 4. Check if ffmpeg is installed
    echo.
    REM Play error sound
    powershell -c (New-Object Media.SoundPlayer "C:\Windows\Media\Windows Critical Stop.wav").PlaySync();
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ SUCCESS! Video created!
echo ========================================
echo.
echo ⏰ Completed at: %TIME%
echo.
echo Video file: SmartTaskHub_Demo.mp4
echo Location: %CD%\SmartTaskHub_Demo.mp4
echo.
echo Next steps:
echo 1. Watch the video to review
echo 2. Share with colleagues
echo 3. Upload to SharePoint/Teams
echo.

REM Play success sound (3 beeps)
echo 🔔 Playing notification sound...
powershell -c (New-Object Media.SoundPlayer "C:\Windows\Media\Windows Notify System Generic.wav").PlaySync();
timeout /t 1 /nobreak >nul
powershell -c (New-Object Media.SoundPlayer "C:\Windows\Media\Windows Notify System Generic.wav").PlaySync();
timeout /t 1 /nobreak >nul
powershell -c (New-Object Media.SoundPlayer "C:\Windows\Media\Windows Notify System Generic.wav").PlaySync();

REM Show popup notification
echo.
echo 📢 Showing popup notification...
powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; $notify = New-Object System.Windows.Forms.NotifyIcon; $notify.Icon = [System.Drawing.SystemIcons]::Information; $notify.Visible = $true; $notify.ShowBalloonTip(10000, 'Video Ready!', 'SmartTaskHub_Demo.mp4 has been created successfully!', [System.Windows.Forms.ToolTipIcon]::Info)}"

REM Open file location
echo.
echo 📂 Opening video location...
explorer /select,"%CD%\SmartTaskHub_Demo.mp4"

echo.
echo ========================================
echo 🎉 ALL DONE! Your video is ready!
echo ========================================
echo.
pause

@REM Made with Bob
