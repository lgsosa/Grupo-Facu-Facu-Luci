import { Component, OnInit } from '@angular/core';
import { ListaLibrosEstrellasService } from '../../service/lista-libros-estrellas.service';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-lista-libros-estrellas',
  templateUrl: './lista-libros-estrellas.component.html',
  styleUrls: ['./lista-libros-estrellas.component.scss']
})
export class ListaLibrosEstrellasComponent implements OnInit {
  libros = [
    { id: 1, titulo: 'Reyes Caídos', imagen: '../../assets/reyes_caidos.webp', nuevaValoracion: '' },
    { id: 2, titulo: 'Cruce de Caminos', imagen: 'assets/crucedecaminos.webp', nuevaValoracion: '' },
    { id: 3, titulo: 'L\'homme de la montagne', imagen: 'assets/lhommemontagne.jpg', nuevaValoracion: '' },
    { id: 4, titulo: 'Cuentos de Otoño', imagen: 'assets/cuentosdeotoño.jpg', nuevaValoracion: '' },
  ];

  valoraciones: any[] = []; // Aquí almacenarás las valoraciones obtenidas
  currentPage: number = 1; // Página actual
  totalPages: number = 1; // Total de páginas

  constructor(private listaLibrosEstrellasService: ListaLibrosEstrellasService) { }

  ngOnInit(): void {
    this.obtenerValoraciones(); // Llama a obtener valoraciones al inicializar el componente
  }

  obtenerValoraciones(): void {
    this.listaLibrosEstrellasService.obtenerValoraciones(this.currentPage).subscribe(
      (data: any) => {
        this.valoraciones = data.valoraciones; // Almacena las valoraciones
        this.totalPages = data.pages; // Almacena el total de páginas
        console.log('Valoraciones obtenidas:', this.valoraciones);
        console.log('Total de páginas:', this.totalPages);
      },
      (error) => {
        console.error('Error al obtener valoraciones', error);
      }
    );
  }

  // Navega a la página anterior
  previousPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--; // Decrementa la página actual
      this.obtenerValoraciones(); // Carga las valoraciones de la nueva página
    }
  }

  // Navega a la página siguiente
  nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++; // Incrementa la página actual
      this.obtenerValoraciones(); // Carga las valoraciones de la nueva página
    }
  }

  agregarValoracion(libro: any): void {
    const valoracionNumerica = Number(libro.nuevaValoracion);
    if (!isNaN(valoracionNumerica)) {
      this.listaLibrosEstrellasService
        .agregarValoracion(libro.id, libro.titulo, valoracionNumerica)
        .subscribe(
          (response: any) => {
            console.log('Valoración agregada exitosamente', response);
            this.obtenerValoraciones(); // Vuelve a cargar las valoraciones después de agregar una nueva
          },
          (error: any) => {
            console.error('Error al agregar la valoración', error);
          }
        );
    } else {
      console.error('Valoración no válida:', libro.nuevaValoracion);
    }
  }
}
