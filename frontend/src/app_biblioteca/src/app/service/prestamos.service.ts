import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PrestamosService {
  url = '/api';  

  constructor(private http: HttpClient) { }

  private getHeaders(): HttpHeaders {
    const auth_token = localStorage.getItem('token');
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
  }

  getPrestamos(): Observable<any> {
    return this.http.get(`${this.url}/prestamos`, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error fetching prestamos', error);
          return throwError(error);
        })
      );
  }

  addPrestamo(nuevoPrestamo: any): Observable<any> {
    return this.http.post(`${this.url}/prestamos`, nuevoPrestamo, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error adding prestamo', error);
          return throwError(error);
        })
      );
  }

  editPrestamo(prestamoEditado: any): Observable<any> {
    // Adaptar la estructura del objeto prestamoEditado para que coincida con lo que espera el backend
    const prestamoData = {
      usuario_id: prestamoEditado.id_usuario,
      libro_id: prestamoEditado.id_libro,
      cantidad: prestamoEditado.cantidad,
      tiempo_de_devolucion: prestamoEditado.tiempo_de_devolucion
    };
    
    return this.http.put(`${this.url}/prestamo/${prestamoEditado.id}`, prestamoData, { headers: this.getHeaders() })
      .pipe(
        catchError((error) => {
          console.error('Error editing prestamo', error);
          return throwError(error);
        })
      );
  }

  deletePrestamo(prestamoId: number): Observable<any> {
    return this.http.delete(`${this.url}/prestamo/${prestamoId}`, { headers: this.getHeaders() });
  }
  
}
