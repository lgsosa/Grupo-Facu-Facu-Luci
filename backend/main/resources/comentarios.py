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
        # Página inicial por defecto
        page = 1
        # Cantidad de elementos por página por defecto
        per_page = 10
        
        # No ejecuto el .all()
        usuarios = db.session.query(ComentariosModel)
        
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

        #if not comentarios:
        #    return jsonify({'message': 'No hay comentarios disponibles'}), 200
        #return jsonify(comentarios), 200

    #insertar recurso
    def post(self):
        comentarios = ComentariosModel.from_json(request.get_json())
        db.session.add(comentarios)
        db.session.commit()
        return comentarios.to_json(), 201
