from flask_restful import Resource
from flask import request
from .libro import LIBROS
from .notificaciones import NOTIFICACIONES
from .prestamo import PRESTAMOS 
from .valoracion import valoraciones

class Configuracion(Resource):
    def get (self,id):
        if int(id) in LIBROS:
            return LIBROS (int(id)), NOTIFICACIONES(int(id)), PRESTAMOS (int(id)), valoraciones
        
        
        return "No existe esta configuracion de la biblioteca", 404
    
    def put (self,id):
        if int(id) in LIBROS:
            usuarios = LIBROS (int(id))
            data = request.get_json()
            usuarios.update(data)
            return "",201
        
        return "No existe esta configuracion de la biblioteca", 404