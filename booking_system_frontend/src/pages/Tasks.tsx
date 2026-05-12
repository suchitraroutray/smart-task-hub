import { useState, useEffect } from 'react';
import { Plus } from 'lucide-react';
import toast from 'react-hot-toast';
import { Task, TaskCreate, TaskUpdate, TaskStatus } from '../types';
import { getTasks, createTask, updateTask, deleteTask } from '../services/api';
import { useUser } from '../hooks/useUser';
import { Button } from '../components/common/Button';
import { LoadingSpinner } from '../components/common/LoadingSpinner';
import { TaskList } from '../components/tasks/TaskList';
import { TaskForm } from '../components/tasks/TaskForm';

export function Tasks() {
  const { user } = useUser();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [editingTask, setEditingTask] = useState<Task | undefined>(undefined);

  // Load tasks on mount and when user changes
  useEffect(() => {
    if (user) {
      loadTasks();
    }
  }, [user]);

  const loadTasks = async () => {
    if (!user) return;

    try {
      setLoading(true);
      const data = await getTasks(user.user_id);
      setTasks(data);
    } catch (error) {
      console.error('Failed to load tasks:', error);
      toast.error('Failed to load tasks');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (data: TaskCreate | TaskUpdate) => {
    if (!user) return;

    try {
      const result = await createTask(data as TaskCreate);
      
      if ('success' in result && result.success === false) {
        toast.error(result.error);
        return;
      }

      setTasks([...tasks, result as Task]);
      setShowForm(false);
      toast.success('Task created successfully!');
    } catch (error) {
      console.error('Failed to create task:', error);
      toast.error('Failed to create task');
      throw error;
    }
  };

  const handleUpdateTask = async (data: TaskCreate | TaskUpdate) => {
    if (!editingTask) return;

    try {
      const result = await updateTask(editingTask.task_id, data as TaskUpdate);
      
      if ('success' in result && result.success === false) {
        toast.error(result.error);
        return;
      }

      setTasks(tasks.map(t => t.task_id === editingTask.task_id ? result as Task : t));
      setEditingTask(undefined);
      setShowForm(false);
      toast.success('Task updated successfully!');
    } catch (error) {
      console.error('Failed to update task:', error);
      toast.error('Failed to update task');
      throw error;
    }
  };

  const handleStatusUpdate = async (taskId: number, status: TaskStatus) => {
    try {
      const result = await updateTask(taskId, { status });
      
      if ('success' in result && result.success === false) {
        toast.error(result.error);
        return;
      }

      setTasks(tasks.map(t => t.task_id === taskId ? result as Task : t));
      toast.success(`Task marked as ${status.replace('_', ' ')}`);
    } catch (error) {
      console.error('Failed to update task status:', error);
      toast.error('Failed to update task status');
    }
  };

  const handleEditTask = (task: Task) => {
    setEditingTask(task);
    setShowForm(true);
  };

  const handleDeleteTask = async (taskId: number) => {
    try {
      const result = await deleteTask(taskId);
      
      if ('success' in result && result.success === false) {
        toast.error(result.error);
        return;
      }

      setTasks(tasks.filter(t => t.task_id !== taskId));
      toast.success('Task deleted successfully!');
    } catch (error) {
      console.error('Failed to delete task:', error);
      toast.error('Failed to delete task');
    }
  };

  const handleCancelForm = () => {
    setShowForm(false);
    setEditingTask(undefined);
  };

  if (!user) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-white mb-4">Please log in</h2>
          <p className="text-gray-400">You need to be logged in to manage tasks</p>
        </div>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  return (
    <div className="min-h-screen py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">My Tasks</h1>
          <p className="text-gray-400">
            Organize and manage your tasks with smart priority assignment
          </p>
        </div>

        {/* Create Task Button */}
        {!showForm && (
          <div className="mb-6">
            <Button
              onClick={() => setShowForm(true)}
              variant="primary"
              className="flex items-center gap-2"
            >
              <Plus className="w-5 h-5" />
              Create New Task
            </Button>
          </div>
        )}

        {/* Task Form */}
        {showForm && (
          <div className="mb-6">
            <TaskForm
              task={editingTask}
              userId={user.user_id}
              onSubmit={editingTask ? handleUpdateTask : handleCreateTask}
              onCancel={handleCancelForm}
            />
          </div>
        )}

        {/* Task List */}
        <TaskList
          tasks={tasks}
          onUpdate={handleStatusUpdate}
          onEdit={handleEditTask}
          onDelete={handleDeleteTask}
        />
      </div>
    </div>
  );
}

// Made with Bob
