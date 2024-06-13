from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort
import json
from .. import db
from main.models import UsuariosModel
from main.models.reseñas import usuario_reseñas
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

app = Flask(__name__)
api = Api(app)


class Usuario(Resource):
    #obtener recurso
    @role_required(roles=["admin", "bibliotecario"])
    def get(self,id):
        usuario = db.session.query(UsuariosModel).get_or_404(id)
        current_identity = get_jwt_identity()
        if current_identity: 
            return usuario.to_json_complete()
        else:
            return usuario.to_json()

    # Eliminar recurso usuario
    @role_required(roles=["admin"])
    def delete(self, id):
        usuario = db.session.query(UsuariosModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return ' Eliminado correctamente ', 204
    
    # Modificar el recurso usuario
    @role_required(roles=["admin", "bibliotecario"])
    def put(self, id):
        usuario = db.session.query(UsuariosModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(usuario, key, value)
        db.session.commit()
        return {'mensaje': 'El usuario ha sido editado con éxito', 'usuario_modificado': usuario.to_json()}, 201

class Usuarios(Resource): 
    @role_required(roles=["admin", "bibliotecario"])
    def get(self):
        # Página inicial por defecto
        page = 1
        # Cantidad de elementos por página por defecto
        per_page = 10
        
        # No ejecuto el .all()
        usuarios_query = db.session.query(UsuariosModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
       
        # Aplicar filtro si se proporciona el parámetro en la consulta
        if request.args.get('prestamos'):
            usuarios_query = usuarios_query.filter(UsuariosModel.prestamos != None)
        if request.args.get('notificaciones'):
            usuarios_query = usuarios_query.filter(UsuariosModel.notificaciones != None)
        if request.args.get('reseñas'):
            usuarios_query = usuarios_query.filter(UsuariosModel.reseñas != None)
        
        # Obtener valor paginado
        usuarios = usuarios_query.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                        'total': usuarios.total,
                        'pages': usuarios.pages,
                        'page': page
                        })


