import { Injectable, signal } from '@angular/core';
import { CsvStorageService } from './csv-storage';
import { Task, TaskPriority, TaskStatus } from '../models/task.model';

@Injectable({ providedIn: 'root' })
export class TaskService {
  // Use Angular signals for simple reactivity
  tasks = signal<Task[]>([]);

  constructor(private store: CsvStorageService) {
    this.tasks.set(this.store.readTasks());
  }

  private now() { return new Date().toISOString(); }
  private genId() { return 't_' + Math.random().toString(36).slice(2, 8) + Date.now().toString(36); }

  addTask(input: { title: string; description: string; dueDate: string; priority: TaskPriority; }): Task {
    const task: Task = {
      id: this.genId(),
      title: input.title.trim(),
      description: input.description.trim(),
      dueDate: input.dueDate,
      priority: input.priority,
      status: 'pending',
      createdAt: this.now(),
      updatedAt: this.now(),
    };
    const next = [task, ...this.tasks()];
    this.tasks.set(next);
    this.store.writeTasks(next, true);          // persist & download CSV on create
    return task;
  }

  updateTask(id: string, patch: Partial<Omit<Task, 'id' | 'createdAt'>>): void {
    const next = this.tasks().map(t => t.id === id ? { ...t, ...patch, updatedAt: this.now() } : t);
    this.tasks.set(next);
    this.store.writeTasks(next);
  }

  updateStatus(id: string, status: TaskStatus){ this.updateTask(id, { status }); }
  deleteTask(id: string){
    const next = this.tasks().filter(t => t.id !== id);
    this.tasks.set(next);
    this.store.writeTasks(next);
  }

  getById(id: string){ return this.tasks().find(t => t.id === id) || null; }

  counts(){
    const all = this.tasks();
    return {
      total: all.length,
      pending: all.filter(t => t.status === 'pending').length,
      inProgress: all.filter(t => t.status === 'in-progress').length,
      completed: all.filter(t => t.status === 'completed').length,
      dueToday: all.filter(t => t.dueDate === new Date().toISOString().slice(0,10)).length,
    };
  }

  search(query: string, status: 'all' | TaskStatus, prio: 'all' | TaskPriority): Task[] {
    const q = query.trim().toLowerCase();
    return this.tasks().filter(t => {
      const matchesQ = !q || [t.title, t.description].some(s => s.toLowerCase().includes(q));
      const matchesS = status === 'all' || t.status === status;
      const matchesP = prio === 'all' || t.priority === prio;
      return matchesQ && matchesS && matchesP;
    });
  }
}
