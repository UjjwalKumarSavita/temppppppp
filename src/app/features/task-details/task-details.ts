import { Component } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { NgIf } from '@angular/common';
import { Task } from '../../shared/models/task.model';
import { TaskService } from '../../shared/services/task';
import { PriorityBadgeComponent } from '../../components/priority-badge/priority-badge';
import { StatusBadgeComponent } from '../../components/status-badge/status-badge';

@Component({
  selector: 'app-task-details',
  standalone: true,
  imports: [NgIf, RouterLink, PriorityBadgeComponent, StatusBadgeComponent],
  templateUrl: './task-details.html',
  styleUrl: './task-details.scss'
})
export class TaskDetailsComponent {
  task: Task | null = null;

  constructor(private route: ActivatedRoute, private tasks: TaskService, private router: Router){
    const id = this.route.snapshot.paramMap.get('id')!;
    this.task = this.tasks.getById(id);
  }

  goBack() {
    this.router.navigateByUrl('/dashboard');
  }

  setStatus(s: 'pending'|'in-progress'|'completed'){
    if(!this.task) return;
    this.tasks.updateStatus(this.task.id, s);
    this.task = this.tasks.getById(this.task.id);
  }

  remove(){
    if(!this.task) return;
    this.tasks.deleteTask(this.task.id);
    this.router.navigateByUrl('/dashboard');
  }
}
