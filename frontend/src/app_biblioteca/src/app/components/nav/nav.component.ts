import { Component } from '@angular/core';
import { AuthService } from '../../service/auth.service';
import {RoleGuard} from "../../guards/role.guard"

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.scss'
})
export class NavComponent {

  constructor(private authService: AuthService,
    private roleguard:RoleGuard
  ) {}


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
