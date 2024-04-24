from flask import jsonify, Flask, request
from flask_restful import Resource, Api, reqparse
import json
from .. import db
from main.models import ComentariosModel

app = Flask(__name__)
api = Api(app)

comentarios = {}
 
class Comentario(Resource):
    def get(self):
        comentarios = db.session.query(ComentariosModel).get_or_404(id)
        return comentarios.to_json

        #if not comentarios:
        #    return jsonify({'message': 'No hay comentarios disponibles'}), 200
        #return jsonify(comentarios), 200

    #insertar recurso
    def post(self):
        comentarios = ComentariosModel.from_json(request.get_json())
        db.session.add(comentarios)
        db.session.commit()
        return comentarios.to_json(), 201
