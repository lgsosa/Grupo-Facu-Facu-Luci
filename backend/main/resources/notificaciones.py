from flask_restful import Resource
from flask import request
from .usuario import USUARIOS

NOTIFICACIONES = {
    1: {"notificacion": ""}
}

class Notificaciones(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get('id')  # Suponiendo que el id se pasa en la solicitud JSON
        if int(user_id) in USUARIOS:
            return NOTIFICACIONES
        else:
            return "El usuario no existe", 404
