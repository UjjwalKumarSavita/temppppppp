import { Component } from '@angular/core';
import { RouterLink, Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './navbar.html',
  styleUrl: './navbar.scss'
})
export class NavbarComponent {
  constructor( private router: Router) {}
  goHome(){ this.router.navigateByUrl('/'); }
  goDash(){ this.router.navigateByUrl('/dashboard'); }
}
