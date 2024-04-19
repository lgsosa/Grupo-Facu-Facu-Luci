from flask_restful import Resource
from flask import request, jsonify
from .libro import LIBROS
from .notificaciones import NOTIFICACIONES
from .prestamo import PRESTAMOS
from .valoracion import valoraciones

class Configuracion(Resource):
    def get(self, id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
            notificaciones = NOTIFICACIONES.get(int(id), {})  # Si no existe, devuelve un diccionario vacío
            prestamos = PRESTAMOS[int(id)]
            valoracion = valoraciones.get(int(id), "")
            
            return {
                "libro": libro,
                "notificaciones": notificaciones,
                "prestamos": prestamos,
                "valoracion": valoracion
            }, 200
        
        return "No existe esta configuracion de la biblioteca", 404