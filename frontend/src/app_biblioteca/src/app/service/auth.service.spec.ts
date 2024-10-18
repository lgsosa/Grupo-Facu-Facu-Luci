import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private tokenKey = 'auth_token'; // Nombre del token en localStorage

  saveToken(token: string): void {
    localStorage.setItem(this.tokenKey, token);
  }

  isLoggedIn(): boolean {
    return !!localStorage.getItem(this.tokenKey); // Devuelve true si hay un token
  }

  logout(): void {
    localStorage.removeItem(this.tokenKey); // Elimina el token al cerrar sesión
  }
}
