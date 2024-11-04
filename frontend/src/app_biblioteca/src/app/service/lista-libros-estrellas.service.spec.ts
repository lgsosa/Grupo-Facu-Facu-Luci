import { TestBed } from '@angular/core/testing';

import { ListaLibrosEstrellasService } from './lista-libros-estrellas.service';

describe('ListaLibrosEstrellasService', () => {
  let service: ListaLibrosEstrellasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ListaLibrosEstrellasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
