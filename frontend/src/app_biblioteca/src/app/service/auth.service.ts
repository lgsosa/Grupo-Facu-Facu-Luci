import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Route, Router } from '@angular/router';

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
}
