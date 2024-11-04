from flask_restful import Resource
from flask import request, jsonify
import json
from main.models import NotificacionesModel
from .. import db
from main.auth.decorators import role_required
from flask_jwt_extended import jwt_required, get_jwt_identity


class Notificaciones(Resource):
    @role_required(roles=["admin", "bibliotecario","alumno"])
    def get(self):
        # Página inicial por defecto
        page = 1
        # Cantidad de elementos por página por defecto
        per_page = 5
        
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
    
    # Insertar recurso
    @role_required(roles=["admin", "bibliotecario"])
    def post(self, current_user):
        notificacion_data = request.get_json()
        if "admin" in current_user.roles:
            # El administrador puede enviar notificaciones a todos los usuarios
            notificacion = NotificacionesModel.from_json(notificacion_data)
            db.session.add(notificacion)
            db.session.commit()
            return notificacion.to_json(), 201
        elif "bibliotecario" in current_user.roles:
            # El bibliotecario puede enviar notificaciones a todos excepto a los administradores
            if "admin" not in notificacion_data["roles"]:
                notificacion_data["id_usuario"] = current_user.id
                notificacion = NotificacionesModel.from_json(notificacion_data)
                db.session.add(notificacion)
                db.session.commit()
                return notificacion.to_json(), 201
            else:
                return jsonify({'message': 'No tienes permiso para enviar una notificación a un administrador'}), 403



