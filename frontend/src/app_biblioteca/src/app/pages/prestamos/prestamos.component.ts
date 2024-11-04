import { Component, OnInit } from '@angular/core';
import { PrestamosService } from '../../service/prestamos.service';

@Component({
  selector: 'app-prestamos',
  templateUrl: './prestamos.component.html',
  styleUrls: ['./prestamos.component.scss']
})
export class PrestamosComponent implements OnInit {
  prestamos: any[] = [];
  nuevoPrestamo: any = {
    nombre_usuario: '',
    cantidad: 1,
    tiempo_de_devolucion: 7,
    id_usuario: '',
    id_libro: '',
    correo_electronico: ''
  };
  prestamoEditado: any;

  constructor(private prestamosService: PrestamosService) { }

  ngOnInit(): void {
    this.getPrestamos();
  }

  getPrestamos(): void {
    this.prestamosService.getPrestamos().subscribe(data => {
      this.prestamos = data.usuarios;
    }, error => {
      console.error('Error fetching prestamos', error);
    });
  }

  guardarPrestamo(): void {
    this.prestamosService.addPrestamo(this.nuevoPrestamo).subscribe(data => {
      this.prestamos.push(data);
      this.nuevoPrestamo = { // Reset nuevoPrestamo
        nombre_usuario: '',
        cantidad: 1,
        tiempo_de_devolucion: 7,
        id_usuario: '',
        id_libro: '',
        correo_electronico: ''
      };
      console.log('Prestamo added', data);
    }, error => {
      console.error('Error adding prestamo', error);
    });
  }

  editarPrestamo(prestamo: any): void {
    this.prestamoEditado = prestamo; // Load prestamo to edit
  }

  actualizarPrestamo(): void {
    this.prestamosService.editPrestamo(this.prestamoEditado).subscribe(data => {
      const index = this.prestamos.findIndex(p => p.id === data.id); // Asegúrate de que aquí sea el id correcto
      if (index !== -1) {
        this.prestamos[index] = data; // Update the prestamo
      }
      this.prestamoEditado = null; // Reset the edited prestamo
      console.log('Prestamo updated', data);
    }, error => {
      console.error('Error updating prestamo', error);
    });
  }

  eliminarPrestamo(prestamo: any): void {
    // Solo necesitas el ID del préstamo para eliminarlo
    const prestamoId = prestamo.id; // Asegúrate de que prestamo.id contiene el ID correcto
  
    console.log('ID del préstamo a eliminar:', prestamoId); // Verifica el ID
  
    this.prestamosService.deletePrestamo(prestamoId).subscribe(() => {
      // Filtra el préstamo eliminado de la lista
      this.prestamos = this.prestamos.filter(p => p.id !== prestamoId);
      console.log('Préstamo eliminado');
    }, error => {
      console.error('Error al eliminar el préstamo:', error);
    });
  }
  
}
