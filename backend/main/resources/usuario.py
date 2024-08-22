from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort
import json
from .. import db
from main.models import UsuariosModel
from main.models.reseñas import usuario_reseñas
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required
from sqlalchemy.exc import IntegrityError

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

    @role_required(roles=["admin", "bibliotecario"])
    def delete(self, id):
        usuario = db.session.query(UsuariosModel).get_or_404(id)

        if usuario.rol in ["admin", "bibliotecario"]:
            abort(403, message="No se puede eliminar a otros administradores o bibliotecarios")

        db.session.delete(usuario)
        db.session.commit()
        return {'mensaje': 'Eliminado correctamente', 'usuario_eliminado': usuario.to_json()}, 200
        

    # Modificar el recurso usuario
    @jwt_required()
    def put(self, id):
        usuario = db.session.query(UsuariosModel).get_or_404(id)

        if usuario.rol in ["admin", "bibliotecario"]:
            abort(403, message="No se puede editar a otros administradores o bibliotecarios")

        data = request.get_json()
        for key, value in data.items():
            setattr(usuario, key, value)
        db.session.commit()
        return {'mensaje': 'Editado correctamente', 'usuario_editaro': usuario.to_json()}, 200

    """ if current_user.rol not in ["admin", "bibliotecario"]:
                abort(403, message="No tienes permiso para editar otros usuarios")
    current_user = UsuariosModel.query.get(current_user_id)#dsps agregar         current_user_id = get_jwt_identity()
        if usuario.rol in ["admin", "bibliotecario"]:
                abort(403, message="No se puede editar a otros administradores o bibliotecarios")

        if current_user_id != str(usuario.id):
            if usuario.rol in ["alumno", "users"]:
                abort(403, message="No tienes permiso para editar otros usuarios")

        data = request.get_json()
        for key, value in data.items():
            setattr(usuario, key, value)
        
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            if "UNIQUE constraint failed" in str(e):
                abort(400, message="El correo electrónico ya está en uso")
            else:
                abort(500, message="Error interno del servidor")

        return {'mensaje': 'El usuario ha sido editado con éxito', 'usuario_modificado': usuario.to_json()}, 201 """
    
    @role_required(roles=["admin", "bibliotecario"])
    @jwt_required()
    def update_usuario(self, usuario_id):
        usuario = db.session.query(UsuariosModel).get_or_404(usuario_id)
        data = request.get_json()

        if 'rol' in data and data['rol'] == "alumno":
            usuario.rol = "alumno"

        for key, value in data.items():
            setattr(usuario, key, value)
        
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            if "UNIQUE constraint failed" in str(e):
                abort(400, message="El correo electrónico ya está en uso")
            else:
                abort(500, message="Error interno del servidor")
        
        return {'mensaje': 'El usuario ha sido actualizado con éxito', 'usuario_modificado': usuario.to_json()}, 200


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


