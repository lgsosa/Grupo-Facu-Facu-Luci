import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class GestionDeUsuarioService {
  private url = '/api/usuarios';  // Para las solicitudes GET y POST

  constructor(private http: HttpClient) { }

  private getHeaders(): HttpHeaders {
    const auth_token = localStorage.getItem('token');
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
  }

  getUsuarios(page: number = 1, perPage: number = 10): Observable<any> {
    return this.http.get(`${this.url}?page=${page}&per_page=${perPage}`, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error fetching usuarios', error);
          return throwError(error);
        })
      );
  }

  getUsuario(id: number): Observable<any> {
    return this.http.get(`${this.url}/${id}`, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error fetching usuario', error);
          return throwError(error);
        })
      );
  }

  crearUsuario(nuevoUsuario: any): Observable<any> {
    return this.http.post(this.url, nuevoUsuario, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error creating usuario', error);
          return throwError(error);
        })
      );
  }

  editarUsuario(id: number, usuarioEditado: any): Observable<any> {
    // Cambiar la ruta para PUT
    return this.http.put(`/api/usuario/${id}`, usuarioEditado, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error editing usuario', error);
          return throwError(error);
        })
      );
  }

  eliminarUsuario(id: number): Observable<any> {
    // Cambiar la ruta para DELETE
    return this.http.delete(`/api/usuario/${id}`, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error deleting usuario', error);
          return throwError(error);
        })
      );
  }
}
