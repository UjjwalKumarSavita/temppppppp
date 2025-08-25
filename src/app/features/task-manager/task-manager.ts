import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink, Router } from '@angular/router';
import { TaskPriority } from '../../shared/models/task.model';
import { TaskService } from '../../shared/services/task';

@Component({
  selector: 'app-task-manager',
  standalone: true,
  imports: [FormsModule, RouterLink],
  templateUrl: './task-manager.html',
  styleUrl: './task-manager.scss'
})
export class TaskManagerComponent {
  title = '';
  description = '';
  dueDate = '';
  priority: TaskPriority = 'medium';

  constructor(private tasks: TaskService, private router: Router) {}

  create(){
    if(!this.title.trim() || !this.dueDate){ return; }
    this.tasks.addTask({ title: this.title, description: this.description, dueDate: this.dueDate, priority: this.priority });
    // Clear inputs and go to dashboard
    this.title = this.description = ''; this.priority = 'medium'; this.dueDate = '';
    this.router.navigateByUrl('/dashboard');
  }
}
