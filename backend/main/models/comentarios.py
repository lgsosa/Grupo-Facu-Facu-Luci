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
    
    @staticmethod
    def from_json(comentario_json):
        id = comentario_json.get('id')
        nombre = comentario_json.get('nombre')
        comentarios = comentario_json.get('comentario')
        return Comentarios(id=id,
                           nombre=nombre,
                           comentarios=comentarios)