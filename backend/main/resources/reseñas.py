from .valoracion import valoraciones
from .comentarios import comentarios
from .libro import LIBROS
from main.models import ReseñasModel
from .. import db

from flask_restful import Resource

class Reseñas (Resource):
    def get(self, id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
            valoracion = valoraciones.get(int(id), "")
            comentario = comentarios.get(int(id),"")
            
            return {
                "libro": libro,
                "valoracion": valoracion,
                "comentarios": comentario

            }, 200
        
        return "No existe este numero de reseña ", 404

