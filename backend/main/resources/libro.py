from flask_restful import Resource
from flask import request

LIBROS = {
    1:{"titulo":"","autor":"","genero":""},
    2:{"titulo":"","autor":"","genero":""}
#los nros son los id
}

class Libro (Resource):
    def get(self,id):
        if int(id) in LIBROS:
            return LIBROS [int(id)]
        
        return "No existe el id", 404
    
    def delete(self,id):
        if int(id) in LIBROS:
            del LIBROS [int(id)]
            return "",204
        
        return "No existe el id", 404
    
    def put(self,id):
        if int(id) in LIBROS:
            usuarios = LIBROS [int(id)]
            data = request.get_json()
            usuarios.update(data)
            return "",201
        
        return "No existe el id", 404
    
class Libros (Resource):
    def get (self):
        return LIBROS
    
    def post(self):
        libro = request.get_json()
        id = int(max(LIBROS.key())+1)
        LIBROS[id] = libro
        return LIBROS[id], 201