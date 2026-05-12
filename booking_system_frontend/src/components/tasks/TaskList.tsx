import { useState } from 'react';
import { Filter } from 'lucide-react';
import { Task, TaskCategory, TaskPriority, TaskStatus } from '../../types';
import { TaskCard } from './TaskCard';

interface TaskListProps {
  tasks: Task[];
  onUpdate: (taskId: number, status: TaskStatus) => void;
  onEdit: (task: Task) => void;
  onDelete: (taskId: number) => void;
}

const categories: (TaskCategory | 'All')[] = ['All', 'Work', 'Personal', 'Urgent'];
const priorities: (TaskPriority | 'All')[] = ['All', 'Critical', 'High', 'Medium', 'Low'];
const statuses: (TaskStatus | 'All')[] = ['All', 'pending', 'in_progress', 'completed'];

export function TaskList({ tasks, onUpdate, onEdit, onDelete }: TaskListProps) {
  const [categoryFilter, setCategoryFilter] = useState<TaskCategory | 'All'>('All');
  const [priorityFilter, setPriorityFilter] = useState<TaskPriority | 'All'>('All');
  const [statusFilter, setStatusFilter] = useState<TaskStatus | 'All'>('All');
  const [showFilters, setShowFilters] = useState(false);

  // Filter tasks based on selected filters
  const filteredTasks = tasks.filter((task) => {
    if (categoryFilter !== 'All' && task.category !== categoryFilter) return false;
    if (priorityFilter !== 'All' && task.priority !== priorityFilter) return false;
    if (statusFilter !== 'All' && task.status !== statusFilter) return false;
    return true;
  });

  const clearFilters = () => {
    setCategoryFilter('All');
    setPriorityFilter('All');
    setStatusFilter('All');
  };

  const hasActiveFilters = categoryFilter !== 'All' || priorityFilter !== 'All' || statusFilter !== 'All';

  return (
    <div className="space-y-4">
      {/* Filter Toggle and Controls */}
      <div className="bg-gray-800 rounded-lg p-4">
        <div className="flex items-center justify-between mb-4">
          <button
            onClick={() => setShowFilters(!showFilters)}
            className="flex items-center gap-2 text-white hover:text-purple-400 transition-colors"
          >
            <Filter className="w-5 h-5" />
            <span className="font-medium">Filters</span>
            {hasActiveFilters && (
              <span className="bg-purple-500 text-white text-xs px-2 py-1 rounded-full">
                Active
              </span>
            )}
          </button>
          {hasActiveFilters && (
            <button
              onClick={clearFilters}
              className="text-sm text-gray-400 hover:text-white transition-colors"
            >
              Clear All
            </button>
          )}
        </div>

        {/* Filter Options */}
        {showFilters && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Category Filter */}
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-2">
                Category
              </label>
              <select
                value={categoryFilter}
                onChange={(e) => setCategoryFilter(e.target.value as TaskCategory | 'All')}
                className="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white text-sm focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                {categories.map((cat) => (
                  <option key={cat} value={cat}>
                    {cat}
                  </option>
                ))}
              </select>
            </div>

            {/* Priority Filter */}
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-2">
                Priority
              </label>
              <select
                value={priorityFilter}
                onChange={(e) => setPriorityFilter(e.target.value as TaskPriority | 'All')}
                className="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white text-sm focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                {priorities.map((priority) => (
                  <option key={priority} value={priority}>
                    {priority}
                  </option>
                ))}
              </select>
            </div>

            {/* Status Filter */}
            <div>
              <label className="block text-sm font-medium text-gray-300 mb-2">
                Status
              </label>
              <select
                value={statusFilter}
                onChange={(e) => setStatusFilter(e.target.value as TaskStatus | 'All')}
                className="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white text-sm focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                {statuses.map((status) => (
                  <option key={status} value={status}>
                    {status === 'All' ? 'All' : status.replace('_', ' ').charAt(0).toUpperCase() + status.slice(1).replace('_', ' ')}
                  </option>
                ))}
              </select>
            </div>
          </div>
        )}
      </div>

      {/* Task Count */}
      <div className="text-gray-400 text-sm">
        Showing {filteredTasks.length} of {tasks.length} tasks
      </div>

      {/* Task Grid */}
      {filteredTasks.length === 0 ? (
        <div className="bg-gray-800 rounded-lg p-12 text-center">
          <p className="text-gray-400 text-lg">
            {tasks.length === 0 ? 'No tasks yet. Create your first task!' : 'No tasks match the selected filters.'}
          </p>
          {hasActiveFilters && tasks.length > 0 && (
            <button
              onClick={clearFilters}
              className="mt-4 text-purple-400 hover:text-purple-300 transition-colors"
            >
              Clear filters to see all tasks
            </button>
          )}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredTasks.map((task) => (
            <TaskCard
              key={task.task_id}
              task={task}
              onUpdate={onUpdate}
              onEdit={onEdit}
              onDelete={onDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}

// Made with Bob
