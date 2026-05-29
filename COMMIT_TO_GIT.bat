@echo off
echo ========================================
echo Smart Task Hub - Git Commit Helper
echo ========================================
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
    echo OR use alternative methods (see below)
    echo.
    pause
    goto :alternatives
)

echo ✅ Git is installed!
echo.

REM Check if this is a git repository
if not exist ".git" (
    echo Initializing Git repository...
    git init
    echo.
)

echo Adding all files to Git...
git add .
echo.

echo Files staged for commit:
git status --short
echo.

set /p COMMIT_MSG="Enter commit message (or press Enter for default): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Add Smart Task Hub demo and documentation

echo.
echo Committing with message: %COMMIT_MSG%
git commit -m "%COMMIT_MSG%"
echo.

echo ========================================
echo ✅ Files committed to Git!
echo ========================================
echo.

REM Check if remote exists
git remote -v >nul 2>&1
if errorlevel 1 (
    echo.
    echo 📌 Next steps:
    echo 1. Create repository on GitHub
    echo 2. Run: git remote add origin YOUR_REPO_URL
    echo 3. Run: git push -u origin main
    echo.
    echo See GIT_COMMIT_GUIDE.md for detailed instructions
    echo.
) else (
    echo.
    set /p PUSH="Push to remote repository? (y/n): "
    if /i "%PUSH%"=="y" (
        echo.
        echo Pushing to remote...
        git push
        echo.
        echo ✅ Pushed to remote repository!
    )
)

echo.
pause
exit /b 0

:alternatives
echo.
echo ========================================
echo Alternative Methods (No Git Required)
echo ========================================
echo.
echo Method 1: GitHub Desktop (Easiest!)
echo   1. Download: https://desktop.github.com/
echo   2. Install and sign in
echo   3. File → Add Local Repository
echo   4. Select: %CD%
echo   5. Commit and push with GUI
echo.
echo Method 2: VS Code (If you have it)
echo   1. Open folder in VS Code
echo   2. Click Source Control icon (left sidebar)
echo   3. Click "Initialize Repository"
echo   4. Stage all files (+ icon)
echo   5. Enter commit message
echo   6. Click checkmark to commit
echo.
echo Method 3: Upload to GitHub Web
echo   1. Go to github.com
echo   2. Create new repository
echo   3. Click "uploading an existing file"
echo   4. Drag and drop all files
echo   5. Commit changes
echo.
echo Method 4: Create ZIP file
echo   1. Right-click smart-task-hub folder
echo   2. Send to → Compressed (zipped) folder
echo   3. Upload ZIP to GitHub or share directly
echo.
echo ========================================
echo.
pause

@REM Made with Bob
