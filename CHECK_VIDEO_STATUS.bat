@echo off
echo ========================================
echo Smart Task Hub - Video Status Checker
echo ========================================
echo.

set VIDEO_FILE=SmartTaskHub_Demo.mp4

if exist "%VIDEO_FILE%" (
    echo ✅ VIDEO FOUND!
    echo ========================================
    echo.
    echo File: %VIDEO_FILE%
    echo Location: %CD%\%VIDEO_FILE%
    echo.
    
    for %%A in ("%VIDEO_FILE%") do (
        echo File Size: %%~zA bytes
        echo Created: %%~tA
    )
    
    echo.
    echo ========================================
    echo Status: READY TO USE
    echo ========================================
    echo.
    echo What you can do:
    echo 1. Double-click the video to watch it
    echo 2. Share it via email or cloud storage
    echo 3. Upload to SharePoint/Teams
    echo.
    echo Opening video location...
    explorer /select,"%CD%\%VIDEO_FILE%"
    
) else (
    echo ❌ VIDEO NOT FOUND
    echo ========================================
    echo.
    echo The video file does not exist yet.
    echo You need to create it first!
    echo.
    echo ========================================
    echo HOW TO CREATE THE VIDEO:
    echo ========================================
    echo.
    echo Option 1: AUTOMATED (Recommended)
    echo    1. Double-click: CREATE_VIDEO.bat
    echo    2. Wait 5-10 minutes
    echo    3. Video will be created automatically
    echo.
    echo Option 2: MANUAL RECORDING
    echo    1. Open: RECORD_VIDEO_GUIDE.md
    echo    2. Follow the 5-step guide
    echo    3. Record using Windows Game Bar
    echo.
    echo ========================================
    echo.
    echo Current location: %CD%
    echo Looking for: %VIDEO_FILE%
    echo.
    echo Would you like to create the video now?
    echo.
    set /p CREATE="Type 'yes' to create video automatically: "
    
    if /i "%CREATE%"=="yes" (
        echo.
        echo Starting video creation...
        echo.
        call CREATE_VIDEO.bat
    ) else (
        echo.
        echo No problem! Create the video when you're ready.
        echo Just double-click: CREATE_VIDEO.bat
        echo.
    )
)

echo.
pause

@REM Made with Bob
