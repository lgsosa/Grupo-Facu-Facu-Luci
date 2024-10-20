import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  login(credentials: { email: string, password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, credentials);
  }

  register(user: { name: string, lastname: string, email: string, password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/register`, user);
  }

  saveToken(token: string): void {
    localStorage.setItem('token', token);
  }

  // Obtener el token JWT desde localStorage
  getToken(): string | null {
    return localStorage.getItem('jwtToken');
  }

  // Eliminar el token JWT de localStorage (logout)
  logout(): void {
    localStorage.removeItem('jwtToken');
  }

  // Método para verificar si el usuario está autenticado
  isLoggedIn(): boolean {
    return !!this.getToken(); // Devuelve true si hay un token
  }
}
