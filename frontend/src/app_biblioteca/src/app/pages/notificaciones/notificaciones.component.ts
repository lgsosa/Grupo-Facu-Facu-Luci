import { Component } from '@angular/core';

interface Notificacion {
  texto: string;
  id_usuario: number | null; // Asegúrate de que esto sea correcto
}

@Component({
  selector: 'app-notificaciones', // Verifica que el selector sea único
  templateUrl: './notificaciones.component.html',
  styleUrls: ['./notificaciones.component.scss'] // Asegúrate de que este archivo exista o elimina esta línea
})


export class NotificacionesComponent {
  notificacion: Notificacion = { texto: '', id_usuario: null };
  editIndex: number | null = null;
  editMode: boolean = false; // Añadir esta línea
  notificaciones: Notificacion[] = [];

  agregarNotificacion() {
    if (this.editIndex !== null) {
      this.notificaciones[this.editIndex] = { ...this.notificacion };
      this.editIndex = null;
      this.editMode = false; // Resetear editMode al guardar cambios
    } else {
      this.notificaciones.push({ ...this.notificacion });
    }
    this.notificacion = { texto: '', id_usuario: null };
  }

  editarNotificacion(index: number) {
    this.editIndex = index;
    this.notificacion = { ...this.notificaciones[index] };
    this.editMode = true; // Activar editMode al editar
  }

  eliminarNotificacion(index: number) {
    this.notificaciones.splice(index, 1);
  }
}
