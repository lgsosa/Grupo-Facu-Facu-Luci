from flask_restful import Resource
from flask import request
from .usuario import USUARIOS

SIGN_IN ={
    1: {"nombre":"","apellido":"","correo electronico":"","clave":""}

}

    
class Login(Resource):
    def put(self,id):
        if int(id) in USUARIOS:
            usuarios = USUARIOS (int(id))
            data = request.get_json()
            usuarios.update(data)
            return "",201
        
        return "No existe el id", 404
    
class Sign_in (Resource):
    def post (self):
        list_users = request.get_json()
        if SIGN_IN != list_users:
            USUARIOS[id] = USUARIOS
            return USUARIOS[id],201,"Usuario creado correctamente"
        return "Ya existe un usuario con esas credenciales"