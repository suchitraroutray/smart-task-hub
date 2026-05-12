# 🎯 Smart Task Assistant - Step-by-Step Usage Guide

This guide will walk you through using the Smart Task Assistant feature in the SmartTaskHub application.

## 📋 Table of Contents
1. [Starting the Application](#starting-the-application)
2. [Logging In](#logging-in)
3. [Creating Your First Task](#creating-your-first-task)
4. [Managing Tasks](#managing-tasks)
5. [Using Filters](#using-filters)
6. [Complete Example Walkthrough](#complete-example-walkthrough)
7. [Testing the Backend API](#testing-the-backend-api)

---

## 🚀 Starting the Application

### Step 1: Open Terminal/Command Prompt

Navigate to the project directory:
```bash
cd c:/Users/004I25744/Downloads/IBM-bob/galaxium-travels
```

### Step 2: Start the Backend Server

Open a **new terminal window** and run:

**On Windows:**
```bash
cd booking_system_backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python server.py
```

**On macOS/Linux:**
```bash
cd booking_system_backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

✅ **Expected Output:**
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8001
```

### Step 3: Start the Frontend Server

Open **another new terminal window** and run:

```bash
cd booking_system_frontend
npm install
npm run dev
```

✅ **Expected Output:**
```
VITE v7.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

### Step 4: Open the Application

Open your web browser and go to:
```
http://localhost:5173
```

---

## 👤 Logging In

### Step 1: Click "Login" Button
- You'll see the "Login" button in the top-right corner of the homepage
- Click it to open the login modal

### Step 2: Enter Your Credentials
Use one of the pre-seeded demo users:

| Name | Email |
|------|-------|
| Alice | alice@example.com |
| Bob | bob@example.com |
| Charlie | charlie@example.com |

**Example:**
- Name: `Alice`
- Email: `alice@example.com`

### Step 3: Click "Continue"
- The system will log you in
- You'll see your name in the top-right corner
- The "Tasks" link will now appear in the navigation menu

---

## ✨ Creating Your First Task

### Step 1: Navigate to Tasks Page
- Click **"Tasks"** in the navigation menu (top of the page)
- You'll see the Tasks page with a "Create New Task" button

### Step 2: Click "Create New Task"
- A form will appear with the following fields:
  - **Title** (required)
  - **Description** (optional)
  - **Category** (required dropdown)

### Step 3: Fill in Task Details

**Example Task:**
```
Title: Prepare quarterly report
Description: Compile Q4 financial data and create presentation for board meeting
Category: Work
```

### Step 4: Click "Create Task"
- The task will be created instantly
- You'll see a success notification
- The task appears in the task list with:
  - 🔵 Blue "Work" badge
  - Orange "High" priority indicator (auto-calculated!)
  - ⚪ Pending status icon

---

## 🎨 Managing Tasks

### Viewing Task Details

Each task card shows:
- **Category Badge** (colored: Blue=Work, Green=Personal, Red=Urgent)
- **Priority Level** (Low, Medium, High, Critical)
- **Title** and **Description**
- **Status** (Pending, In Progress, Completed)
- **Created/Updated Dates**
- **Action Buttons** (Edit, Delete)

### Updating Task Status

Click the **status icon** on the top-right of any task card:
- ⚪ **Pending** → Click to mark as "In Progress"
- 🔵 **In Progress** → Click to mark as "Completed"
- ✅ **Completed** → Click to reset to "Pending"

### Editing a Task

1. Click the **"Edit"** button on any task card
2. Modify the title, description, or category
3. Click **"Update Task"**
4. Priority will be recalculated if you change the category!

### Deleting a Task

1. Click the **"Delete"** button on any task card
2. Confirm the deletion in the popup
3. Task is permanently removed

---

## 🔍 Using Filters

### Step 1: Click "Filters" Button
- Located at the top of the task list
- Shows "Active" badge if filters are applied

### Step 2: Select Filter Options

**Filter by Category:**
- All (default)
- Work
- Personal
- Urgent

**Filter by Priority:**
- All (default)
- Critical
- High
- Medium
- Low

**Filter by Status:**
- All (default)
- Pending
- In Progress
- Completed

### Step 3: View Filtered Results
- Task count updates automatically
- Only matching tasks are displayed
- Click "Clear All" to reset filters

---

## 🎯 Complete Example Walkthrough

Let's create and manage a complete set of tasks to test all features!

### Example 1: Work Task with Urgent Keywords

**Create Task:**
```
Title: URGENT: Fix production bug
Description: Critical issue affecting customer payments - needs immediate attention
Category: Work
```

**Expected Result:**
- ✅ Task created successfully
- 🔵 Blue "Work" badge
- 🔴 Red "Critical" priority (upgraded due to "URGENT" and "immediate" keywords!)
- ⚪ Pending status

**Test Actions:**
1. Click status icon → Changes to "In Progress" 🔵
2. Click status icon again → Changes to "Completed" ✅
3. Click "Edit" → Change category to "Personal"
4. Notice priority changes to "High" (recalculated!)

---

### Example 2: Personal Task

**Create Task:**
```
Title: Buy groceries
Description: Milk, eggs, bread, vegetables
Category: Personal
```

**Expected Result:**
- ✅ Task created successfully
- 🟢 Green "Personal" badge
- 🟡 Yellow "Medium" priority
- ⚪ Pending status

---

### Example 3: Urgent Task

**Create Task:**
```
Title: Submit tax documents
Description: Deadline is tomorrow
Category: Urgent
```

**Expected Result:**
- ✅ Task created successfully
- 🔴 Red "Urgent" badge
- 🔴 Red "Critical" priority
- ⚪ Pending status

---

### Example 4: Testing Filters

**After creating the 3 tasks above:**

1. **Filter by Priority = "Critical"**
   - Should show: "Fix production bug" and "Submit tax documents"
   - Count: "Showing 2 of 3 tasks"

2. **Filter by Category = "Work"**
   - Should show: "Fix production bug"
   - Count: "Showing 1 of 3 tasks"

3. **Filter by Status = "Completed"**
   - Mark one task as completed first
   - Should show only completed tasks

4. **Click "Clear All"**
   - All 3 tasks visible again

---

## 🧪 Testing the Backend API

### Test 1: Create Task via API

Open a new terminal and run:

```bash
curl -X POST http://localhost:8001/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "title": "API Test Task",
    "description": "Testing the REST API",
    "category": "Work"
  }'
```

**Expected Response:**
```json
{
  "task_id": 4,
  "user_id": 1,
  "title": "API Test Task",
  "description": "Testing the REST API",
  "category": "Work",
  "priority": "High",
  "status": "pending",
  "created_at": "2026-05-12T07:56:00.000000",
  "updated_at": "2026-05-12T07:56:00.000000"
}
```

### Test 2: List All Tasks

```bash
curl http://localhost:8001/api/tasks?user_id=1
```

### Test 3: Update Task Status

```bash
curl -X PUT http://localhost:8001/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "completed"
  }'
```

### Test 4: Run Backend Tests

```bash
cd booking_system_backend
pytest tests/test_task_services.py -v
```

**Expected Output:**
```
test_calculate_priority_urgent_category PASSED
test_calculate_priority_work_category PASSED
test_create_task_success PASSED
test_list_tasks_filter_by_category PASSED
... (20+ tests should pass)
```

---

## 🎓 Key Features to Test

### ✅ Smart Priority Assignment
- Create a Personal task with title "ASAP: Call dentist"
- Notice priority upgrades from Medium to High!

### ✅ Category-Based Colors
- Work tasks = Blue badge
- Personal tasks = Green badge
- Urgent tasks = Red badge

### ✅ Status Workflow
- Pending (⚪) → In Progress (🔵) → Completed (✅)
- Click status icon to cycle through states

### ✅ Real-Time Filtering
- Apply multiple filters simultaneously
- See task count update instantly
- Clear filters to see all tasks

### ✅ Edit & Recalculation
- Edit a task's category
- Watch priority recalculate automatically

---

## 🐛 Troubleshooting

### Backend Not Starting
```bash
# Check Python version (need 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Frontend Not Starting
```bash
# Check Node version (need 18+)
node --version

# Clear and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Tasks Not Appearing
1. Make sure you're logged in (see your name in top-right)
2. Check browser console for errors (F12)
3. Verify backend is running on port 8001
4. Check that frontend .env has correct API URL

### Database Issues
```bash
# Delete and recreate database
cd booking_system_backend
rm -f booking_system.db
python server.py  # Will recreate with seed data
```

---

## 🎉 Success Checklist

After following this guide, you should be able to:

- ✅ Start both backend and frontend servers
- ✅ Log in with a demo user
- ✅ Navigate to the Tasks page
- ✅ Create tasks in all three categories
- ✅ See automatic priority assignment
- ✅ Update task status by clicking the icon
- ✅ Edit and delete tasks
- ✅ Use filters to find specific tasks
- ✅ See keyword-based priority upgrades
- ✅ Test the REST API with curl
- ✅ Run the test suite successfully

---

## 📚 Next Steps

1. **Explore the API Documentation**
   - Visit http://localhost:8001/docs
   - Try the interactive API explorer

2. **Test MCP Tools** (for AI agents)
   - Use the MCP endpoint at http://localhost:8001/mcp
   - Test with an MCP-compatible client

3. **Create More Complex Tasks**
   - Try different keyword combinations
   - Test edge cases
   - Experiment with filters

4. **Review the Code**
   - Backend: `booking_system_backend/services/task.py`
   - Frontend: `booking_system_frontend/src/pages/Tasks.tsx`
   - Tests: `booking_system_backend/tests/test_task_services.py`

---

**Happy Task Managing! 🚀**

*Built with Bob - Your AI-native IDE*