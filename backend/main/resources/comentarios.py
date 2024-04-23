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

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('libro_id', type=int, required=True, help='ID del libro es obligatorio')
        parser.add_argument('comentario', type=str, required=True, help='Comentario es obligatorio')
        args = parser.parse_args()
        
        libro_id = args['libro_id']
        comentario = args['comentario']
        
        comentarios[libro_id] = comentario
        return {'message': 'Comentario agregado correctamente'}, 201
