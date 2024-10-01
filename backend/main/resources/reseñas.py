from .valoracion import valoraciones
from .comentarios import comentarios
from .libro import LIBROS
from main.models import ReseñasModel
from .. import db
from flask import Flask, request, jsonify
from main.models.reseñas import usuario_reseñas
from flask_restful import Resource
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required

class Reseñas (Resource):
    @jwt_required(optional=True)
    def get(self, id):

        # Página inicial por defecto
        page = 1
        # Cantidad de elementos por página por defecto
        per_page = 10
        
        # No ejecuto el .all()
        usuarios = db.session.query(ReseñasModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###

        if request.args.get('usuario_reseñas'):
            usuarios = usuarios.outerjoin(ReseñasModel.historias).group_by(ReseñasModel.id).having(func.count(usuario_reseñas.id) >= int(request.args.get('usuario_reseñas')))

        
        # Obtener valor paginado
        usuarios = usuarios.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                        'total': usuarios.total,
                        'pages': usuarios.pages,
                        'page': page
                        })

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


