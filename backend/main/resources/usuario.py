from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

USUARIOS = {
    1: {
        "nombre y apellido completo": "Facundo Mesa",
        "telefono": "2615486975",
        "correo electronico": "fa.mesa@alumno.um.edu.ar"
    },
    2: {
        "nombre y apellido completo": "Facundo Mangione",
        "telefono": "2614961572",
        "correo electronico": "f.mangione@alumno.um.edu.ar"
    },
    3: {
        "nombre y apellido completo": "Luciana Sosa",
        "telefono": "2612740142",
        "correo electronico": "lg.sosa@alumno.um.edu.ar"
    },
    4: {
        "nombre y apellido completo": "Teresa de Calcuta",
        "telefono": "2611497589",
        "correo electronico": "mariateresadecalculta@gmail.com"
    }
}

class Usuario(Resource):
    def get(self,id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        return "No existe el id", 404
    
    def delete(self,id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)]
            return "Usuario Eliminado", 204
        return "No existe el id", 404
    
    def put(self, id):
        if int(id) in USUARIOS:
            usuario = USUARIOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return ' Usuario actualizado correctamente', 201
        return '', 404

class Usuarios(Resource):
    def get(self):
        return USUARIOS
    
    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys(), default=0)) + 1
        USUARIOS[id] = usuario
        return {'mensaje': 'El animal ha sido creado con éxito'}, 201

