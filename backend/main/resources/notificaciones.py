from flask_restful import Resource
from flask import request
from .usuario import USUARIOS

NOTIFICACIONES = {
    1: {"notificacion": " Por favor pase por secretaria cuando sea posible: "},
    2: {"notificacion": " Se olvido sus pertenencias en la biblioteca "}
}


class Notificaciones(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get('id')
        notification = data.get('notificacion')

        if user_id in USUARIOS:
            NOTIFICACIONES[user_id] = {"notificacion": notification}
            return {"message": "Notificación creada con éxito para el usuario {}".format(user_id)}, 201
        else:
            return "El usuario no existe", 404
