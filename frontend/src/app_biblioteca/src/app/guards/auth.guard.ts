import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Route, Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url = "/api";

  constructor(
    private HttpClient: HttpClient,
    private router: Router
  ) {}

  login(dataLogin: any): Observable<any> {
    return this.HttpClient.post(this.url + '/auth/login', dataLogin).pipe(take(1));
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('role');
    this.router.navigateByUrl('home');
  }

  saveUserSession(token: string, role: string) {
    localStorage.setItem('token', token);
    localStorage.setItem('role', role);
  }

  getRole() {
    return localStorage.getItem('role');
  }

  isAdminOrLibrarian(): boolean {
    const role = this.getRole();
    return role === 'admin' || role === 'bibliotecario';
  }
}
