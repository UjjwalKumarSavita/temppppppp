import { Component, computed, signal } from '@angular/core';
import { NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { TaskCardComponent } from '../../components/task-card/task-card';
import { TaskService } from '../../shared/services/task';
import { StatusBadgeComponent } from '../../components/status-badge/status-badge';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [NgFor, NgIf, FormsModule, TaskCardComponent, StatusBadgeComponent],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss'
})
export class DashboardComponent {
  query = '';
  status: 'all'|'pending'|'in-progress'|'completed' = 'all';
  priority: 'all'|'low'|'medium'|'high' = 'all';

  constructor(public tasks: TaskService, private router: Router) {}

  filtered = computed(() => this.tasks.search(this.query, this.status as any, this.priority as any));
  counts = computed(() => this.tasks.counts());

  setStatusFor(id: string, s: 'pending'|'in-progress'|'completed'){ this.tasks.updateStatus(id, s); }
  remove(id: string){ this.tasks.deleteTask(id); }
  

  goBack() {
    this.router.navigateByUrl('/');
  }
}
