@echo off
echo ========================================
echo  Smart Task Hub - Demo Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed!
    echo.
    echo Please install Node.js from: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed
echo [OK] Node.js is installed
echo.

REM Check if backend dependencies are installed
if not exist "booking_system_backend\.venv" (
    echo [SETUP] Creating Python virtual environment...
    cd booking_system_backend
    python -m venv .venv
    call .venv\Scripts\activate
    echo [SETUP] Installing backend dependencies...
    pip install -r requirements.txt
    cd ..
    echo.
)

REM Check if frontend dependencies are installed
if not exist "booking_system_frontend\node_modules" (
    echo [SETUP] Installing frontend dependencies...
    cd booking_system_frontend
    call npm install
    cd ..
    echo.
)

echo ========================================
echo  Starting Smart Task Hub Demo
echo ========================================
echo.
echo Backend will start on: http://localhost:8001
echo Frontend will start on: http://localhost:5173
echo API Docs available at: http://localhost:8001/docs
echo.
echo Press Ctrl+C in each window to stop the servers
echo.
pause

REM Start backend in new window
echo [STARTING] Backend server...
start "Smart Task Hub - Backend" cmd /k "cd booking_system_backend && .venv\Scripts\activate && python server.py"

REM Wait a bit for backend to start
timeout /t 5 /nobreak >nul

REM Start frontend in new window
echo [STARTING] Frontend server...
start "Smart Task Hub - Frontend" cmd /k "cd booking_system_frontend && npm run dev"

REM Wait a bit for frontend to start
timeout /t 5 /nobreak >nul

echo.
echo ========================================
echo  Demo is starting!
echo ========================================
echo.
echo Opening browser in 5 seconds...
timeout /t 5 /nobreak >nul

REM Open browser
start http://localhost:5173

echo.
echo ========================================
echo  Demo is running!
echo ========================================
echo.
echo Frontend: http://localhost:5173
echo Backend API: http://localhost:8001
echo API Docs: http://localhost:8001/docs
echo.
echo To stop the demo:
echo 1. Close the Backend window
echo 2. Close the Frontend window
echo 3. Or press Ctrl+C in each window
echo.
echo Enjoy the demo!
pause

@REM Made with Bob
