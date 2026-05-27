"""
Power BI Monitoring Service
Monitors Power BI workspace for refresh failures and automatically creates tasks
"""

from sqlalchemy.orm import Session
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import requests
from models import Task, User
from schemas import TaskOut, ErrorResponse
import os


class PowerBIMonitor:
    """Monitor Power BI workspace and auto-create tasks for issues"""
    
    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expiry = None
        
    def get_access_token(self) -> str:
        """Get Azure AD access token for Power BI API"""
        # Check if token is still valid
        if self.access_token and self.token_expiry and datetime.utcnow() < self.token_expiry:
            return self.access_token
            
        # Get new token
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://analysis.windows.net/powerbi/api/.default'
        }
        
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            token_data = response.json()
            
            self.access_token = token_data['access_token']
            # Token expires in 3600 seconds, refresh 5 minutes before
            self.token_expiry = datetime.utcnow() + timedelta(seconds=3300)
            
            return self.access_token
        except Exception as e:
            print(f"Error getting access token: {e}")
            return None
    
    def get_datasets(self, workspace_id: str) -> List[Dict]:
        """Get all datasets in a workspace"""
        token = self.get_access_token()
        if not token:
            return []
            
        url = f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets"
        headers = {'Authorization': f'Bearer {token}'}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json().get('value', [])
        except Exception as e:
            print(f"Error getting datasets: {e}")
            return []
    
    def get_refresh_history(self, workspace_id: str, dataset_id: str, top: int = 5) -> List[Dict]:
        """Get refresh history for a dataset"""
        token = self.get_access_token()
        if not token:
            return []
            
        url = f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets/{dataset_id}/refreshes?$top={top}"
        headers = {'Authorization': f'Bearer {token}'}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json().get('value', [])
        except Exception as e:
            print(f"Error getting refresh history: {e}")
            return []
    
    def check_refresh_failures(self, db: Session, workspace_id: str, user_id: int) -> List[TaskOut]:
        """Check for refresh failures and create tasks"""
        created_tasks = []
        
        # Get all datasets
        datasets = self.get_datasets(workspace_id)
        
        for dataset in datasets:
            dataset_id = dataset.get('id')
            dataset_name = dataset.get('name')
            
            # Get refresh history
            refreshes = self.get_refresh_history(workspace_id, dataset_id, top=1)
            
            if not refreshes:
                continue
                
            latest_refresh = refreshes[0]
            status = latest_refresh.get('status')
            
            # Check if refresh failed
            if status == 'Failed':
                # Check if task already exists for this failure
                existing_task = db.query(Task).filter(
                    Task.user_id == user_id,
                    Task.title.contains(f"Dataset '{dataset_name}' refresh failed"),
                    Task.status != 'completed'
                ).first()
                
                if not existing_task:
                    # Create task for refresh failure
                    error_message = latest_refresh.get('serviceExceptionJson', 'Unknown error')
                    end_time = latest_refresh.get('endTime', 'Unknown')
                    
                    now = datetime.utcnow().isoformat()
                    task = Task(
                        user_id=user_id,
                        title=f"URGENT: Dataset '{dataset_name}' refresh failed",
                        description=f"Refresh failed at {end_time}\nError: {error_message}\nDataset ID: {dataset_id}",
                        category='Urgent',
                        priority='Critical',
                        status='pending',
                        created_at=now,
                        updated_at=now
                    )
                    
                    db.add(task)
                    db.commit()
                    db.refresh(task)
                    
                    created_tasks.append(TaskOut.model_validate(task))
        
        return created_tasks
    
    def check_slow_refreshes(self, db: Session, workspace_id: str, user_id: int, threshold_minutes: int = 30) -> List[TaskOut]:
        """Check for slow refreshes and create tasks"""
        created_tasks = []
        
        datasets = self.get_datasets(workspace_id)
        
        for dataset in datasets:
            dataset_id = dataset.get('id')
            dataset_name = dataset.get('name')
            
            refreshes = self.get_refresh_history(workspace_id, dataset_id, top=1)
            
            if not refreshes:
                continue
                
            latest_refresh = refreshes[0]
            status = latest_refresh.get('status')
            
            if status == 'Completed':
                start_time = datetime.fromisoformat(latest_refresh.get('startTime').replace('Z', '+00:00'))
                end_time = datetime.fromisoformat(latest_refresh.get('endTime').replace('Z', '+00:00'))
                duration = (end_time - start_time).total_seconds() / 60  # minutes
                
                if duration > threshold_minutes:
                    # Check if task already exists
                    existing_task = db.query(Task).filter(
                        Task.user_id == user_id,
                        Task.title.contains(f"Dataset '{dataset_name}' refresh is slow"),
                        Task.status != 'completed'
                    ).first()
                    
                    if not existing_task:
                        now = datetime.utcnow().isoformat()
                        task = Task(
                            user_id=user_id,
                            title=f"Dataset '{dataset_name}' refresh is slow",
                            description=f"Refresh took {duration:.1f} minutes (threshold: {threshold_minutes} minutes)\nConsider optimizing the dataset or queries.\nDataset ID: {dataset_id}",
                            category='Work',
                            priority='High',
                            status='pending',
                            created_at=now,
                            updated_at=now
                        )
                        
                        db.add(task)
                        db.commit()
                        db.refresh(task)
                        
                        created_tasks.append(TaskOut.model_validate(task))
        
        return created_tasks


def create_scheduled_task(db: Session, user_id: int, title: str, description: str, category: str) -> TaskOut:
    """Create a scheduled recurring task"""
    from services.task import calculate_priority
    
    priority = calculate_priority(category, title, description)
    now = datetime.utcnow().isoformat()
    
    task = Task(
        user_id=user_id,
        title=title,
        description=description,
        category=category,
        priority=priority,
        status='pending',
        created_at=now,
        updated_at=now
    )
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return TaskOut.model_validate(task)


def create_weekly_tasks(db: Session, user_id: int) -> List[TaskOut]:
    """Create weekly recurring tasks for Power BI developers"""
    weekly_tasks = [
        {
            'title': 'Weekly: Review dashboard performance metrics',
            'description': 'Check load times, query performance, and user feedback for all dashboards',
            'category': 'Work'
        },
        {
            'title': 'Weekly: Backup Power BI reports',
            'description': 'Export PBIX files and save to backup location',
            'category': 'Work'
        },
        {
            'title': 'Weekly: Review team DAX code',
            'description': 'Code review for best practices and performance optimization',
            'category': 'Work'
        }
    ]
    
    created_tasks = []
    for task_data in weekly_tasks:
        task = create_scheduled_task(db, user_id, **task_data)
        created_tasks.append(task)
    
    return created_tasks


def create_monthly_tasks(db: Session, user_id: int) -> List[TaskOut]:
    """Create monthly recurring tasks for Power BI developers"""
    monthly_tasks = [
        {
            'title': 'Monthly: Update fiscal year calculations',
            'description': 'Review and update fiscal calendar, YTD, and QTD calculations',
            'category': 'Work'
        },
        {
            'title': 'Monthly: Review data source connections',
            'description': 'Verify all data sources are connected and credentials are valid',
            'category': 'Work'
        },
        {
            'title': 'Monthly: Clean up unused datasets',
            'description': 'Archive or delete datasets that are no longer in use',
            'category': 'Work'
        }
    ]
    
    created_tasks = []
    for task_data in monthly_tasks:
        task = create_scheduled_task(db, user_id, **task_data)
        created_tasks.append(task)
    
    return created_tasks


# Made with Bob - Power BI Automation for Developers