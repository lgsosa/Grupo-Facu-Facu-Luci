from flask_restful import Resource
from flask import request
from .usuario import USUARIOS

SIGN_IN ={
    1: {"nombre":" Facundo ","apellido":" Mangione ","correo electronico":" f.mangione@um.edu.ar ","clave":" 120803"},
    2: {"nombre":" Materia ","apellido":" De Calcuta ","correo electronico":" mariateresadecalculta@gmail.com ","clave":" diositoamen1 "}
}

    
class Login(Resource):
    def put(self,id):
        if int(id) in USUARIOS:
            usuarios_antes = SIGN_IN.copy()
            usuarios = USUARIOS [int(id)]
            data = request.get_json()
            usuarios.update(data)
            return {'mensaje': 'El usuario ha sido editado con éxito', 'libros_antes': usuarios_antes, 'libros_después': SIGN_IN}, 201
        return "No existe el id", 404

class Sign_in (Resource):
    def post(self):
        usuario = request.get_json()
        id = int(max(SIGN_IN.keys(), default=0)) + 1
        SIGN_IN[id] = usuario
        return {'mensaje': 'El usuario ha sido crreado con éxito'}, 201
    
    