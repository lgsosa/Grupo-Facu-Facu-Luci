from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuariosModel
from datetime import timedelta
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
#Importar funcion de envío de mail
from main.mail.functions import sendMail

#Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')  
#Método de logueo
@auth.route('/login', methods=['POST'])
def login():
    usuario = db.session.query(UsuariosModel).filter(UsuariosModel.correo_electronico == request.get_json().get("correo_electronico")).first_or_404()
    # Valida la contraseña
    if usuario.validate_password(request.get_json().get("password")):
        # Genera un nuevo token con tiempo de expiración de 30 minutos
        access_token = create_access_token(identity=usuario, expires_delta=timedelta(minutes=30))
        
        # Devolver valores y token
        data = {
            'id': str(usuario.id),
            'correo_electronico': usuario.correo_electronico,
            'access_token': access_token
        }
        return data, 200
    else:
        return 'Incorrect password', 401


# Método de registro
@auth.route('/register', methods=['POST'])
def register():
    # Obtener usuario
    usuario = UsuariosModel.from_json(request.get_json())
    # Verificar si el correo electrónico ya existe en la base de datos
    exists = db.session.query(UsuariosModel).filter(UsuariosModel.correo_electronico == usuario.correo_electronico).scalar() is not None
    if exists:
        return 'Duplicated email', 409
    else:
        try:
            # Agregar usuario a la base de datos
            db.session.add(usuario)
            db.session.commit()
            # Enviar correo de bienvenida
            send = sendMail([usuario.correo_electronico], "Welcome!", 'register', usuario=usuario)
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json(), 201
