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
  registerForm!: FormGroup;
  errorMessage: string | null = null; // Propiedad para el mensaje de error
  canAddUsers: boolean = false; // Propiedad para controlar el acceso

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.registerForm = this.fb.group({
      nombre: ['', Validators.required],
      telefono: ['', Validators.required],
      correo_electronico: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      rol: ['', Validators.required]
    });

    this.canAddUsers = this.authService.isAdminOrLibrarian(); // Verifica si el usuario puede agregar
  }

  onSubmit(): void {
    if (this.registerForm.valid && this.canAddUsers) {
      this.authService.register(this.registerForm.value).subscribe({
        next: (response) => {
          console.log('Registro exitoso', response);
          this.router.navigate(['/login']);
        },
        error: (error) => {
          console.error('Error en el registro', error);
          this.errorMessage = 'Ocurrió un error. Por favor, intenta nuevamente.';
        }
      });
    } else if (!this.canAddUsers) {
      this.errorMessage = 'Regístrese en la biblioteca para acceder a esta función.';
    }
  }
}
