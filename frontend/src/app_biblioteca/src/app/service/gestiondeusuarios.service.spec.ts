import { TestBed } from '@angular/core/testing';

import { GestiondeusuariosService } from './gestiondeusuarios.service';

describe('GestiondeusuariosService', () => {
  let service: GestiondeusuariosService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GestiondeusuariosService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
