import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
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
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AuthService } from './services/auth.service';  // Servicio de autenticación
import { AuthGuard } from './guards/auth.guard';       // Guard para autenticación
import { RoleGuard } from './guards/role.guard';       // Guard para roles

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
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    AuthService,  // Asegúrate de proveer el servicio
    AuthGuard,    // Guard de autenticación
    RoleGuard     // Guard de roles
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
