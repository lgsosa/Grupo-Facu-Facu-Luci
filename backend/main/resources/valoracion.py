from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from .. import db
from main.models import Valoraciones_Admin_Model
import json

app = Flask(__name__)
api = Api(app)

# Base de datos simulada para las valoraciones
valoraciones = {}

# Parser para las solicitudes POST
parser = reqparse.RequestParser()
parser.add_argument('id_libro', type=int, help='ID del libro')
parser.add_argument('valoracion', type=int, help='Valoración del libro')

class Valoracion(Resource):
    def post(self):
        args = parser.parse_args()
        id_libro = args['id_libro']
        valoracion = args['valoracion']
        valoraciones[id_libro] = valoracion
        return {"id_libro": id_libro, "valoracion": valoracion}, 201


class ValoracionAdmin(Resource):
    def get(self):
        valoraciones = db.session.query(Valoraciones_Admin_Model).get_or_404(id)
        return valoraciones.to_json
        #return valoraciones 

