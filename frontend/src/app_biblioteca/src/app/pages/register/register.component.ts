import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  registerForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.registerForm = this.fb.group({
      name: ['', Validators.required],
      lastname: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.registerForm.valid) {
        const { name, lastname, email, password } = this.registerForm.value;
        this.authService.register({ name, lastname, email, password }).subscribe(
            (response) => {
                console.log('Registro exitoso', response);
                // Redirigir al login o mostrar un mensaje
                this.router.navigate(['/login']);
            },
            (error) => {
                console.error('Error en el registro', error);

        }
      );
    }
  }
}
