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
    
    # Modificar el recurso préstamo
    def put(self, id):
        prestamo = db.session.query(PrestamosModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(prestamo, key, value)
        db.session.commit()
        return 'Prestamo actualizado correctamente', 201

    # Eliminar recurso préstamo
    def delete(self, id):
        prestamo = db.session.query(PrestamosModel).get_or_404(id)
        db.session.delete(prestamo)
        db.session.commit()
        return ' Eliminado correctamente ', 204


class Prestamos (Resource):
    def get (self):
        return PRESTAMOS
    
    #insertar recurso
    def post(self):
        prestamo = PrestamosModel.from_json(request.get_json())
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201