# 🎨 Smart Task Hub - Visual Demo Guide

## 📱 What You'll See - Complete Visual Walkthrough

This guide shows you exactly what the Smart Task Hub application looks like and how to use it, step by step.

---

## 🚀 Step 1: Starting the Application

### On Windows (Your System)

**Option A: Double-click the batch file**
1. Navigate to: `c:/Users/SuchitraRoutray/.bob/project/smart-task-hub`
2. Double-click `START_DEMO.bat`
3. Wait for two windows to open (Backend and Frontend)
4. Browser will open automatically to http://localhost:5173

**Option B: Manual start (if batch file doesn't work)**

Open PowerShell and run:
```powershell
# First, install Python from https://www.python.org/downloads/
# Then install Node.js from https://nodejs.org/

# Terminal 1 - Backend
cd c:/Users/SuchitraRoutray/.bob/project/smart-task-hub/booking_system_backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python server.py

# Terminal 2 - Frontend (new PowerShell window)
cd c:/Users/SuchitraRoutray/.bob/project/smart-task-hub/booking_system_frontend
npm install
npm run dev
```

---

## 🌟 Step 2: First Screen - User Identification

When you first open http://localhost:5173, you'll see:

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                    ✨ ✨ ✨ ✨ ✨ ✨                          ║
║                                                               ║
║              🌟 Welcome to SmartTaskHub 🌟                   ║
║                                                               ║
║         Your Intelligent Task Management System              ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │                                                      │    ║
║  │  Please identify yourself to continue               │    ║
║  │                                                      │    ║
║  │  Name:  ┌──────────────────────────────┐           │    ║
║  │         │ Enter your name              │           │    ║
║  │         └──────────────────────────────┘           │    ║
║  │                                                      │    ║
║  │  Email: ┌──────────────────────────────┐           │    ║
║  │         │ Enter your email             │           │    ║
║  │         └──────────────────────────────┘           │    ║
║  │                                                      │    ║
║  │              [ Continue ]                           │    ║
║  │                                                      │    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
║                    ✨ ✨ ✨ ✨ ✨ ✨                          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**What to do:**
1. Type your name (e.g., "Suchitra Routray")
2. Type your email (e.g., "suchitra@demo.com")
3. Click "Continue"

**What happens:**
- System creates your user account
- Saves your info in browser
- Takes you to the home page

---

## 🏠 Step 3: Home Page

After login, you'll see:

```
╔═══════════════════════════════════════════════════════════════╗
║  SmartTaskHub                           👤 Suchitra Routray  ║
║  ─────────────────────────────────────────────────────────    ║
║  [Home]  [Flights]  [Tasks]  [My Bookings]                   ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║                    ⭐ ⭐ ⭐ ⭐ ⭐                              ║
║                                                               ║
║              Welcome to SmartTaskHub                         ║
║                                                               ║
║        Your Intelligent Task Management System               ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │                                                      │    ║
║  │  ✨ Features:                                       │    ║
║  │                                                      │    ║
║  │  📋 Smart Task Management                           │    ║
║  │     Create and organize tasks with automatic        │    ║
║  │     priority assignment                             │    ║
║  │                                                      │    ║
║  │  🎯 Intelligent Prioritization                      │    ║
║  │     Tasks are automatically prioritized based on    │    ║
║  │     category and keywords                           │    ║
║  │                                                      │    ║
║  │  📊 Power BI Integration                            │    ║
║  │     Monitor dataset refreshes and get automatic     │    ║
║  │     alerts for failures                             │    ║
║  │                                                      │    ║
║  │  🔄 Automated Scheduling                            │    ║
║  │     Weekly and monthly recurring tasks              │    ║
║  │                                                      │    ║
║  │           [ Get Started with Tasks → ]              │    ║
║  │                                                      │    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**What to do:**
- Click "Get Started with Tasks" or click "Tasks" in the menu

---

## 📋 Step 4: Tasks Page (Main Feature)

This is where the magic happens!

```
╔═══════════════════════════════════════════════════════════════╗
║  SmartTaskHub                           👤 Suchitra Routray  ║
║  ─────────────────────────────────────────────────────────    ║
║  [Home]  [Flights]  [Tasks]  [My Bookings]                   ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  📋 Smart Task Assistant                                     ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │ Filters:                                            │    ║
║  │ Category: [All ▼] Priority: [All ▼] Status: [All ▼]│    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
║  [ + Create New Task ]                                       ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │ 🔴 CRITICAL PRIORITY                                │    ║
║  │ ─────────────────────────────────────────────────   │    ║
║  │ URGENT: Dataset 'Sales Analytics' refresh failed   │    ║
║  │                                                      │    ║
║  │ Status: ⚪ Pending                                  │    ║
║  │ Category: Urgent                                    │    ║
║  │ Created: 2 hours ago                                │    ║
║  │                                                      │    ║
║  │ Description:                                        │    ║
║  │ Refresh failed at 2026-05-29T09:30:00Z             │    ║
║  │ Error: Data source connection timeout               │    ║
║  │ Dataset ID: abc-123-def-456                         │    ║
║  │                                                      │    ║
║  │ [ ✏️ Edit ] [ 🗑️ Delete ] [ ▶️ Mark In Progress ]  │    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │ 🔵 HIGH PRIORITY                                    │    ║
║  │ ─────────────────────────────────────────────────   │    ║
║  │ Weekly: Review dashboard performance metrics       │    ║
║  │                                                      │    ║
║  │ Status: ⚪ Pending                                  │    ║
║  │ Category: Work                                      │    ║
║  │ Created: 1 day ago                                  │    ║
║  │                                                      │    ║
║  │ Description:                                        │    ║
║  │ Check load times, query performance, and user      │    ║
║  │ feedback for all dashboards                         │    ║
║  │                                                      │    ║
║  │ [ ✏️ Edit ] [ 🗑️ Delete ] [ ▶️ Mark In Progress ]  │    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │ 🟢 MEDIUM PRIORITY                                  │    ║
║  │ ─────────────────────────────────────────────────   │    ║
║  │ Update team documentation                           │    ║
║  │                                                      │    ║
║  │ Status: ✅ Completed                                │    ║
║  │ Category: Personal                                  │    ║
║  │ Created: 3 days ago                                 │    ║
║  │                                                      │    ║
║  │ [ ✏️ Edit ] [ 🗑️ Delete ]                          │    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Color Coding:**
- 🔴 **Red Border** = Critical Priority (Urgent tasks)
- 🔵 **Blue Border** = High Priority (Work tasks)
- 🟢 **Green Border** = Medium Priority (Personal tasks)
- ⚪ **Gray Border** = Low Priority or Completed

**Status Icons:**
- ⚪ **Pending** = Not started yet
- 🔵 **In Progress** = Currently working on it
- ✅ **Completed** = Finished

---

## ➕ Step 5: Creating a New Task

Click "Create New Task" button:

```
╔═══════════════════════════════════════════════════════════════╗
║  Create New Task                                    [ ✕ ]    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Title: *                                                     ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │ Fix broken Power BI dashboard                       │    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
║  Description:                                                 ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │ The executive dashboard is showing errors.          │    ║
║  │ Need to check data connections and refresh          │    ║
║  │ schedule immediately.                                │    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
║  Category: *                                                  ║
║  ┌─────────────────────────────────────────────────────┐    ║
║  │ ( ) Work      - Professional tasks                  │    ║
║  │ ( ) Personal  - Personal errands                    │    ║
║  │ (•) Urgent    - Critical items                      │    ║
║  └─────────────────────────────────────────────────────┘    ║
║                                                               ║
║  Priority: Critical (Auto-assigned)                          ║
║  ℹ️ Priority is automatically calculated based on            ║
║     category and keywords in title/description               ║
║                                                               ║
║              [ Cancel ]  [ Create Task ]                     ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**What to do:**
1. Enter a title (required)
2. Enter a description (optional but recommended)
3. Select a category:
   - **Work**: Professional tasks → High priority
   - **Personal**: Personal tasks → Medium priority
   - **Urgent**: Critical tasks → Critical priority
4. Click "Create Task"

**Smart Priority:**
The system automatically assigns priority based on:
- Category selection
- Keywords like: "urgent", "asap", "critical", "emergency", "immediate", "now"

---

## 🔍 Step 6: Filtering Tasks

Use the filter dropdowns at the top:

```
┌─────────────────────────────────────────────────────────┐
│ Category: [All ▼]  Priority: [All ▼]  Status: [All ▼]  │
└─────────────────────────────────────────────────────────┘
```

**Category Filter:**
- All
- Work (🔵 Blue tasks)
- Personal (🟢 Green tasks)
- Urgent (🔴 Red tasks)

**Priority Filter:**
- All
- Low
- Medium
- High
- Critical

**Status Filter:**
- All
- Pending (⚪)
- In Progress (🔵)
- Completed (✅)

---

## 📊 Step 7: Power BI Integration (Advanced)

To see Power BI automation features, open the API documentation:

**URL:** http://localhost:8001/docs

```
╔═══════════════════════════════════════════════════════════════╗
║  SmartTaskHub API - Interactive Documentation                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  📚 API Endpoints                                            ║
║                                                               ║
║  ▼ Power BI Automation                                       ║
║                                                               ║
║    POST /powerbi/check-refreshes                             ║
║    ─────────────────────────────────────────────────────     ║
║    Check Power BI workspace for refresh failures and         ║
║    create tasks automatically                                ║
║                                                               ║
║    [ Try it out ]                                            ║
║                                                               ║
║    Parameters:                                               ║
║    workspace_id: string (required)                           ║
║    user_id: integer (required)                               ║
║    tenant_id: string (optional)                              ║
║    client_id: string (optional)                              ║
║    client_secret: string (optional)                          ║
║                                                               ║
║    ┌─────────────────────────────────────────────────┐      ║
║    │ {                                                │      ║
║    │   "workspace_id": "your-workspace-id",          │      ║
║    │   "user_id": 1                                  │      ║
║    │ }                                                │      ║
║    └─────────────────────────────────────────────────┘      ║
║                                                               ║
║    [ Execute ]                                               ║
║                                                               ║
║  ▼ POST /tasks/scheduled/weekly                              ║
║    Create weekly recurring tasks for Power BI developers     ║
║                                                               ║
║  ▼ POST /tasks/scheduled/monthly                             ║
║    Create monthly recurring tasks for Power BI developers    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**What to do:**
1. Click "Try it out" on any endpoint
2. Fill in the parameters
3. Click "Execute"
4. See the response
5. Go back to the Tasks page to see new tasks

---

## 🎯 Complete Demo Flow (5 Minutes)

### Minute 1: Login
1. Open http://localhost:5173
2. Enter name: "Suchitra Routray"
3. Enter email: "suchitra@demo.com"
4. Click Continue

### Minute 2: Create Manual Task
1. Click "Create New Task"
2. Title: "Review Q4 Dashboard"
3. Description: "Check data accuracy for executive presentation"
4. Category: Work
5. Click "Create Task"
6. See it appear with High priority

### Minute 3: Create Urgent Task
1. Click "Create New Task"
2. Title: "URGENT: Fix broken connection"
3. Description: "Production dashboard showing errors"
4. Category: Urgent
5. Click "Create Task"
6. See it appear with Critical priority at the top

### Minute 4: Try Filtering
1. Click Category dropdown → Select "Urgent"
2. See only urgent tasks
3. Click "All" to see all tasks again
4. Click Status dropdown → Select "Pending"
5. See only pending tasks

### Minute 5: Update Task Status
1. Click on a task to expand it
2. Click "Mark In Progress"
3. See status change to 🔵 In Progress
4. Click "Mark Completed"
5. See status change to ✅ Completed

---

## 🌐 URLs to Remember

| Service | URL | Purpose |
|---------|-----|---------|
| **Frontend** | http://localhost:5173 | Main application UI |
| **Backend API** | http://localhost:8001 | REST API endpoints |
| **API Docs** | http://localhost:8001/docs | Interactive API documentation |
| **Health Check** | http://localhost:8001/ | Check if backend is running |

---

## 🎨 UI Color Scheme

The application uses a beautiful cosmic theme:

**Background:**
- Deep space black with animated stars
- Gradient overlays (purple to pink)
- Twinkling star animations

**Task Cards:**
- **Critical**: Red border, red badge
- **High**: Blue border, blue badge
- **Medium**: Green border, green badge
- **Low**: Gray border, gray badge

**Buttons:**
- Primary: Purple gradient
- Secondary: Gray outline
- Danger: Red
- Success: Green

**Text:**
- Headings: White
- Body: Light gray
- Labels: Medium gray

---

## 📱 Mobile Responsive

The application works on:
- 💻 Desktop (1920x1080 and above)
- 💻 Laptop (1366x768)
- 📱 Tablet (768x1024)
- 📱 Mobile (375x667)

---

## 🆘 Common Issues & Solutions

### Issue 1: "Cannot connect to backend"
**What you see:** Error message in frontend
**Solution:** 
1. Check if backend is running (http://localhost:8001)
2. Restart backend: `python server.py`

### Issue 2: "Tasks not loading"
**What you see:** Empty task list
**Solution:**
1. Check browser console (F12)
2. Verify user is logged in
3. Try refreshing the page

### Issue 3: "Create task button not working"
**What you see:** Nothing happens when clicking
**Solution:**
1. Fill in all required fields (Title and Category)
2. Check browser console for errors

---

## 🎉 Success! You're Ready to Demo

You now know:
- ✅ How to start the application
- ✅ How to login
- ✅ What the UI looks like
- ✅ How to create tasks
- ✅ How to filter and manage tasks
- ✅ Where to find Power BI features
- ✅ How to use the API documentation

**Next Steps:**
1. Try creating your own tasks
2. Experiment with different categories
3. Test the filtering options
4. Explore the API documentation
5. Set up Power BI integration (optional)

---

**Enjoy exploring Smart Task Hub!** 🚀✨

*Built with ❤️ for Power BI Developers*