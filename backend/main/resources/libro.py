from flask_restful import Resource
from flask import request
import json
from .. import db
from main.models import LibrosModel

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
        libros = db.session.query(LibrosModel).get_or_404(id)
        return libros.to_json
        #if int(id) in LIBROS:
        #    return LIBROS [int(id)]
        
        #return "No existe el id", 404
    
    # Eliminar recurso libro
    def delete(self, id):
        libro = db.session.query(LibrosModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return ' Eliminado correctamente ', 204

    
    # Modificar el recurso libro
    def put(self, id):
        libro = db.session.query(LibrosModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(libro, key, value)
        db.session.commit()
        return {'mensaje': 'El libro ha sido editado con éxito', 'libro_modificado': libro.to_json()}, 201

    
class Libros (Resource):
    def get (self):
        return LIBROS
    
    #insertar recurso
    def post(self):
        libro = LibrosModel.from_json(request.get_json())
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201