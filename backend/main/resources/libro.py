from flask_restful import Resource
from flask import request

LIBROS = {
    1:{"titulo":" El guardian de la biblia del Diablo ","autor":" Richard Dubell ","genero":" misterio "},
    2:{"titulo":" El club de los psicopatas ","autor":" John Katzenbach","genero":" terror psicologico "},
    3:{"titulo":" La historia del loco ","autor":" John Katzenbach","genero":" terror psicologico "},
    4:{"titulo":" Will Grayson, Will Grayson  ","autor":" John Green , David Leuthan","genero":" novela "},
    5:{"titulo":" Buscando a Alaska  ","autor":" John Green , David Leuthan","genero":" novela "},
    6:{"titulo":" Despues de ti ","autor":" Jojo Moyes ","genero":" novela "},
    7:{"titulo":" Yo antes de ti ","autor":" Jojo Moyes ","genero":" novela "},
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
    
    def put(self, id):
        if int(id) in LIBROS:
            libros_antes = LIBROS.copy()  # Hacer una copia de la lista de libros antes de la edición
            libro = LIBROS[int(id)]
            data = request.get_json()
            libro.update(data)
            return {'mensaje': 'El libro ha sido editado con éxito', 'libros_antes': libros_antes, 'libros_después': LIBROS}, 201
        return "No existe el id", 404
    
class Libros (Resource):
    def get (self):
        return LIBROS
    
    def post(self):
        usuario = request.get_json()
        id = int(max(LIBROS.keys(), default=0)) + 1
        LIBROS[id] = usuario
        return {'mensaje': 'El libro ha sido añadido con éxito'}, 201