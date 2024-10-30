import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaLibrosEstrellasComponent } from './lista-libros-estrellas.component';

describe('ListaLibrosEstrellasComponent', () => {
  let component: ListaLibrosEstrellasComponent;
  let fixture: ComponentFixture<ListaLibrosEstrellasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ListaLibrosEstrellasComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListaLibrosEstrellasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
