import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-status-badge',
  standalone: true,
  template: `<span class="badge dot" [@ngStyle]="{'--c': color}">{{status}}</span>`,
  styleUrl: './status-badge.scss'
})
export class StatusBadgeComponent {
  @Input() status: 'pending'|'in-progress'|'completed' = 'pending';
  get color(){
    switch(this.status){
      case 'completed': return '#4ade80';
      case 'in-progress': return '#6bc2ff';
      default: return '#9fb0c0';
    }
  }
}
