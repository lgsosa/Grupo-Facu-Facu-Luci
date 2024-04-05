from flask import Flask, request
from flask_restful import Resource, Api, reqparse

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
        # Agregar la valoración a la base de datos simulada
        valoraciones[id_libro] = valoracion
        return {'message': 'Valoración agregada correctamente'}, 201

class ValoracionAdmin(Resource):
    def get(self):
        return valoraciones
