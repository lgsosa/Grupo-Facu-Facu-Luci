import { Component } from '@angular/core';

interface Notificacion {
  texto: string;
  id_usuario: number;
}

@Component({
  selector: 'app-notificaciones',
  templateUrl: './notificaciones.component.html',
  styleUrls: ['./notificaciones.component.scss'],
})
export class NotificacionesComponent {
  notificacion: string = '';
  id_usuario: number | null = null;
  notificaciones: Notificacion[] = [];
  editarIndex: number | null = null;

  onSubmit() {
    if (this.editarIndex !== null) {
      // Modificar notificación existente
      this.notificaciones[this.editarIndex] = {
        texto: this.notificacion,
        id_usuario: this.id_usuario!,
      };
      this.editarIndex = null; // Reiniciar índice de edición
    } else {
      // Agregar nueva notificación
      this.notificaciones.push({
        texto: this.notificacion,
        id_usuario: this.id_usuario!,
      });
    }

    // Reiniciar los campos
    this.notificacion = '';
    this.id_usuario = null;
  }

  editarNotificacion(index: number) {
    this.editarIndex = index;
    this.notificacion = this.notificaciones[index].texto;
    this.id_usuario = this.notificaciones[index].id_usuario;
  }

  eliminarNotificacion(notificacion: Notificacion) {
    this.notificaciones = this.notificaciones.filter(
      (n) => n !== notificacion
    );
  }
}
