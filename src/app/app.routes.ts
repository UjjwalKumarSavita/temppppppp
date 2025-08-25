import { Routes } from '@angular/router';
import { TaskManagerComponent } from './features/task-manager/task-manager';
import { DashboardComponent } from './features/dashboard/dashboard';
import { TaskDetailsComponent } from './features/task-details/task-details';

export const routes: Routes = [
  { path: '', component: TaskManagerComponent, title: 'Task Manager' },
  { path: 'dashboard', component: DashboardComponent, title: 'Task Dashboard' },
  { path: 'task/:id', component: TaskDetailsComponent, title: 'Task Details' },
  { path: '**', redirectTo: '' }
];
