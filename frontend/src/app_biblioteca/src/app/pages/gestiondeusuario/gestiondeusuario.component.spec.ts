import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GestiondeusuarioComponent } from './gestiondeusuario.component';

describe('GestiondeusuarioComponent', () => {
  let component: GestiondeusuarioComponent;
  let fixture: ComponentFixture<GestiondeusuarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [GestiondeusuarioComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GestiondeusuarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
