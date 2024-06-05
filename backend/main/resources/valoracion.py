from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
from .. import db
from main.models import Valoraciones_Admin_Model
import json
from flask_jwt_extended import jwt_required
from main.auth.decorators import role_required

app = Flask(__name__)
api = Api(app)

# Base de datos simulada para las valoraciones
valoraciones = {}

# Parser para las solicitudes POST
parser = reqparse.RequestParser()
parser.add_argument('id_libro', type=int, help='ID del libro')
parser.add_argument('valoracion', type=int, help='Valoración del libro')

class Valoracion(Resource):
    @jwt_required(optional=True)
    def post(self):
        args = parser.parse_args()
        id_libro = args['id_libro']
        valoracion = args['valoracion']
        valoraciones[id_libro] = valoracion
        return {"id_libro": id_libro, "valoracion": valoracion}, 201


class ValoracionAdmin(Resource):
    @role_required(roles = ["admin"])
    def get(self):
        # Página inicial por defecto
        page = 1
        # Cantidad de elementos por página por defecto
        per_page = 10
        
        # No ejecuto el .all()
        usuarios = db.session.query(Valoraciones_Admin_Model)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        
        # Obtener valor paginado
        usuarios = usuarios.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                        'total': usuarios.total,
                        'pages': usuarios.pages,
                        'page': page
                        })

