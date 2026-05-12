from sqlalchemy.orm import Session
from typing import Union, Optional, List
from datetime import datetime
from models import Task, User
from schemas import TaskOut, TaskCreate, TaskUpdate, ErrorResponse


def calculate_priority(category: str, title: str = "", description: str = "") -> str:
    """
    Calculate task priority based on category and keywords.
    
    Rules:
    - Urgent category → Critical priority
    - Work category → High priority
    - Personal category → Medium priority
    - Keywords like 'asap', 'urgent', 'critical' → Upgrade priority
    """
    # Base priority from category
    priority_map = {
        'Urgent': 'Critical',
        'Work': 'High',
        'Personal': 'Medium'
    }
    
    base_priority = priority_map.get(category, 'Low')
    
    # Check for urgent keywords in title/description
    urgent_keywords = ['asap', 'urgent', 'critical', 'emergency', 'immediate', 'now']
    text = f"{title} {description}".lower()
    
    has_urgent_keyword = any(keyword in text for keyword in urgent_keywords)
    
    if has_urgent_keyword:
        # Upgrade priority if urgent keywords found
        if base_priority == 'Medium':
            return 'High'
        elif base_priority == 'Low':
            return 'Medium'
    
    return base_priority


def create_task(db: Session, task_data: TaskCreate) -> Union[TaskOut, ErrorResponse]:
    """Create a new task with auto-calculated priority."""
    try:
        # Verify user exists
        user = db.query(User).filter(User.user_id == task_data.user_id).first()
        if not user:
            return ErrorResponse(
                error="User not found",
                error_code="USER_NOT_FOUND",
                details=f"No user found with ID {task_data.user_id}"
            )
        
        # Calculate priority
        priority = calculate_priority(
            task_data.category,
            task_data.title,
            task_data.description or ""
        )
        
        # Create task
        now = datetime.utcnow().isoformat()
        task = Task(
            user_id=task_data.user_id,
            title=task_data.title,
            description=task_data.description,
            category=task_data.category,
            priority=priority,
            status='pending',
            created_at=now,
            updated_at=now
        )
        
        db.add(task)
        db.commit()
        db.refresh(task)
        
        return TaskOut.model_validate(task)
    
    except Exception as e:
        db.rollback()
        return ErrorResponse(
            error="Failed to create task",
            error_code="TASK_CREATE_ERROR",
            details=str(e)
        )


def get_task(db: Session, task_id: int) -> Union[TaskOut, ErrorResponse]:
    """Get a specific task by ID."""
    task = db.query(Task).filter(Task.task_id == task_id).first()
    
    if not task:
        return ErrorResponse(
            error="Task not found",
            error_code="TASK_NOT_FOUND",
            details=f"No task found with ID {task_id}"
        )
    
    return TaskOut.model_validate(task)


def list_tasks(
    db: Session,
    user_id: Optional[int] = None,
    category: Optional[str] = None,
    priority: Optional[str] = None,
    status: Optional[str] = None
) -> List[TaskOut]:
    """List tasks with optional filters."""
    query = db.query(Task)
    
    if user_id:
        query = query.filter(Task.user_id == user_id)
    if category:
        query = query.filter(Task.category == category)
    if priority:
        query = query.filter(Task.priority == priority)
    if status:
        query = query.filter(Task.status == status)
    
    # Order by priority (Critical > High > Medium > Low) and creation date
    priority_order = {
        'Critical': 0,
        'High': 1,
        'Medium': 2,
        'Low': 3
    }
    
    tasks = query.all()
    tasks.sort(key=lambda t: (priority_order.get(t.priority, 4), t.created_at))
    
    return [TaskOut.model_validate(task) for task in tasks]


def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> Union[TaskOut, ErrorResponse]:
    """Update an existing task."""
    try:
        task = db.query(Task).filter(Task.task_id == task_id).first()
        
        if not task:
            return ErrorResponse(
                error="Task not found",
                error_code="TASK_NOT_FOUND",
                details=f"No task found with ID {task_id}"
            )
        
        # Update fields if provided
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.status is not None:
            task.status = task_data.status
        
        # If category changed, recalculate priority
        if task_data.category is not None:
            task.category = task_data.category
            task.priority = calculate_priority(
                task.category,
                task.title,
                task.description or ""
            )
        
        task.updated_at = datetime.utcnow().isoformat()
        
        db.commit()
        db.refresh(task)
        
        return TaskOut.model_validate(task)
    
    except Exception as e:
        db.rollback()
        return ErrorResponse(
            error="Failed to update task",
            error_code="TASK_UPDATE_ERROR",
            details=str(e)
        )


def delete_task(db: Session, task_id: int) -> Union[dict, ErrorResponse]:
    """Delete a task."""
    try:
        task = db.query(Task).filter(Task.task_id == task_id).first()
        
        if not task:
            return ErrorResponse(
                error="Task not found",
                error_code="TASK_NOT_FOUND",
                details=f"No task found with ID {task_id}"
            )
        
        db.delete(task)
        db.commit()
        
        return {"success": True, "message": "Task deleted successfully"}
    
    except Exception as e:
        db.rollback()
        return ErrorResponse(
            error="Failed to delete task",
            error_code="TASK_DELETE_ERROR",
            details=str(e)
        )


def get_high_priority_tasks(db: Session, user_id: int) -> List[TaskOut]:
    """Get all high and critical priority tasks for a user."""
    tasks = db.query(Task).filter(
        Task.user_id == user_id,
        Task.priority.in_(['High', 'Critical']),
        Task.status != 'completed'
    ).all()
    
    return [TaskOut.model_validate(task) for task in tasks]

# Made with Bob
