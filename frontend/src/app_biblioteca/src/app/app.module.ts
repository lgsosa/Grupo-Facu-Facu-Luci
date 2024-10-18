import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms'; 
import { AppRoutingModule } from './app-routing.module'; 
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { ErrorPageComponent } from './pages/error-page/error-page.component';
import { NavComponent } from './components/nav/nav.component';
import { FooterComponent } from './components/footer/footer.component';
import { GestiondeusuarioComponent } from './pages/gestiondeusuario/gestiondeusuario.component';
import { RegisterComponent } from './pages/register/register.component';
import { PrestamosComponent } from './pages/prestamos/prestamos.component';
import { LibroComponent } from './pages/libro/libro.component';
import { LoginComponent } from './pages/login/login.component';
import { ListaLibrosEstrellasComponent } from './pages/lista-libros-estrellas/lista-libros-estrellas.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ErrorPageComponent,
    NavComponent,
    FooterComponent,
    GestiondeusuarioComponent,
    RegisterComponent,
    PrestamosComponent,
    LibroComponent,
    LoginComponent,
    ListaLibrosEstrellasComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    AppRoutingModule  
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
