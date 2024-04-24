from .. import db

class Libros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable = False)
    autor = db.Column(db.String(100), nullable = False) 
    genero = db.Column(db.String(100), nullable = False) 

    def to_json(self):
        libros_json = {
            "id": self.id,
            "titulo": str(self.titulo), 
            "autor": str(self.autor), 
            "genero": str(self.autor),
        }   
        return libros_json
    
    @staticmethod
    def from_json(libro_json):
        id = libro_json.get('id')
        titulo = libro_json.get('titulo')
        autor = libro_json.get('autor')
        genero = libro_json.get('genero')
        return Libros(id=id,
                      titulo=titulo,
                      autor=autor,
                      genero=genero)