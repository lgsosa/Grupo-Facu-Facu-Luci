// src/app/services/auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'URL_DEL_BACKEND'; // Cambia a la URL real de tu backend
  constructor(private http: HttpClient) {}
  // Método para hacer login y obtener el JWT
  login(credentials: { email: string, password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, credentials);
  }
  // Guardar el token JWT en localStorage
  saveToken(token: string): void {
    localStorage.setItem('jwtToken', token);
  }
  // Obtener el token JWT desde localStorage
  getToken(): string | null {
    return localStorage.getItem('jwtToken');
  }
  // Eliminar el token JWT de localStorage (logout)
  logout(): void {
    localStorage.removeItem('jwtToken');
  }
}