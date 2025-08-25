import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-priority-badge',
  standalone: true,
  template: `<span class="badge dot" [@ngStyle]="{'--c': color}" [class.p]="true">{{label}}</span>`,
  styleUrl: './priority-badge.scss'
})
export class PriorityBadgeComponent {
  @Input() priority: 'low'|'medium'|'high' = 'medium';
  get label(){ return this.priority; }
  get color(){
    switch(this.priority){
      case 'high': return '#ff6b6b';
      case 'medium': return '#fbbf24';
      default: return '#8bffdc';
    }
  }
}
