from flask_restful import Resource
from flask import request
from .usuario import USUARIOS
from .. import db
from main.models import PrestamosModel

PRESTAMOS = {
    1: {"usuario":" Facundo Mesa ", "cantidad":" 2 ","tiempo de devolucion":" 15 dias "},
    2: {"usuario":" Luciana Sosa ", "cantidad":" 1 ","tiempo de devolucion":" 5 dias "}
 }

class Prestamo (Resource):
    def get(self,id):
        prestamos = db.session.query(PrestamosModel).get_or_404(id)
        return prestamos.to_json
     #   if int(id) in PRESTAMOS:
      #      return PRESTAMOS [int(id)]
        
       # return "No existe el id", 404
    
    def put(self, id):
        if int(id) in PRESTAMOS:
            animal = PRESTAMOS[int(id)]
            data = request.get_json()
            animal.update(data)
            return ' Prestamo actualizado correctamente ', 201
        return ' Error al crear "Prestamo" ', 404

    def delete (self,id):
        if int(id) in PRESTAMOS:
            del PRESTAMOS [int(id)]

        return "No existe el id", 404
    
class Prestamos (Resource):
    def get (self):
        return PRESTAMOS
    
    def post(self):
        usuario = request.get_json()
        id = int(max(PRESTAMOS.keys(), default=0)) + 1
        PRESTAMOS[id] = usuario
        return {'mensaje': 'El prestamo ha sido creado con éxito'}, 201