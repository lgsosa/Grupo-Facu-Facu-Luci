from flask_restful import Resource
from flask import request
from .usuario import USUARIOS

PRESTAMOS = {
    1: {"usuario":"", "cantidad":"","tiempo de devolucion":""},
    2: {"usuario":"", "cantidad":"","tiempo de devolucion":""}
 }

class Prestamo (Resource):
    def get(self,id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS [int(id)]
        
        return "No existe el id", 404
    
    def put (self,id):
        if int(id) in PRESTAMOS:
            del PRESTAMOS [int(id)]
            return "",204
        
        return "No existe el id", 404
    
    def delete (self,id):
        if int(id) in PRESTAMOS:
            del PRESTAMOS [int(id)]

        return "No existe el id", 404
    
class Prestamos (Resource):
    def get (self):
        return PRESTAMOS
    
    def post (self):
        prestamo = request.get_json()
        id = int(max(PRESTAMOS.key())+1)
        PRESTAMOS[id] = prestamo
        return PRESTAMOS[id], 201, "recurso creado correctamente"