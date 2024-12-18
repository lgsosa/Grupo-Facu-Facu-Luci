import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ErrorPageComponent } from './pages/error-page/error-page.component';
import { GestiondeusuarioComponent } from './pages/gestiondeusuario/gestiondeusuario.component';
import { RegisterComponent } from './pages/register/register.component';
import { PrestamosComponent } from './pages/prestamos/prestamos.component';
import { LibroComponent } from './pages/libro/libro.component';
import { LoginComponent } from './pages/login/login.component';
import { ListaLibrosEstrellasComponent } from './pages/lista-libros-estrellas/lista-libros-estrellas.component';
import { authsessionrolGuard } from './guards/authsessionrol.guard';
import { NotificacionesComponent } from './pages/notificaciones/notificaciones.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'error_page', component: ErrorPageComponent },
  { path: 'gestiondeusuario', component: GestiondeusuarioComponent, canActivate: [authsessionrolGuard]}, 
  { path: 'register', component: RegisterComponent,  canActivate: [authsessionrolGuard] },
  { path: 'prestamos', component: PrestamosComponent, canActivate: [authsessionrolGuard] },
  { path: 'libros', component: ListaLibrosEstrellasComponent },
  { path: 'login', component: LoginComponent },
  { path: 'libro/:id', component: LibroComponent },
  {path: 'notificaciones', component: NotificacionesComponent, canActivate: [authsessionrolGuard] },

  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: '**', redirectTo: 'error_page' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
