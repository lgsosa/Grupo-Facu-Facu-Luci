import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Route, Router } from '@angular/router';
import { jwtDecode } from "jwt-decode";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url = "/api";

  constructor
    (private HttpClient: HttpClient,
      private router :Router
    ) {}

  login(dataLogin:any): Observable<any> {
    return this.HttpClient.post(this.url + '/auth/login', dataLogin).pipe(take(1));
  }

  register(userData: any): Observable<any> {
    return this.HttpClient.post(this.url + '/auth/register', userData);
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigateByUrl('home');
  }

  saveUserSession(token: string, rol: string): void {
      // tengo que implenetar la lógica para guardar la sesión del usuario
      localStorage.setItem('token', token);
      localStorage.setItem('rol', rol);
    }

  isAdminOrLibrarian(): boolean {
      const token = localStorage.getItem('token');
      const rol = localStorage.getItem('rol'); // Obtén el rol de localStorage
      if (!token || !rol) {
          return false; // No hay token o rol, el usuario no está autenticado
      }
  
      try {
          const decoded: any = jwtDecode(token);
          console.log("jwt decode", decoded);
          console.log(`Rol almacenado: ${rol}`); // Muestra el rol almacenado
          return rol === 'admin' || rol === 'librarian'; // Usa el rol almacenado
      } catch (error) {
          console.error('Error al decodificar el token', error);
          return false; // Si hay un error, no es admin ni bibliotecario
      }
  }  
  getToken(): string | null {
    return localStorage.getItem('token');
  }

  }
