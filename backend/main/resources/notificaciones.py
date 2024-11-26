from flask_restful import Resource
from flask import request, jsonify
from main.models.notificaciones import Notificaciones as NotificacionesModel
from .. import db
from main.auth.decorators import role_required
from flask_jwt_extended import jwt_required, get_jwt_identity


class Notificaciones(Resource):
    @role_required(roles=["admin", "bibliotecario", "alumno"])
    def get(self):
        # Página inicial por defecto
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Consulta paginada
        notificaciones = db.session.query(NotificacionesModel).paginate(page=page, per_page=per_page, error_out=False)

        return jsonify({
            'notificaciones': [n.to_json() for n in notificaciones.items],
            'total': notificaciones.total,
            'pages': notificaciones.pages,
            'page': notificaciones.page
        })
    
    # Insertar recurso
    @role_required(roles=["admin", "bibliotecario"])
    def post(self, current_user):
        notificacion_data = request.get_json()

        # Verificar permisos y roles
        if "admin" in current_user.roles:
            notificacion = NotificacionesModel.from_json(notificacion_data)
            db.session.add(notificacion)
            db.session.commit()
            return notificacion.to_json(), 201
        elif "bibliotecario" in current_user.roles:
            # Bibliotecario puede enviar notificaciones solo a usuarios no administradores
            if not notificacion_data.get("roles") or "admin" not in notificacion_data["roles"]:
                notificacion_data["id_usuario"] = current_user.id
                notificacion = NotificacionesModel.from_json(notificacion_data)
                db.session.add(notificacion)
                db.session.commit()
                return notificacion.to_json(), 201
            else:
                return jsonify({'message': 'No puedes enviar una notificación a un administrador'}), 403
