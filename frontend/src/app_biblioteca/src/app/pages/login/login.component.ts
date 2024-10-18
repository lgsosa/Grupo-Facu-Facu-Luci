import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
  export class LoginComponent implements OnInit {
    loginForm: FormGroup;

    constructor(
      private fb: FormBuilder,
      private authService: AuthService,
      private router: Router
    ) {
      this.loginForm = this.fb.group({
        email: ['', [Validators.required, Validators.email]],
        password: ['', Validators.required]
      });
    }

    ngOnInit(): void {
      console.log('LoginComponent inicializado'); 
    }    

  onSubmit(): void {
    if (this.loginForm.valid) {
      const { email, password } = this.loginForm.value;
      this.authService.login({ email, password }).subscribe(
        (response) => {
          this.authService.saveToken(response.token);
          this.router.navigate(['/home']);
        },
        (error) => {
          console.error('Error en el login', error);
        }
      );
    }
  }
}


