from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from .. import db
from main.models import Valoraciones_Admin_Model
from flask_jwt_extended import jwt_required

app = Flask(__name__)
api = Api(app)

# Parser para las solicitudes POST
parser = reqparse.RequestParser()
parser.add_argument('id_libro', type=int, required=True, help='ID del libro')
parser.add_argument('nombre_del_libro', type=str, required=True, help='Nombre del libro')
parser.add_argument('valoracion', type=int, required=True, help='Valoración del libro')


class Valoracion(Resource):
    @jwt_required(optional=True)
    def post(self):
        args = parser.parse_args()
        id_libro = args['id_libro']  # Este es el ID del libro
        nombre = args['nombre_del_libro']  # Nombre del libro
        valoracion = args['valoracion']  # Valoración

        # Crear una nueva instancia del modelo
        nueva_valoracion = Valoraciones_Admin_Model(nombre=nombre, valoracion=valoracion)
        
        # Aquí, probablemente quieras asociar la valoración con el libro usando id_libro,
        # dependiendo de cómo esté estructurado tu modelo

        db.session.add(nueva_valoracion)
        db.session.commit()  # Guardar cambios en la base de datos

        return {"id": nueva_valoracion.id, "nombre": nueva_valoracion.nombre, "valoracion": nueva_valoracion.valoracion}, 201


class ValoracionAdmin(Resource):
    def get(self):
        page = 1
        per_page = 5
        valoraciones_query = db.session.query(Valoraciones_Admin_Model)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        valoraciones_paginated = valoraciones_query.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({
            'valoraciones': [valoracion.to_json() for valoracion in valoraciones_paginated.items],
            'total': valoraciones_paginated.total,
            'pages': valoraciones_paginated.pages,
            'page': page
        })

api.add_resource(Valoracion, '/valoracion')
api.add_resource(ValoracionAdmin, '/valoraciones')
