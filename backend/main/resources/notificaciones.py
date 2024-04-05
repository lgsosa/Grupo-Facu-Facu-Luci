from flask_restful import Resource
from flask import request
from .usuario import USUARIOS

NOTIFICACIONES = {
    1: {"notificacion":""}
}

class Notificaciones(Resource):
    def post (self):
        usuarios = request.get_json()
        if int(id) in USUARIOS:
            return NOTIFICACIONES
        
        return "No existe el id", 404