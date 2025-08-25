export type TaskPriority = 'low' | 'medium' | 'high';
export type TaskStatus   = 'pending' | 'in-progress' | 'completed';

export interface Task {
  id: string;
  title: string;
  description: string;
  dueDate: string;        // ISO date string (yyyy-mm-dd)
  priority: TaskPriority;
  status: TaskStatus;

  createdAt: string;      // ISO datetime
  updatedAt: string;      // ISO datetime
}
