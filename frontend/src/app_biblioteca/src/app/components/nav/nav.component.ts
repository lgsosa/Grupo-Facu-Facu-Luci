import { Component } from '@angular/core';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.scss'
})
export class NavComponent {

  constructor(private authService: AuthService) {}

  get isToken() {
    return !!localStorage.getItem('token');
  }

  get isAdminOrLibrarian() {
    return this.authService.isAdminOrLibrarian();
  }

  cerrarSesion() {
    this.authService.logout();
  }
}
import { Component } from '@angular/core';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.scss'
})
export class NavComponent {

  constructor(private authService: AuthService) {}

  get isToken() {
    return !!localStorage.getItem('token');
  }

  get isAdminOrLibrarian() {
    return this.authService.isAdminOrLibrarian();
  }

  cerrarSesion() {
    this.authService.logout();
  }
}
