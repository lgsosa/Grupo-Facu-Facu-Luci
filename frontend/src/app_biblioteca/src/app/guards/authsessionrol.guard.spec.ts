import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { authsessionrolGuard } from './authsessionrol.guard';

describe('authsessionrolGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => authsessionrolGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
