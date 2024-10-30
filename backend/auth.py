import jwt
import datetime
from flask import current_app

SECRET_KEY = 'mi_clave_secreta'

def generar_token(usuario_id):
    payload = {
        'user_id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expira en 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verificar_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido
