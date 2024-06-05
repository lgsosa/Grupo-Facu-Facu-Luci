from flask_restful import Resource
from flask import request, jsonify
import json
from main.models import NotificacionesModel
from .. import db
from main.auth.decorators import role_required
from flask_jwt_extended import jwt_required, get_jwt_identity


class Notificaciones(Resource):
    @jwt_required(optional=True)
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
    @role_required(roles=["admin"])

    def post(self):
        current_user_id = get_jwt_identity()  # Obtiene el ID del usuario actual
        if current_user_id is not None:  # Asegurarse de que el ID del usuario actual no sea None
            notificacion_data = request.get_json()
            notificacion_data["id_usuario"] = current_user_id  # Establece el ID del usuario en los datos de la notificación
            notificacion = NotificacionesModel.from_json(notificacion_data)
            db.session.add(notificacion)
            db.session.commit()
            return notificacion.to_json(), 201
        else:
            # Manejar el caso donde el ID del usuario actual es None
            return jsonify({'message': 'Usuario no autenticado'}), 401


