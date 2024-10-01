from .. import db

class Libros(db.Model):

    __tableusuario__= "libros"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable = False)
    autor = db.Column(db.String(100), nullable = False) 
    genero = db.Column(db.String(100), nullable = False) 

    #nombre de la relacion
    
    prestamos = db.relationship("Prestamos", back_populates="libros", cascade= "all, delete-orphan")
    reseñas = db.relationship("Reseñas", back_populates="libros", cascade= "all, delete-orphan")
    autores = db.relationship("Autores", secondary = "libros_autores", back_populates="libros")

    def to_json(self):
        libros_json = {
            "id": self.id,
            "titulo": str(self.titulo), 
            "autor": str(self.autor), 
            "genero": str(self.autor),
        }   
        return libros_json
    
    def to_json_complete (self):
        prestamos = [prestamo.to_json() for prestamo in self.prestamos]
        reseñas = [reseña.to_json() for reseña in self.reseñas]
        autores = [autores.to_json() for autores in self.autores]
        libros_json = {
            "id": self.id,
            "titulo": str(self.titulo), 
            "autor": str(self.autor), 
            "genero": str(self.genero),
            "prestamos": prestamos,
            "reseñas": reseñas,
            "autores": autores

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