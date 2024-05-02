from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
from .. import db
from main.models import UsuariosModel

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
        usuario = db.session.query(UsuariosModel).get_or_404(id)
        return usuario.to_json_complete()


       # if int(id) in USUARIOS:
        #    return USUARIOS[int(id)]
        #return "No existe el id", 404
    
    # Eliminar recurso usuario
    def delete(self, id):
        usuario = db.session.query(UsuariosModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return ' Eliminado correctamente ', 204

    
    # Modificar el recurso libro
    def put(self, id):
        usuario = db.session.query(UsuariosModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(usuario, key, value)
        db.session.commit()
        return {'mensaje': 'El usuario ha sido editado con éxito', 'usuario_modificado': usuario.to_json()}, 201


class Usuarios(Resource):
    def get(self):
        return USUARIOS
    
    #insertar recurso
    def post(self):
        usuario = UsuariosModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201

