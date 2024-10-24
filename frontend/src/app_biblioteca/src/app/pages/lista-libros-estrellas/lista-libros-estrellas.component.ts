import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-lista-libros-estrellas',
  templateUrl: './lista-libros-estrellas.component.html',
  styleUrls: ['./lista-libros-estrellas.component.scss']
})
export class ListaLibrosEstrellasComponent implements OnInit {

  libros = [
    {
      title: 'Reyes caidos',
      image: 'assets/reyes_caidos.webp', 
      stars: '★★★★☆',
      synopsis: '"Reyes Caídos" es un libro que compila todas las dimensiones, reinos y dioses que fueron derrotados por una entidad llamada El Hambre antes de su aparición. El libro trata sobre la confrontación de estas fuerzas y sus efectos en los reinos y su historia',
      comentarios: ['']
    },
    {
      title: 'Cruce de caminos',
      image: 'assets/crucedecaminos.webp',
      stars: '★★★☆☆',
      synopsis: '"Cruce de caminos" de Naira Gamboa narra la historia de una joven que debe tomar decisiones cruciales en su vida, explorando temas de amor, crecimiento personal y el impacto de las elecciones.',
      comentarios: ['']
    },
    {
      title: 'Cuentos de otoño',
      image: 'assets/cuentosdeotoño.jpg',
      stars: '★★★★★',
      synopsis: '"Cuentos de otoño" de José Luis Alonso de Santos es una colección de relatos que reflejan emociones y situaciones cotidianas, utilizando el otoño como metáfora de cambio, melancolía y reflexión sobre la vida.',
      comentarios: ['']
    },
    {
      title: "L'omme montagne",
      image: 'assets/lhommemontagne.jpg',
      stars: '★★☆☆☆',
      synopsis: "L'omme montagne de Marco Paci narra la búsqueda de identidad de un hombre en un entorno desafiante, explorando temas de lucha personal y conexión con la naturaleza.",
      comentarios: ['']
    }
  ];
  
  currentPage: number = 1; 
  itemsPerPage: number = 4; 

  constructor() { }

  ngOnInit(): void { }

  getPaginatedLibros() {
    const startIndex = (this.currentPage - 1) * this.itemsPerPage;
    const endIndex = startIndex + this.itemsPerPage;
    return this.libros.slice(startIndex, endIndex);
  }

  nextPage() {
    if (this.currentPage * this.itemsPerPage < this.libros.length) {
      this.currentPage++;
    }
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.currentPage--;
    }
  }
}
