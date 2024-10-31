import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { GestiondeusuariosService } from '../../service/gestiondeusuarios.service';

@Component({
  selector: 'app-gestiondeusuario',
  templateUrl: './gestiondeusuario.component.html',
  styleUrls: ['./gestiondeusuario.component.scss'] // Corregido de styleUrl a styleUrls
})
export class GestiondeusuarioComponent {
  searchQuery = '';
  
  arrayUsuarios: any[] = [];
  filteredUsers: any[] = [];
  nuevoUsuario: any = {
    name: '',
    phone: '',
    email: ''
  };

  currentPage: number = 1; // Variable para manejar la paginación

  constructor(
    private router: Router,
    private gestiondeusuarios: GestiondeusuariosService
  ) {}

  ngOnInit() {
    this.gestiondeusuarios.getUsers().subscribe((rta: any) => {
      console.log('usuarios api: ', rta);
      this.arrayUsuarios = rta.usuarios || [];
      this.filteredUsers = [...this.arrayUsuarios];
    });
  }
  
  editarusuario(user: any) {
    console.log('Estoy editando', user);
    this.router.navigate(['/usuario' + user.id + '/editar']);
  }

  buscar() {
    console.log('buscar: ', this.searchQuery);
    this.filteredUsers = this.arrayUsuarios.filter(user => user.name.includes(this.searchQuery));
  }

  // Método para paginación anterior
  paginacionAnterior() {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.updateFilteredUsers();
    }
  }

  // Método para paginación siguiente
  paginacionSiguiente() {
    this.currentPage++;
    this.updateFilteredUsers();
  }

  // Método para guardar un nuevo usuario
  guardarUsuario(form: any) {
    console.log('Guardando usuario', this.nuevoUsuario);
    // Aquí puedes implementar la lógica para guardar el nuevo usuario
    // Por ejemplo, llamar a un servicio que envíe los datos al backend
    this.gestiondeusuarios.addUser(this.nuevoUsuario).subscribe((response: any) => {
      console.log('Usuario guardado:', response);
      // Reiniciar el formulario y actualizar la lista de usuarios
      this.nuevoUsuario = { name: '', phone: '', email: '' };
      this.ngOnInit(); // Refrescar la lista de usuarios
    });
  }

  // Método para actualizar la lista de usuarios filtrados según la página actual
  private updateFilteredUsers() {
    // Aquí implementa la lógica para filtrar los usuarios según la paginación
    // Por ejemplo, puedes utilizar slice para mostrar solo un número limitado de usuarios por página
  }
  
}
