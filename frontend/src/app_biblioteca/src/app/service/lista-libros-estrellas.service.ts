// lista-libros-estrellas.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ListaLibrosEstrellasService {
  url = '/api'; 

  constructor(private http: HttpClient) { }

  private getHeaders(): HttpHeaders {
    const auth_token = localStorage.getItem('token');
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
  }

  obtenerValoraciones(page: number): Observable<any> {
    return this.http.get<{ valoraciones: any[], pages: number }>(`${this.url}/valoraciones?page=${page}&per_page=5`, { headers: this.getHeaders() })
      .pipe(
        map(response => response), // Devuelve la respuesta completa para acceder a totalPages
        catchError((error) => {
          console.error('Error fetching valoraciones', error);
          return throwError(error);
        })
      );
  }

  agregarValoracion(id_libro: number, nombre_del_libro: string, valoracion: number): Observable<any> {
    const body = { id_libro, nombre_del_libro, valoracion };
    return this.http.post<any>(`${this.url}/valoracion`, body, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error adding valoracion', error);
          return throwError(error);
        })
      );
  }
}
