import pytest
from datetime import datetime
from services.task import (
    create_task,
    get_task,
    list_tasks,
    update_task,
    delete_task,
    calculate_priority,
    get_high_priority_tasks
)
from schemas import TaskCreate, TaskUpdate, ErrorResponse


def test_calculate_priority_urgent_category():
    """Test that Urgent category gets Critical priority"""
    priority = calculate_priority('Urgent', 'Regular task', 'No special keywords')
    assert priority == 'Critical'


def test_calculate_priority_work_category():
    """Test that Work category gets High priority"""
    priority = calculate_priority('Work', 'Regular task', 'No special keywords')
    assert priority == 'High'


def test_calculate_priority_personal_category():
    """Test that Personal category gets Medium priority"""
    priority = calculate_priority('Personal', 'Regular task', 'No special keywords')
    assert priority == 'Medium'


def test_calculate_priority_with_urgent_keywords():
    """Test that urgent keywords upgrade priority"""
    # Personal with urgent keyword should become High
    priority = calculate_priority('Personal', 'ASAP task', 'This is urgent')
    assert priority == 'High'


def test_create_task_success(db_session, test_user):
    """Test successful task creation"""
    task_data = TaskCreate(
        user_id=test_user.user_id,
        title='Test Task',
        description='Test description',
        category='Work'
    )
    
    result = create_task(db_session, task_data)
    
    assert not isinstance(result, ErrorResponse)
    assert result.title == 'Test Task'
    assert result.category == 'Work'
    assert result.priority == 'High'
    assert result.status == 'pending'
    assert result.user_id == test_user.user_id


def test_create_task_with_urgent_keywords(db_session, test_user):
    """Test task creation with urgent keywords upgrades priority"""
    task_data = TaskCreate(
        user_id=test_user.user_id,
        title='URGENT: Fix critical bug',
        description='This needs immediate attention',
        category='Personal'
    )
    
    result = create_task(db_session, task_data)
    
    assert not isinstance(result, ErrorResponse)
    assert result.priority == 'High'  # Upgraded from Medium


def test_create_task_nonexistent_user(db_session):
    """Test task creation with non-existent user fails"""
    task_data = TaskCreate(
        user_id=99999,
        title='Test Task',
        category='Work'
    )
    
    result = create_task(db_session, task_data)
    
    assert isinstance(result, ErrorResponse)
    assert result.error_code == 'USER_NOT_FOUND'


def test_get_task_success(db_session, test_task):
    """Test retrieving a task by ID"""
    result = get_task(db_session, test_task.task_id)
    
    assert not isinstance(result, ErrorResponse)
    assert result.task_id == test_task.task_id
    assert result.title == test_task.title


def test_get_task_not_found(db_session):
    """Test retrieving non-existent task"""
    result = get_task(db_session, 99999)
    
    assert isinstance(result, ErrorResponse)
    assert result.error_code == 'TASK_NOT_FOUND'


def test_list_tasks_all(db_session, test_user, test_task):
    """Test listing all tasks for a user"""
    # Create additional tasks
    task_data1 = TaskCreate(
        user_id=test_user.user_id,
        title='Task 2',
        category='Personal'
    )
    task_data2 = TaskCreate(
        user_id=test_user.user_id,
        title='Task 3',
        category='Urgent'
    )
    
    create_task(db_session, task_data1)
    create_task(db_session, task_data2)
    
    tasks = list_tasks(db_session, user_id=test_user.user_id)
    
    assert len(tasks) >= 3
    assert all(t.user_id == test_user.user_id for t in tasks)


def test_list_tasks_filter_by_category(db_session, test_user):
    """Test filtering tasks by category"""
    # Create tasks with different categories
    for category in ['Work', 'Personal', 'Urgent']:
        task_data = TaskCreate(
            user_id=test_user.user_id,
            title=f'{category} Task',
            category=category
        )
        create_task(db_session, task_data)
    
    work_tasks = list_tasks(db_session, user_id=test_user.user_id, category='Work')
    
    assert len(work_tasks) >= 1
    assert all(t.category == 'Work' for t in work_tasks)


def test_list_tasks_filter_by_priority(db_session, test_user):
    """Test filtering tasks by priority"""
    # Create tasks with different priorities
    task_data = TaskCreate(
        user_id=test_user.user_id,
        title='Critical Task',
        category='Urgent'
    )
    create_task(db_session, task_data)
    
    critical_tasks = list_tasks(db_session, user_id=test_user.user_id, priority='Critical')
    
    assert len(critical_tasks) >= 1
    assert all(t.priority == 'Critical' for t in critical_tasks)


def test_list_tasks_filter_by_status(db_session, test_user, test_task):
    """Test filtering tasks by status"""
    pending_tasks = list_tasks(db_session, user_id=test_user.user_id, status='pending')
    
    assert len(pending_tasks) >= 1
    assert all(t.status == 'pending' for t in pending_tasks)


def test_update_task_title(db_session, test_task):
    """Test updating task title"""
    update_data = TaskUpdate(title='Updated Title')
    
    result = update_task(db_session, test_task.task_id, update_data)
    
    assert not isinstance(result, ErrorResponse)
    assert result.title == 'Updated Title'
    assert result.task_id == test_task.task_id


def test_update_task_status(db_session, test_task):
    """Test updating task status"""
    update_data = TaskUpdate(status='in_progress')
    
    result = update_task(db_session, test_task.task_id, update_data)
    
    assert not isinstance(result, ErrorResponse)
    assert result.status == 'in_progress'


def test_update_task_category_recalculates_priority(db_session, test_task):
    """Test that changing category recalculates priority"""
    # Original task is Work (High priority)
    update_data = TaskUpdate(category='Urgent')
    
    result = update_task(db_session, test_task.task_id, update_data)
    
    assert not isinstance(result, ErrorResponse)
    assert result.category == 'Urgent'
    assert result.priority == 'Critical'  # Recalculated


def test_update_task_not_found(db_session):
    """Test updating non-existent task"""
    update_data = TaskUpdate(title='New Title')
    
    result = update_task(db_session, 99999, update_data)
    
    assert isinstance(result, ErrorResponse)
    assert result.error_code == 'TASK_NOT_FOUND'


def test_delete_task_success(db_session, test_task):
    """Test successful task deletion"""
    result = delete_task(db_session, test_task.task_id)
    
    assert not isinstance(result, ErrorResponse)
    assert result['success'] is True
    
    # Verify task is deleted
    get_result = get_task(db_session, test_task.task_id)
    assert isinstance(get_result, ErrorResponse)


def test_delete_task_not_found(db_session):
    """Test deleting non-existent task"""
    result = delete_task(db_session, 99999)
    
    assert isinstance(result, ErrorResponse)
    assert result.error_code == 'TASK_NOT_FOUND'


def test_get_high_priority_tasks(db_session, test_user):
    """Test getting high priority tasks"""
    # Create tasks with different priorities
    for category in ['Work', 'Personal', 'Urgent']:
        task_data = TaskCreate(
            user_id=test_user.user_id,
            title=f'{category} Task',
            category=category
        )
        create_task(db_session, task_data)
    
    high_priority_tasks = get_high_priority_tasks(db_session, test_user.user_id)
    
    # Should include Work (High) and Urgent (Critical), but not Personal (Medium)
    assert len(high_priority_tasks) >= 2
    assert all(t.priority in ['High', 'Critical'] for t in high_priority_tasks)
    assert all(t.status != 'completed' for t in high_priority_tasks)


def test_get_high_priority_tasks_excludes_completed(db_session, test_user):
    """Test that completed high priority tasks are excluded"""
    # Create a high priority task
    task_data = TaskCreate(
        user_id=test_user.user_id,
        title='High Priority Task',
        category='Work'
    )
    result = create_task(db_session, task_data)
    
    # Mark it as completed
    update_task(db_session, result.task_id, TaskUpdate(status='completed'))
    
    high_priority_tasks = get_high_priority_tasks(db_session, test_user.user_id)
    
    # Completed task should not be in the list
    assert not any(t.task_id == result.task_id for t in high_priority_tasks)

# Made with Bob
