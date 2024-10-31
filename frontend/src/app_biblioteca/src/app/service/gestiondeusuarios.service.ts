import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GestiondeusuariosService {

  url = '/api';
  constructor(
    private HttpClient:HttpClient
  ){ }

  getUsers() {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}` 
    })

    const requestOptions = {headers: headers}
    return this.HttpClient.get(this.url+ '/usuarios', requestOptions);
}

  addUser(nuevoUsuario: any): Observable<any>  {
    return this.HttpClient.post<any>(`${this.url}/usuarios`, nuevoUsuario); // Asegúrate de que esta ruta sea correcta
  }

}
