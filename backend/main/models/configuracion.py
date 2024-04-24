from .. import db

class Configuracion (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable = False)
    autor = db.Column(db.String(100), nullable = False) 
    genero = db.Column(db.String(100), nullable = False) 

    def to_json(self):
        libros_json = {
            "libros": self.id,
            "notificaciones": str(self.titulo), 
            "prestamos": str(self.autor), 
            "valoracion ": str(self.autor),
        }   
        return libros_json