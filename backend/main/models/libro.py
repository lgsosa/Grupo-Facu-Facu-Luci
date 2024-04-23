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