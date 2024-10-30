import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-libro',
  templateUrl: './libro.component.html',
  styleUrls: ['./libro.component.scss']
})
export class LibroComponent implements OnInit {
  libroId: string | null = null;
  libro: any; // Puedes definir un tipo más específico si lo deseas

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.libroId = params.get('id'); // Captura el ID
      this.cargarLibro(this.libroId);
    });
  }

  cargarLibro(id: string | null) {
    // Simulando una carga de datos (puedes integrar un servicio aquí)
    const libros = [
      { id: 'reyes_caidos', title: 'Reyes Caídos', synopsis: 'Sinopsis de Reyes Caídos...', stars: '★★★★★', image: 'assets/reyes_caidos.webp' },
      { id: 'cruce_de_caminos', title: 'Cruce de Caminos', synopsis: 'Sinopsis de Cruce de Caminos...', stars: '★★★★★', image: 'assets/crucedecaminos.webp' },
      { id: 'lhomme_de_la_montagne', title: "L'homme de la montagne", synopsis: 'Sinopsis de L\'homme de la montagne...', stars: '★★★★☆', image: 'assets/lhommemontagne.jpg' },
      { id: 'cuentos_de_otono', title: 'Cuentos de Otoño', synopsis: 'Sinopsis de Cuentos de Otoño...', stars: '★★★★★', image: 'assets/cuentosdeotoño.jpg' },
    ];

    this.libro = libros.find(libro => libro.id === id);
  }
}
