from flask_restful import Resource
from flask import request,jsonify
from .. import db
from main.models import AutoresModel
from main.auth.decorators import role_required
from flask_jwt_extended import jwt_required, get_jwt_identity


class Autor(Resource):
    @jwt_required(optional=True)
    def get(self, id):
        autor = db.session.query(AutoresModel).get_or_404(id)
        return autor.to_json()
        # if int(id) in AUTORES:
        #     return AUTORES[int(id)]
        # return "No existe el id", 404

    @role_required(roles=["admin"])
    def delete(self, id):
        autores = db.session.query(AutoresModel).get_or_404(id)
        db.session.delete(autores)
        db.session.commit()
        return {"mensaje": ' Eliminado correctamente '},204
    
    @role_required(roles=["admin"])
    def put(self, id):
        autor = db.session.query(AutoresModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(autor, key, value)
        db.session.commit()
        return {'mensaje': 'El autor ha sido editado con éxito', 'autor_modificado': autor.to_json()}, 201

class Autores(Resource):
    @jwt_required(optional=True)
    def get(self):
        # Página inicial por defecto
        page = 1
        # Cantidad de elementos por página por defecto
        per_page = 10
        
        # No ejecuto el .all()
        usuarios = db.session.query(AutoresModel)
        
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
    
    #insertar recurso
    @role_required(roles=["admin"])
    def post(self):
        usuario = AutoresModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201


# Diccionario de autores
AUTORES = {
    1: {"nombre_autor": "Richard Dubell", "libros_titulo": ["El guardian de la biblia del Diablo"]},
    2: {"nombre_autor": "John Katzenbach", "libros_titulo": ["El club de los psicopatas", "La historia del loco"]},
    3: {"nombre_autor": "John Green", "libros_titulo": ["Will Grayson, Will Grayson", "Buscando a Alaska"]},
    4: {"nombre_autor": "David Leuthan", "libros_titulo": ["Will Grayson, Will Grayson", "Buscando a Alaska"]},
    5: {"nombre_autor": "Jojo Moyes", "libros_titulo": ["Despues de ti", "Yo antes de ti"]},
}