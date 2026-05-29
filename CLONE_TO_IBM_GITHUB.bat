@echo off
echo ========================================
echo Clone Repository to IBM GitHub Enterprise
echo ========================================
echo.
echo Source: https://github.com/suchitraroutray/smart-task-hub
echo Target: https://github.ibm.com/Suchitra-Routray/ica-bobathon
echo.

REM Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is NOT installed!
    echo.
    echo Please install Git first:
    echo 1. Download from: https://git-scm.com/download/win
    echo 2. Run installer (use default settings)
    echo 3. Restart this script
    echo.
    pause
    exit /b 1
)

echo ✅ Git is installed!
echo.

REM Create temporary directory
set TEMP_DIR=%TEMP%\smart-task-hub-clone
echo Creating temporary directory: %TEMP_DIR%
if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"
mkdir "%TEMP_DIR%"
cd /d "%TEMP_DIR%"
echo.

echo ========================================
echo Step 1: Cloning from GitHub.com
echo ========================================
echo.
echo Cloning: https://github.com/suchitraroutray/smart-task-hub
git clone https://github.com/suchitraroutray/smart-task-hub.git
if errorlevel 1 (
    echo.
    echo ❌ Failed to clone from GitHub.com
    echo.
    pause
    exit /b 1
)
echo.
echo ✅ Cloned successfully!
echo.

cd smart-task-hub

echo ========================================
echo Step 2: Removing old remote
echo ========================================
echo.
git remote remove origin
echo ✅ Old remote removed
echo.

echo ========================================
echo Step 3: Adding IBM GitHub remote
echo ========================================
echo.
echo Adding: https://github.ibm.com/Suchitra-Routray/ica-bobathon.git
git remote add origin https://github.ibm.com/Suchitra-Routray/ica-bobathon.git
echo ✅ IBM GitHub remote added
echo.

echo ========================================
echo Step 4: Pushing to IBM GitHub
echo ========================================
echo.
echo You will be prompted for IBM GitHub credentials
echo Username: Your IBM email (e.g., suchitra.routray@ibm.com)
echo Password: Your IBM GitHub personal access token
echo.
pause

git push -u origin main
if errorlevel 1 (
    echo.
    echo ⚠️  Push failed. Trying 'master' branch instead...
    git push -u origin master
    if errorlevel 1 (
        echo.
        echo ❌ Failed to push to IBM GitHub
        echo.
        echo Possible issues:
        echo 1. Repository doesn't exist on IBM GitHub
        echo 2. Wrong credentials
        echo 3. No permission to push
        echo.
        echo Please:
        echo 1. Create repository on IBM GitHub first
        echo 2. Make sure you have push access
        echo 3. Use correct credentials
        echo.
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo ✅ SUCCESS!
echo ========================================
echo.
echo Repository cloned to IBM GitHub:
echo https://github.ibm.com/Suchitra-Routray/ica-bobathon
echo.
echo Cleaning up temporary directory...
cd /d %TEMP%
rmdir /s /q "%TEMP_DIR%"
echo.
echo ✅ All done!
echo.
pause

@REM Made with Bob
