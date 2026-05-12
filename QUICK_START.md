# 🚀 Quick Start - Where & How to Use Your Application

## 📍 WHERE IS THE APPLICATION?

### On Your Computer:
```
Location: C:\Users\004I25744\Downloads\IBM-bob\galaxium-travels
```

### In VS Code:
- You currently have it open in VS Code
- Look at the left sidebar - you'll see the folder structure
- The application code is RIGHT HERE in your current workspace!

---

## 🎯 HOW TO START THE APPLICATION

### STEP 1: Open PowerShell/Command Prompt

Press `Windows Key + R`, type `cmd`, press Enter

### STEP 2: Navigate to Your Application

```bash
cd C:\Users\004I25744\Downloads\IBM-bob\galaxium-travels
```

### STEP 3: Start Backend (First Terminal)

Copy and paste these commands ONE BY ONE:

```bash
cd booking_system_backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python server.py
```

**✅ SUCCESS LOOKS LIKE:**
```
INFO:     Uvicorn running on http://0.0.0.0:8001
```

**⚠️ KEEP THIS WINDOW OPEN!** Don't close it.

---

### STEP 4: Start Frontend (Second Terminal)

Open a **NEW** Command Prompt window (repeat Step 1)

Navigate to the same folder:
```bash
cd C:\Users\004I25744\Downloads\IBM-bob\galaxium-travels
```

Then run:
```bash
cd booking_system_frontend
npm install
npm run dev
```

**✅ SUCCESS LOOKS LIKE:**
```
➜  Local:   http://localhost:5173/
```

**⚠️ KEEP THIS WINDOW OPEN TOO!**

---

## 🌐 WHERE TO OPEN THE APPLICATION

### In Your Web Browser:

1. Open **Google Chrome**, **Edge**, or **Firefox**
2. Type in the address bar:
   ```
   http://localhost:5173
   ```
3. Press Enter

**🎉 YOU SHOULD SEE:**
- A space-themed website
- "Galaxium Travels" in the header
- Navigation menu: Home, Flights, My Bookings, Tasks

---

## 🎮 HOW TO USE THE TASK ASSISTANT

### Step 1: Log In

1. Click the **"Login"** button (top-right corner)
2. Enter:
   - Name: `Alice`
   - Email: `alice@example.com`
3. Click **"Continue"**

### Step 2: Go to Tasks

1. Look at the top navigation menu
2. Click **"Tasks"**
3. You're now on the Tasks page!

### Step 3: Create Your First Task

1. Click the big **"Create New Task"** button
2. Fill in the form:
   ```
   Title: Buy groceries
   Description: Milk, eggs, bread
   Category: Personal
   ```
3. Click **"Create Task"**

**🎉 SUCCESS!** You'll see your task appear with:
- A green "Personal" badge
- Yellow "Medium" priority
- A pending status icon

### Step 4: Try More Features

**Update Status:**
- Click the circle icon (⚪) on your task
- It changes to "In Progress" (🔵)
- Click again → "Completed" (✅)

**Create an Urgent Task:**
```
Title: URGENT: Submit report
Description: Deadline is today!
Category: Work
```
- Notice it gets "Critical" priority automatically!

**Use Filters:**
- Click "Filters" button
- Select "Priority: Critical"
- See only urgent tasks

---

## 📸 VISUAL GUIDE

### What You'll See:

```
┌─────────────────────────────────────────────────────┐
│  🚀 Galaxium Travels          [Login] or [Alice ▼] │
│  Home | Flights | My Bookings | Tasks              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  My Tasks                                          │
│  Organize and manage your tasks                    │
│                                                     │
│  [+ Create New Task]                               │
│                                                     │
│  ┌──────────────────────────────────────┐         │
│  │ 🟢 Personal        Medium      ⚪    │         │
│  │ Buy groceries                        │         │
│  │ Milk, eggs, bread                    │         │
│  │ [Edit] [Delete]                      │         │
│  └──────────────────────────────────────┘         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ❓ TROUBLESHOOTING

### "Cannot find module" or "Command not found"

**For Backend:**
```bash
# Make sure Python is installed
python --version

# If not installed, download from: https://www.python.org/downloads/
```

**For Frontend:**
```bash
# Make sure Node.js is installed
node --version

# If not installed, download from: https://nodejs.org/
```

### "Port already in use"

**Backend (Port 8001):**
```bash
# Find and kill the process
netstat -ano | findstr :8001
taskkill /PID <process_id> /F
```

**Frontend (Port 5173):**
```bash
# Find and kill the process
netstat -ano | findstr :5173
taskkill /PID <process_id> /F
```

### "Page not loading"

1. Check both terminals are still running
2. Look for error messages in the terminals
3. Try refreshing the browser (Ctrl + F5)
4. Make sure you're using: `http://localhost:5173` (not https)

---

## 🎯 QUICK TEST CHECKLIST

After starting the application, verify:

- [ ] Backend terminal shows "Uvicorn running on http://0.0.0.0:8001"
- [ ] Frontend terminal shows "Local: http://localhost:5173/"
- [ ] Browser opens to http://localhost:5173
- [ ] You see "Galaxium Travels" header
- [ ] You can click "Login" and enter credentials
- [ ] You see "Tasks" in the navigation menu
- [ ] You can create a task
- [ ] Task appears in the list with correct colors

---

## 📞 NEED MORE HELP?

1. **Detailed Guide:** Open `TASK_ASSISTANT_GUIDE.md` in this folder
2. **API Documentation:** Visit http://localhost:8001/docs (after starting backend)
3. **Check Logs:** Look at the terminal windows for error messages

---

## 🎉 YOU'RE READY!

Your application is:
- ✅ Located at: `C:\Users\004I25744\Downloads\IBM-bob\galaxium-travels`
- ✅ Opened in: VS Code (your current window)
- ✅ Runs in: Web browser at http://localhost:5173
- ✅ Needs: 2 terminal windows running (backend + frontend)

**Start using it now by following the steps above!** 🚀