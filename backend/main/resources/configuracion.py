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

    
    def put(self, id):
        if int(id) in LIBROS:
            data = request.get_json()
            
            # Actualizar la configuración del libro
            LIBROS[int(id)].update(data.get("libro", {}))
            
            # Actualizar la configuración de las notificaciones
            NOTIFICACIONES[int(id)].update(data.get("notificaciones", {}))
            
            # Actualizar la configuración de los préstamos
            PRESTAMOS[int(id)].update(data.get("prestamos", {}))
            
            # Actualizar la configuración de las valoraciones
            valoraciones[int(id)] = data.get("valoracion", "")
            
            return "", 201
        
        return "No existe esta configuracion de la biblioteca", 404
