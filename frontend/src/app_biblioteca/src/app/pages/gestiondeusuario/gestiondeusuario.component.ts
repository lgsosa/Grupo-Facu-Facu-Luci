import { Component, OnInit } from '@angular/core';
import { GestionDeUsuarioService } from '../../service/gestiondeusuario.service';

@Component({
  selector: 'app-gestiondeusuario',
  templateUrl: './gestiondeusuario.component.html',
  styleUrls: ['./gestiondeusuario.component.scss']
})
export class GestiondeusuarioComponent implements OnInit {
  usuarios: any[] = [];  // Lista de usuarios
  nuevoUsuario: any = {}; // Objeto para crear un nuevo usuario
  usuarioSeleccionado: any = null; // Usuario seleccionado para editar

  constructor(private gestionDeUsuarioService: GestionDeUsuarioService) {}

  ngOnInit(): void {
    this.obtenerUsuarios();
  }

  obtenerUsuarios() {
      this.gestionDeUsuarioService.getUsuarios().subscribe(data => {
        console.log(data);  // Verifica la respuesta completa en la consola
        this.usuarios = data.usuarios;
      }, error => {
        console.error('Error al cargar los usuarios', error);
      });
    }


  guardarUsuario(): void {
    this.gestionDeUsuarioService.crearUsuario(this.nuevoUsuario).subscribe(
      (response) => {
        this.obtenerUsuarios(); // Actualiza la lista después de añadir un nuevo usuario
        this.nuevoUsuario = {}; // Resetea el formulario
      },
      (error) => {
        console.error('Error creating user', error);
      }
    );
  }

  editarUsuario(usuario: any): void {
    this.usuarioSeleccionado = { ...usuario }; // Clona el usuario seleccionado
  }

  actualizarUsuario(): void {
    if (this.usuarioSeleccionado) {
      this.gestionDeUsuarioService.editarUsuario(this.usuarioSeleccionado.id, this.usuarioSeleccionado).subscribe(
        (response) => {
          this.obtenerUsuarios(); // Actualiza la lista después de la edición
          this.usuarioSeleccionado = null; // Resetea la edición
        },
        (error) => {
          console.error('Error updating user', error);
        }
      );
    }
  }

  eliminarUsuario(id: number): void {
    this.gestionDeUsuarioService.eliminarUsuario(id).subscribe(
      (response) => {
        this.obtenerUsuarios(); // Actualiza la lista después de la eliminación
      },
      (error) => {
        console.error('Error deleting user', error);
      }
    );
  }

  // Este método se llama antes de eliminar para seleccionar el usuario.
  seleccionarUsuario(usuario: any): void {
    this.usuarioSeleccionado = usuario; // Guarda el usuario seleccionado
  }
}
