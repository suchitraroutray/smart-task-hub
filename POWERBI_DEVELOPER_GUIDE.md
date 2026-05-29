# 📊 SmartTaskHub for Power BI Developers - Complete Guide

## 📋 Table of Contents
1. [Introduction](#introduction)
2. [Purpose & Benefits](#purpose--benefits)
3. [Features Overview](#features-overview)
4. [Prerequisites](#prerequisites)
5. [Installation & Setup](#installation--setup)
6. [Power BI Integration Setup](#power-bi-integration-setup)
7. [How to Use the Application](#how-to-use-the-application)
8. [Automation Features](#automation-features)
9. [Real-World Scenarios](#real-world-scenarios)
10. [API Reference](#api-reference)
11. [Troubleshooting](#troubleshooting)
12. [Best Practices](#best-practices)

---

## 🎯 Introduction

**SmartTaskHub** is an intelligent task management system specifically enhanced for Power BI developers. It combines manual task tracking with automated monitoring of your Power BI workspace to help you stay on top of dashboard maintenance, refresh failures, and routine tasks.

### What Makes It Special for Power BI Developers?

- ✅ **Automatic Task Creation** from Power BI refresh failures
- ✅ **Smart Priority Assignment** based on keywords and categories
- ✅ **Scheduled Recurring Tasks** for routine maintenance
- ✅ **Power BI Workspace Monitoring** via REST API
- ✅ **Performance Tracking** for slow dataset refreshes
- ✅ **Visual Organization** with color-coded categories

---

## 🎁 Purpose & Benefits

### Purpose

SmartTaskHub helps Power BI developers:
1. **Never miss a refresh failure** - Automatic detection and task creation
2. **Stay organized** - Track all dashboard work in one place
3. **Prioritize effectively** - Smart priority assignment
4. **Maintain routine tasks** - Automated weekly/monthly task creation
5. **Monitor performance** - Detect slow refreshes automatically

### Benefits

#### For Individual Developers
- 📈 **Increased Productivity** - Spend less time tracking, more time developing
- 🎯 **Better Focus** - Automatic prioritization shows what needs attention
- 🔔 **Proactive Monitoring** - Catch issues before users report them
- 📊 **Progress Tracking** - See what you've accomplished

#### For Teams
- 👥 **Shared Visibility** - Everyone sees critical tasks
- 🔄 **Consistent Processes** - Automated recurring tasks ensure nothing is forgotten
- 📝 **Documentation** - Task history provides audit trail
- ⚡ **Faster Response** - Automated alerts for failures

---

## 🌟 Features Overview

### Core Features

#### 1. Manual Task Management
- Create, edit, and delete tasks
- Update task status (Pending → In Progress → Completed)
- Filter by category, priority, and status
- Color-coded visual organization

#### 2. Smart Priority Assignment
```
Automatic Priority Calculation:
- Urgent category → Critical priority
- Work category → High priority
- Personal category → Medium priority

Keyword Detection (auto-upgrades priority):
- "urgent", "asap", "critical", "emergency", "immediate", "now"
```

#### 3. Power BI Automation (NEW!)
- **Refresh Failure Detection** - Auto-creates tasks when datasets fail to refresh
- **Performance Monitoring** - Detects slow refreshes (>30 minutes)
- **Scheduled Tasks** - Weekly and monthly recurring tasks
- **Workspace Integration** - Connects to Power BI REST API

---

## 📋 Prerequisites

### Required Software

1. **Python 3.8+**
   - Download: https://www.python.org/downloads/
   - Verify: `python --version`

2. **Node.js 18+**
   - Download: https://nodejs.org/
   - Verify: `node --version`

3. **Git**
   - Download: https://git-scm.com/
   - Verify: `git --version`

### Required Accounts & Permissions

1. **Azure AD App Registration** (for Power BI API)
   - Access to Azure Portal
   - Permissions to create App Registrations
   - Power BI Service Administrator role (or workspace admin)

2. **Power BI Service**
   - Power BI Pro or Premium license
   - Access to workspaces you want to monitor
   - Workspace Admin permissions

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
# Navigate to your desired directory
cd C:/Users/YourName/Projects

# Clone the repository
git clone https://github.com/suchitraroutray/smart-task-hub
cd smart-task-hub
```

### Step 2: Backend Setup

```bash
# Navigate to backend directory
cd booking_system_backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Frontend Setup

```bash
# Open a new terminal
cd booking_system_frontend

# Install dependencies
npm install
```

### Step 4: Environment Configuration

```bash
# In booking_system_backend directory
# Copy the example environment file
copy .env.example .env

# Edit .env file with your settings
notepad .env
```

---

## 🔧 Power BI Integration Setup

### Step 1: Create Azure AD App Registration

1. **Go to Azure Portal**
   - Navigate to: https://portal.azure.com
   - Sign in with your organizational account

2. **Create App Registration**
   ```
   Azure Active Directory → App registrations → New registration
   
   Name: SmartTaskHub-PowerBI-Monitor
   Supported account types: Single tenant
   Redirect URI: (leave blank for now)
   
   Click "Register"
   ```

3. **Note Your Credentials**
   ```
   After registration, copy these values:
   - Application (client) ID
   - Directory (tenant) ID
   ```

4. **Create Client Secret**
   ```
   Go to: Certificates & secrets → New client secret
   
   Description: SmartTaskHub Secret
   Expires: 24 months (or as per your policy)
   
   Click "Add"
   
   ⚠️ IMPORTANT: Copy the secret VALUE immediately!
   You won't be able to see it again.
   ```

### Step 2: Grant Power BI API Permissions

1. **Add API Permissions**
   ```
   Go to: API permissions → Add a permission
   
   Select: Power BI Service
   
   Delegated permissions:
   ✅ Dataset.Read.All
   ✅ Dataset.ReadWrite.All
   ✅ Workspace.Read.All
   
   Click "Add permissions"
   ```

2. **Grant Admin Consent**
   ```
   Click "Grant admin consent for [Your Organization]"
   Click "Yes" to confirm
   
   All permissions should show green checkmarks
   ```

### Step 3: Enable Power BI Service Principal

1. **Go to Power BI Admin Portal**
   ```
   https://app.powerbi.com
   Settings (gear icon) → Admin portal
   ```

2. **Enable Service Principal Access**
   ```
   Tenant settings → Developer settings
   
   Find: "Service principals can use Power BI APIs"
   Toggle: Enabled
   Apply to: The entire organization (or specific security group)
   
   Click "Apply"
   ```

3. **Add Service Principal to Workspace**
   ```
   Go to your Power BI workspace
   Settings → Access
   
   Add: Your app name (SmartTaskHub-PowerBI-Monitor)
   Role: Admin or Member
   
   Click "Add"
   ```

### Step 4: Configure Application

Edit your `.env` file in `booking_system_backend`:

```env
# Power BI API Configuration
POWERBI_TENANT_ID=12345678-1234-1234-1234-123456789abc
POWERBI_CLIENT_ID=87654321-4321-4321-4321-cba987654321
POWERBI_CLIENT_SECRET=your-secret-value-here

# Power BI Workspace IDs (get from workspace URL)
# URL format: https://app.powerbi.com/groups/WORKSPACE-ID/...
POWERBI_WORKSPACE_IDS=workspace-id-1,workspace-id-2

# Automation Settings
POWERBI_CHECK_INTERVAL_MINUTES=15
POWERBI_SLOW_REFRESH_THRESHOLD_MINUTES=30
```

### Step 5: Find Your Workspace ID

```
1. Go to Power BI Service (app.powerbi.com)
2. Open your workspace
3. Look at the URL:
   https://app.powerbi.com/groups/12345678-abcd-efgh-ijkl-123456789abc/...
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                    This is your Workspace ID
4. Copy and paste into .env file
```

---

## 💻 How to Use the Application

### Starting the Application

#### Option 1: Quick Start (Recommended)

**Windows:**
```bash
# From smart-task-hub directory
start.bat
```

**macOS/Linux:**
```bash
# From smart-task-hub directory
./start.sh
```

#### Option 2: Manual Start

**Terminal 1 - Backend:**
```bash
cd booking_system_backend
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux
python server.py
```

**Terminal 2 - Frontend:**
```bash
cd booking_system_frontend
npm run dev
```

### Accessing the Application

Once started, open your browser:

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8001
- **API Documentation**: http://localhost:8001/docs

### First-Time Setup

1. **Open the Application**
   ```
   Navigate to: http://localhost:5173
   ```

2. **Login**
   ```
   Click "Login" button (top-right)
   
   Use demo account:
   Name: Alice
   Email: alice@example.com
   
   Click "Continue"
   ```

3. **Navigate to Tasks**
   ```
   Click "Tasks" in the navigation menu
   ```

4. **You're Ready!**
   ```
   You can now:
   - Create manual tasks
   - Trigger Power BI monitoring
   - Create scheduled tasks
   ```

---

## 🤖 Automation Features

### 1. Power BI Refresh Monitoring

#### How It Works

The system connects to Power BI REST API and checks:
- Dataset refresh status
- Refresh history
- Error messages
- Refresh duration

When a failure is detected, it automatically creates a task.

#### Triggering Manual Check

**Via API:**
```bash
curl -X POST "http://localhost:8001/powerbi/check-refreshes" \
  -H "Content-Type: application/json" \
  -d '{
    "workspace_id": "your-workspace-id",
    "user_id": 1
  }'
```

**Via Swagger UI:**
```
1. Go to: http://localhost:8001/docs
2. Find: POST /powerbi/check-refreshes
3. Click "Try it out"
4. Enter:
   - workspace_id: your-workspace-id
   - user_id: 1
5. Click "Execute"
```

#### What Gets Created

**Example Task for Refresh Failure:**
```
Title: "URGENT: Dataset 'Sales Analytics' refresh failed"
Category: Urgent
Priority: Critical
Description: 
  Refresh failed at 2026-05-27T02:30:00Z
  Error: Gateway timeout - unable to connect to data source
  Dataset ID: abc123-def456-ghi789
Status: Pending
```

**Example Task for Slow Refresh:**
```
Title: "Dataset 'Finance Dashboard' refresh is slow"
Category: Work
Priority: High
Description:
  Refresh took 45.3 minutes (threshold: 30 minutes)
  Consider optimizing the dataset or queries.
  Dataset ID: xyz789-uvw456-rst123
Status: Pending
```

### 2. Scheduled Recurring Tasks

#### Weekly Tasks

**Trigger via API:**
```bash
curl -X POST "http://localhost:8001/tasks/scheduled/weekly?user_id=1"
```

**Creates:**
```
1. "Weekly: Review dashboard performance metrics"
   - Check load times, query performance, user feedback
   
2. "Weekly: Backup Power BI reports"
   - Export PBIX files and save to backup location
   
3. "Weekly: Review team DAX code"
   - Code review for best practices and optimization
```

#### Monthly Tasks

**Trigger via API:**
```bash
curl -X POST "http://localhost:8001/tasks/scheduled/monthly?user_id=1"
```

**Creates:**
```
1. "Monthly: Update fiscal year calculations"
   - Review and update fiscal calendar, YTD, QTD
   
2. "Monthly: Review data source connections"
   - Verify all sources connected, credentials valid
   
3. "Monthly: Clean up unused datasets"
   - Archive or delete datasets no longer in use
```

### 3. Setting Up Automated Monitoring (Advanced)

For continuous monitoring, you can set up a scheduled task:

**Windows Task Scheduler:**
```powershell
# Create a PowerShell script: monitor-powerbi.ps1
$uri = "http://localhost:8001/powerbi/check-refreshes"
$body = @{
    workspace_id = "your-workspace-id"
    user_id = 1
} | ConvertTo-Json

Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/json"

# Schedule to run every 15 minutes via Task Scheduler
```

**Linux Cron Job:**
```bash
# Add to crontab (crontab -e)
*/15 * * * * curl -X POST "http://localhost:8001/powerbi/check-refreshes" -H "Content-Type: application/json" -d '{"workspace_id":"your-id","user_id":1}'
```

---

## 🎯 Real-World Scenarios

### Scenario 1: Morning Routine

**8:00 AM - Start Your Day**

1. **Open SmartTaskHub**
   ```
   Navigate to: http://localhost:5173
   Login with your credentials
   ```

2. **Check for Overnight Failures**
   ```
   Go to API docs: http://localhost:8001/docs
   Run: POST /powerbi/check-refreshes
   
   System checks all datasets and creates tasks for any failures
   ```

3. **Review Critical Tasks**
   ```
   In SmartTaskHub:
   - Click "Filters"
   - Select Priority: "Critical"
   - See all urgent items
   ```

4. **Start Working**
   ```
   - Click status icon on first task (⚪ → 🔵)
   - Open Power BI Desktop
   - Fix the issue
   - Return to SmartTaskHub
   - Mark as completed (🔵 → ✅)
   ```

### Scenario 2: Client Request Workflow

**10:30 AM - Client Emails**

**Email Received:**
```
From: client@company.com
Subject: URGENT: Sales Dashboard showing wrong numbers
Body: The revenue chart is displaying incorrect totals...
```

**Your Actions:**

1. **Create Task in SmartTaskHub**
   ```
   Click "Create New Task"
   
   Title: "URGENT: Fix Sales Dashboard revenue calculation"
   Description: "Client reported incorrect totals in revenue chart. 
                 Email from client@company.com at 10:30 AM"
   Category: Urgent
   
   Click "Create Task"
   ```

2. **System Auto-Assigns Priority**
   ```
   Priority: Critical (because of "URGENT" keyword)
   Status: Pending
   Badge: Red "Urgent"
   ```

3. **Work on the Issue**
   ```
   - Click status → In Progress
   - Open Power BI Desktop
   - Investigate DAX measure
   - Find issue: SUM should be SUMX
   - Fix and test
   - Publish to service
   ```

4. **Complete and Document**
   ```
   - Return to SmartTaskHub
   - Click "Edit" on task
   - Update description: "Fixed: Changed SUM to SUMX in Revenue measure. 
                          Tested with sample data. Published at 11:15 AM"
   - Click status → Completed
   ```

### Scenario 3: Weekly Maintenance

**Monday 9:00 AM - Weekly Tasks**

1. **Create Weekly Tasks**
   ```
   Go to: http://localhost:8001/docs
   Run: POST /tasks/scheduled/weekly
   
   System creates 3 tasks:
   - Review dashboard performance
   - Backup reports
   - Review team code
   ```

2. **Work Through Tasks**
   ```
   Task 1: Review dashboard performance
   - Open Power BI Service
   - Check Performance Analyzer
   - Document slow visuals
   - Mark task as completed
   
   Task 2: Backup reports
   - Download PBIX files
   - Save to backup location
   - Mark as completed
   
   Task 3: Review team code
   - Check pull requests
   - Review DAX measures
   - Provide feedback
   - Mark as completed
   ```

### Scenario 4: Performance Investigation

**2:00 PM - Slow Dashboard Reported**

1. **Manual Task Creation**
   ```
   Title: "Investigate slow Customer Dashboard"
   Description: "Users reporting 30+ second load times"
   Category: Work
   Priority: High (auto-assigned)
   ```

2. **Investigation Process**
   ```
   - Mark as In Progress
   - Open Performance Analyzer
   - Identify slow DAX queries
   - Check data model relationships
   - Optimize measures
   ```

3. **Trigger Automated Check**
   ```
   Run: POST /powerbi/check-refreshes
   
   System detects: "Dataset 'Customer Analytics' refresh took 45 minutes"
   Creates new task automatically
   ```

4. **Complete Both Tasks**
   ```
   Original task: "Optimized 3 DAX measures, reduced load time to 8 seconds"
   Auto-created task: "Implemented incremental refresh, reduced to 12 minutes"
   ```

### Scenario 5: Month-End Routine

**First Monday of Month**

1. **Create Monthly Tasks**
   ```
   Run: POST /tasks/scheduled/monthly
   
   Creates:
   - Update fiscal year calculations
   - Review data source connections
   - Clean up unused datasets
   ```

2. **Fiscal Year Update**
   ```
   - Mark as In Progress
   - Open Date dimension table
   - Update fiscal calendar
   - Test YTD and QTD calculations
   - Publish changes
   - Mark as Completed
   ```

3. **Data Source Review**
   ```
   - Check all gateway connections
   - Verify credentials
   - Test data refresh
   - Document any issues
   - Mark as Completed
   ```

4. **Dataset Cleanup**
   ```
   - List all datasets
   - Identify unused ones (no views in 30 days)
   - Archive PBIX files
   - Delete from service
   - Mark as Completed
   ```

---

## 📚 API Reference

### Power BI Automation Endpoints

#### Check Refresh Failures

```http
POST /powerbi/check-refreshes
Content-Type: application/json

{
  "workspace_id": "12345678-abcd-efgh-ijkl-123456789abc",
  "user_id": 1,
  "tenant_id": "optional-override",
  "client_id": "optional-override",
  "client_secret": "optional-override"
}
```

**Response:**
```json
[
  {
    "task_id": 15,
    "user_id": 1,
    "title": "URGENT: Dataset 'Sales Analytics' refresh failed",
    "description": "Refresh failed at 2026-05-27T02:30:00Z\nError: Gateway timeout",
    "category": "Urgent",
    "priority": "Critical",
    "status": "pending",
    "created_at": "2026-05-27T09:00:00",
    "updated_at": "2026-05-27T09:00:00"
  }
]
```

#### Create Weekly Tasks

```http
POST /tasks/scheduled/weekly?user_id=1
```

**Response:**
```json
[
  {
    "task_id": 16,
    "title": "Weekly: Review dashboard performance metrics",
    "category": "Work",
    "priority": "High",
    "status": "pending"
  },
  {
    "task_id": 17,
    "title": "Weekly: Backup Power BI reports",
    "category": "Work",
    "priority": "High",
    "status": "pending"
  },
  {
    "task_id": 18,
    "title": "Weekly: Review team DAX code",
    "category": "Work",
    "priority": "High",
    "status": "pending"
  }
]
```

#### Create Monthly Tasks

```http
POST /tasks/scheduled/monthly?user_id=1
```

**Response:**
```json
[
  {
    "task_id": 19,
    "title": "Monthly: Update fiscal year calculations",
    "category": "Work",
    "priority": "High",
    "status": "pending"
  },
  {
    "task_id": 20,
    "title": "Monthly: Review data source connections",
    "category": "Work",
    "priority": "High",
    "status": "pending"
  },
  {
    "task_id": 21,
    "title": "Monthly: Clean up unused datasets",
    "category": "Work",
    "priority": "High",
    "status": "pending"
  }
]
```

### Task Management Endpoints

#### List Tasks

```http
GET /api/tasks?user_id=1&category=Work&priority=Critical&status=pending
```

#### Create Task

```http
POST /api/tasks
Content-Type: application/json

{
  "user_id": 1,
  "title": "Fix dashboard",
  "description": "Revenue chart broken",
  "category": "Work"
}
```

#### Update Task

```http
PUT /api/tasks/1
Content-Type: application/json

{
  "status": "completed"
}
```

#### Delete Task

```http
DELETE /api/tasks/1
```

---

## 🔧 Troubleshooting

### Power BI Integration Issues

#### Error: "Failed to get access token"

**Cause:** Invalid Azure AD credentials

**Solution:**
```
1. Verify credentials in .env file:
   - POWERBI_TENANT_ID
   - POWERBI_CLIENT_ID
   - POWERBI_CLIENT_SECRET

2. Check Azure AD App Registration:
   - App still exists
   - Secret hasn't expired
   - Permissions granted

3. Test credentials:
   curl -X POST "https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token" \
     -d "grant_type=client_credentials" \
     -d "client_id={client-id}" \
     -d "client_secret={client-secret}" \
     -d "scope=https://analysis.windows.net/powerbi/api/.default"
```

#### Error: "Workspace not found"

**Cause:** Invalid workspace ID or insufficient permissions

**Solution:**
```
1. Verify workspace ID:
   - Go to Power BI Service
   - Open workspace
   - Check URL for correct ID

2. Check permissions:
   - Service principal added to workspace
   - Role is Admin or Member
   - Service principal access enabled in tenant settings

3. Test workspace access:
   GET https://api.powerbi.com/v1.0/myorg/groups/{workspace-id}
   Authorization: Bearer {access-token}
```

#### Error: "No datasets found"

**Cause:** Empty workspace or permission issues

**Solution:**
```
1. Verify workspace has datasets:
   - Open workspace in Power BI Service
   - Check Datasets tab

2. Check API permissions:
   - Dataset.Read.All granted
   - Admin consent provided

3. Test dataset access:
   GET https://api.powerbi.com/v1.0/myorg/groups/{workspace-id}/datasets
   Authorization: Bearer {access-token}
```

### Application Issues

#### Backend Won't Start

**Error:** "Port 8001 already in use"

**Solution:**
```bash
# Windows
netstat -ano | findstr :8001
taskkill /PID <process-id> /F

# macOS/Linux
lsof -ti:8001 | xargs kill -9
```

**Error:** "Module not found"

**Solution:**
```bash
# Reinstall dependencies
cd booking_system_backend
pip install -r requirements.txt --force-reinstall
```

#### Frontend Won't Start

**Error:** "Port 5173 already in use"

**Solution:**
```bash
# Windows
netstat -ano | findstr :5173
taskkill /PID <process-id> /F

# macOS/Linux
lsof -ti:5173 | xargs kill -9
```

**Error:** "Cannot find module"

**Solution:**
```bash
cd booking_system_frontend
rm -rf node_modules package-lock.json
npm install
```

#### Tasks Not Appearing

**Cause:** Not logged in or wrong user

**Solution:**
```
1. Check login status (top-right corner)
2. Verify user_id in API calls matches logged-in user
3. Check browser console for errors (F12)
4. Verify backend is running (http://localhost:8001)
```

### Database Issues

#### Error: "Database is locked"

**Solution:**
```bash
# Stop all servers
# Delete database
cd booking_system_backend
rm booking_system.db

# Restart backend (will recreate database)
python server.py
```

---

## 💡 Best Practices

### For Power BI Developers

#### 1. Daily Routine

```
Morning (9:00 AM):
✅ Run refresh check
✅ Review critical tasks
✅ Plan your day

Throughout Day:
✅ Update task status as you work
✅ Create tasks for new issues
✅ Document solutions in task descriptions

End of Day (5:00 PM):
✅ Mark completed tasks
✅ Review pending items
✅ Plan tomorrow's priorities
```

#### 2. Task Organization

```
Use Categories Effectively:
- Urgent: Production issues, client emergencies
- Work: Regular development, maintenance
- Personal: Learning, skill development

Use Descriptions:
- Include error messages
- Document solutions
- Add dataset/report IDs
- Link to related resources
```

#### 3. Automation Strategy

```
Weekly Tasks (Monday):
- Performance review
- Backup reports
- Code review

Monthly Tasks (1st Monday):
- Fiscal calculations
- Connection review
- Dataset cleanup

On-Demand:
- Refresh failure checks (after deployments)
- Performance monitoring (when issues reported)
```

#### 4. Monitoring Schedule

```
Recommended Check Frequency:
- Production workspaces: Every 15 minutes
- Development workspaces: Every hour
- Test workspaces: Daily

Set up automated checks:
- Windows Task Scheduler
- Linux cron jobs
- Azure Functions (for cloud deployment)
```

### Security Best Practices

#### 1. Credential Management

```
✅ DO:
- Store credentials in .env file
- Add .env to .gitignore
- Use Azure Key Vault for production
- Rotate secrets regularly (every 6 months)

❌ DON'T:
- Commit credentials to Git
- Share credentials in emails
- Use same credentials across environments
- Store in plain text files
```

#### 2. Access Control

```
✅ DO:
- Use service principal with minimum permissions
- Grant workspace access only where needed
- Review permissions quarterly
- Use separate credentials per environment

❌ DON'T:
- Use personal account credentials
- Grant tenant-wide permissions
- Share service principal across teams
- Use admin accounts for automation
```

---

## 🎓 Advanced Topics

### Custom Automation Scripts

You can extend the automation with custom scripts:

**Example: Email Notifications**

```python
# custom_notifications.py
import smtplib
from email.mime.text import MIMEText

def send_task_notification(task):
    msg = MIMEText(f"New critical task: {task.title}")
    msg['Subject'] = 'SmartTaskHub Alert'
    msg['From'] = 'alerts@yourcompany.com'
    msg['To'] = 'you@yourcompany.com'
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your-email', 'your-password')
        server.send_message(msg)
```

**Example: Teams Integration**

```python
# teams_webhook.py
import requests

def post_to_teams(task):
    webhook_url = "your-teams-webhook-url"
    
    message = {
        "@type": "MessageCard",
        "title": "New Critical Task",
        "text": f"{task.title}\n\n{task.description}",
        "themeColor": "FF0000"
    }
    
    requests.post(webhook_url, json=message)
```

### Performance Optimization

**For Large Workspaces:**

```python
# Batch processing
def check_multiple_workspaces(workspace_ids, user_id):
    all_tasks = []
    for workspace_id in workspace_ids:
        tasks = check_refreshes(workspace_id, user_id)
        all_tasks.extend(tasks)
    return all_tasks

# Parallel processing
from concurrent.futures import ThreadPoolExecutor

def check_workspaces_parallel(workspace_ids, user_id):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(check_refreshes, ws_id, user_id)
            for ws_id in workspace_ids
        ]
        results = [f.result() for f in futures]
    return [task for tasks in results for task in tasks]
```

---

## 📞 Support & Resources

### Getting Help

1. **Documentation**
   - This guide
   - API docs: http://localhost:8001/docs
   - README.md in repository

2. **Community**
   - GitHub Issues: Report bugs or request features
   - Discussions: Ask questions, share tips

3. **Power BI Resources**
   - Power BI REST API: https://docs.microsoft.com/power-bi/developer/
   - Azure AD: https://docs.microsoft.com/azure/active-directory/

### Useful Links

- **Power BI REST API Documentation**: https://docs.microsoft.com/rest/api/power-bi/
- **Azure AD App Registration**: https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps
- **Power BI Service**: https://app.powerbi.com
- **SmartTaskHub Repository**: https://github.com/suchitraroutray/smart-task-hub

---

## 🎉 Conclusion

SmartTaskHub helps Power BI developers stay organized and proactive by:

✅ Automatically detecting and creating tasks for refresh failures
✅ Monitoring performance and alerting on slow refreshes
✅ Providing scheduled recurring tasks for routine maintenance
✅ Offering smart prioritization based on keywords and categories
✅ Tracking progress with visual status indicators

**Start using SmartTaskHub today and never miss a critical Power BI issue again!**

---

**Built with ❤️ for Power BI Developers**

*Made with Bob - Your AI-native IDE*

---

## 📝 Changelog

### Version 1.0.0 (2026-05-27)
- ✨ Initial release with Power BI automation
- ✨ Refresh failure detection
- ✨ Performance monitoring
- ✨ Scheduled recurring tasks
- ✨ Smart priority assignment
- ✨ Visual task management interface

---

## 📄 License

This project is part of the SmartTaskHub system.
See LICENSE file for details.