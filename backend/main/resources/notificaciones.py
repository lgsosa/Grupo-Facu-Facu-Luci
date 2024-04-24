from flask_restful import Resource
from flask import request
from .usuario import USUARIOS
import json
from main.models import NotificacionesModel
from .. import db

NOTIFICACIONES = {
    1: {"notificacion": " Por favor pase por secretaria cuando sea posible: "},
    2: {"notificacion": " Se olvido sus pertenencias en la biblioteca "}
}


class Notificaciones(Resource):
    def get(self,id):
        notificaciones = db.session.query(NotificacionesModel).get_or_404(id)
        return notificaciones.to_json

    #insertar recurso
    def post(self):
        notificaciones = NotificacionesModel.from_json(request.get_json())
        db.session.add(notificaciones)
        db.session.commit()
        return notificaciones.to_json(), 201
