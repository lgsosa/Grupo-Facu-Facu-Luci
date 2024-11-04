import { TestBed } from '@angular/core/testing';

import { GestiondeusuarioService } from './gestiondeusuario.service';

describe('GestiondeusuarioService', () => {
  let service: GestiondeusuarioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GestiondeusuarioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
