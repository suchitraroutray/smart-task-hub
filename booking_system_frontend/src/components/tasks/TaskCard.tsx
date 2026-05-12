import { useState } from 'react';
import { Trash2, Edit2, CheckCircle, Circle, Clock } from 'lucide-react';
import { Task, TaskStatus } from '../../types';
import { Card } from '../common/Card';
import { Button } from '../common/Button';

interface TaskCardProps {
  task: Task;
  onUpdate: (taskId: number, status: TaskStatus) => void;
  onEdit: (task: Task) => void;
  onDelete: (taskId: number) => void;
}

// Category color mapping
const categoryColors = {
  Work: 'bg-blue-500',
  Personal: 'bg-green-500',
  Urgent: 'bg-red-500',
};

// Priority color mapping
const priorityColors = {
  Low: 'text-gray-500',
  Medium: 'text-yellow-500',
  High: 'text-orange-500',
  Critical: 'text-red-600',
};

// Status icon mapping
const statusIcons = {
  pending: Circle,
  in_progress: Clock,
  completed: CheckCircle,
};

// Status color mapping
const statusColors = {
  pending: 'text-gray-400',
  in_progress: 'text-blue-500',
  completed: 'text-green-500',
};

export function TaskCard({ task, onUpdate, onEdit, onDelete }: TaskCardProps) {
  const [isDeleting, setIsDeleting] = useState(false);

  const handleStatusToggle = () => {
    const statusFlow: Record<TaskStatus, TaskStatus> = {
      pending: 'in_progress',
      in_progress: 'completed',
      completed: 'pending',
    };
    onUpdate(task.task_id, statusFlow[task.status]);
  };

  const handleDelete = async () => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      setIsDeleting(true);
      try {
        await onDelete(task.task_id);
      } catch (error) {
        setIsDeleting(false);
      }
    }
  };

  const StatusIcon = statusIcons[task.status];

  return (
    <Card className="hover:shadow-lg transition-shadow">
      <div className="space-y-3">
        {/* Header with category badge and priority */}
        <div className="flex items-start justify-between">
          <div className="flex items-center gap-2">
            <span
              className={`${categoryColors[task.category]} text-white text-xs font-semibold px-2 py-1 rounded`}
            >
              {task.category}
            </span>
            <span className={`${priorityColors[task.priority]} text-sm font-medium`}>
              {task.priority}
            </span>
          </div>
          <button
            onClick={handleStatusToggle}
            className={`${statusColors[task.status]} hover:opacity-70 transition-opacity`}
            title={`Status: ${task.status.replace('_', ' ')}`}
          >
            <StatusIcon className="w-6 h-6" />
          </button>
        </div>

        {/* Title */}
        <h3 className="text-lg font-semibold text-white">{task.title}</h3>

        {/* Description */}
        {task.description && (
          <p className="text-gray-300 text-sm line-clamp-2">{task.description}</p>
        )}

        {/* Status badge */}
        <div className="flex items-center gap-2">
          <span className="text-xs text-gray-400">
            Status: <span className="capitalize">{task.status.replace('_', ' ')}</span>
          </span>
        </div>

        {/* Timestamps */}
        <div className="text-xs text-gray-500 space-y-1">
          <div>Created: {new Date(task.created_at).toLocaleDateString()}</div>
          {task.updated_at !== task.created_at && (
            <div>Updated: {new Date(task.updated_at).toLocaleDateString()}</div>
          )}
        </div>

        {/* Actions */}
        <div className="flex gap-2 pt-2 border-t border-gray-700">
          <Button
            variant="secondary"
            size="sm"
            onClick={() => onEdit(task)}
            className="flex-1"
          >
            <Edit2 className="w-4 h-4 mr-1" />
            Edit
          </Button>
          <Button
            variant="secondary"
            size="sm"
            onClick={handleDelete}
            disabled={isDeleting}
            className="flex-1 hover:bg-red-600 hover:text-white"
          >
            <Trash2 className="w-4 h-4 mr-1" />
            {isDeleting ? 'Deleting...' : 'Delete'}
          </Button>
        </div>
      </div>
    </Card>
  );
}

// Made with Bob
