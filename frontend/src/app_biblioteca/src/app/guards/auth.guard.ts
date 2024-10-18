// src/app/guards/auth.guard.ts
import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from '../service/auth.service';
@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router) {}
  canActivate(): boolean {
    const token = this.authService.getToken();
    if (token) {
      // Si el token existe, permitir el acceso
      return true;
    }
    // Si no hay token, redirigir a la página de login
    this.router.navigate(['/login']);
    return false;
  }
}