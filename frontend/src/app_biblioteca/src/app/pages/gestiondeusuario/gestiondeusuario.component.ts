import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { GestiondeusuariosService } from '../../service/gestiondeusuarios.service';

@Component({
  selector: 'app-gestiondeusuario',
  templateUrl: './gestiondeusuario.component.html',
  styleUrl: './gestiondeusuario.component.scss'
})
export class GestiondeusuarioComponent {
  searchQuery = "";
  
  arrayUsuarios:any[] = []
  filteredUsers:any = []

  constructor(
    private router: Router,
    private gestiondeusuarios: GestiondeusuariosService
  ){}

  ngOnInit(){

    this.gestiondeusuarios.getUsers().subscribe((rta:any) => {
      console.log("usuarios api: ", rta);
      this.arrayUsuarios = rta.usuarios || []
      this.filteredUsers = [...this.arrayUsuarios]

    })

  }
  
  editarusuario(user:any){
    console.log("Estoy editando", user);
    this.router.navigate(["/usuario"+user.id+"/editar"]);
  }

  buscar(){
    console.log("buscar: ", this.searchQuery);
    this.filteredUsers = this.arrayUsuarios.filter(user => user.name.includes(this.searchQuery))
  }



}
