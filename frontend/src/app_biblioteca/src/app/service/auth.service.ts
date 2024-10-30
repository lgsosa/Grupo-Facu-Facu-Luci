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
    //let dataLogin = {
    //  email: "lucianagsosa03@gmail.com",
    //  password: "123456789"
    //}
    return this.HttpClient.post(this.url + '/auth/login', dataLogin).pipe(take(1));
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
      if (!token) {
        return false; // No hay token, el usuario no está autenticado
      }
  
      try {
        const decoded:any = jwtDecode(token);
        console.log("jwt decode",decoded)
        // Asumiendo que en el payload del token tienes un campo 'role'
        return decoded.rol === 'admin' || decoded.rol === 'librarian';
      } catch (error) {
        console.error('Error al decodificar el token', error);
        return false; // Si hay un error, no es admin ni bibliotecario
      }
    }
  }
