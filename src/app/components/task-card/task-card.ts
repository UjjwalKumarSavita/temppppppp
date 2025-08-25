import { Component, Input, Output, EventEmitter } from '@angular/core';
import { RouterLink } from '@angular/router';
import { Task } from '../../shared/models/task.model';
import { PriorityBadgeComponent } from '../priority-badge/priority-badge';
import { StatusBadgeComponent } from '../status-badge/status-badge';

@Component({
  selector: 'app-task-card',
  standalone: true,
  imports: [RouterLink, PriorityBadgeComponent, StatusBadgeComponent],
  templateUrl: './task-card.html',
  styleUrl: './task-card.scss'
})
export class TaskCardComponent {
  @Input() task!: Task;
  @Output() setStatus = new EventEmitter<'pending'|'in-progress'|'completed'>();
  @Output() remove = new EventEmitter<void>();
}
