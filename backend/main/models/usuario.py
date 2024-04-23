from .. import db 

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.Integer, nullable=False)
    correo_electronico = db.Column(db.String(100), nullable = False)


    def to_json(self):
        usuario_json = {
            "id": self.id,
            "nombre y apellido ": str(self.nombre),
            "telefono": self.telefono,
            "correo electronico": str(self.correo_electronico),

        }
        return usuario_json


