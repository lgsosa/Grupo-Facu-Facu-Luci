from .. import db 

class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    comentarios = db.Column(db.String(100), nullable = False)

    def to_json(self):
        comentario_json = {
            "id": self.id,
            "nombre": str(self.nombre), 
            "comentario": str(self.comentarios),  # Convierte el comentario a cadena si es necesario
        }
        return comentario_json
