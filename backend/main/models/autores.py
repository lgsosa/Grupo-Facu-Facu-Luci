from .. import db

class Autores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(100), nullable=False)
    libros_titulo = db.Column(db.String(100), nullable=False)

    def to_json(self):
        autores_json = {
            "id": self.id,
            "autor": self.autor,
            "libros_titulo": self.libros_titulo
        }   
        return autores_json
    
    @staticmethod
    def from_json(autores_json):
        id = autores_json.get('id')
        autor = autores_json.get('autor')
        libros_titulo = autores_json.get('libros_titulo')
        return Autores(id=id,
                                autor=autor,
                                libros_titulo=libros_titulo)
