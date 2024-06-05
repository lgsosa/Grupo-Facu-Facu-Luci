from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuariosModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

#Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')

#Método de logueo
@auth.route('/login', methods=['POST'])
def login():

    usuario = db.session.query(UsuariosModel).filter(UsuariosModel.correo_electronico == request.get_json().get("correo_electronico")).first_or_404()
    #Valida la contraseña
    if usuario.validate_password(request.get_json().get("password")):
        #Genera un nuevo token
        #Pasa el objeto animal como identidad
        access_token = create_access_token(identity=usuario)
        #Devolver valores y token
        data = {
            'id': str(usuario.id),
            'correo_electronico': usuario.correo_electronico,
            'access_token': access_token
        }

        return data, 200
    else:
        return 'Incorrect password', 401

#Método de registro
@auth.route('/register', methods=['POST'])
def register():
    # Obtener animal
    usuario = UsuariosModel.from_json(request.get_json())
    # Verificar si el mail ya existe en la db, scalar() para saber la cantidad de ese email
    exists = db.session.query(UsuariosModel).filter(UsuariosModel.correo_electronico == usuario.correo_electronico).scalar() is not None
    print("¿Correo electrónico existente?", exists)
    if exists:
        return 'msg: The email is duplicate', 409
    else:
        try:
            # Agregar animal a DB
            db.session.add(usuario)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json(), 201
