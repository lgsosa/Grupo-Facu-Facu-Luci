from flask_restful import Resource
from flask import request, jsonify
from .usuario import USUARIOS
import json
from main.models import NotificacionesModel
from .. import db

NOTIFICACIONES = {
    1: {"notificacion": " Por favor pase por secretaria cuando sea posible: "},
    2: {"notificacion": " Se olvido sus pertenencias en la biblioteca "}
}


class Notificaciones(Resource):
    def get(self):
        # Página inicial por defecto
        page = 1
        # Cantidad de elementos por página por defecto
        per_page = 10
        
        # No ejecuto el .all()
        usuarios = db.session.query(NotificacionesModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        
        # Obtener valor paginado
        usuarios = usuarios.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                        'total': usuarios.total,
                        'pages': usuarios.pages,
                        'page': page
                        })
    
    #insertar recurso
    def post(self):
        notificaciones = NotificacionesModel.from_json(request.get_json())
        db.session.add(notificaciones)
        db.session.commit()
        return notificaciones.to_json(), 201
