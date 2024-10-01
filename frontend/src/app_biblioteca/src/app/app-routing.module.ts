import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ErrorPageComponent } from './pages/error-page/error-page.component';
import { GestiondeusuarioComponent } from './pages/gestiondeusuario/gestiondeusuario.component';
import { RegisterComponent } from './pages/register/register.component';
import { PrestamosComponent } from './pages/prestamos/prestamos.component';
import { LibroComponent } from './pages/libro/libro.component';

const routes: Routes = [

  {path:"home", component: HomeComponent},
  {path:"error_page", component:ErrorPageComponent},
  {path:"gestiondeusuario", component:GestiondeusuarioComponent},
  {path:"register", component:RegisterComponent},
  {path:"prestamos", component:PrestamosComponent},
  {path:"libro", component:LibroComponent},

  {path:"", redirectTo: "/home", pathMatch:"full"},
  {path:"**", redirectTo: "error_page"}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
