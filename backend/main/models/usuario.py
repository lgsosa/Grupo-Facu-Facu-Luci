from .. import db 

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable = False)
    telefono = db.Column(db.Integer)
    correo_electronico = db.Column(db.String(100),nullable = False)


    def to_json(self):
        usuario_json = {
            "id": self.id,
            "nombre y apellido ": str(self.nombre),
            "telefono": self.telefono,
            "correo electronico": str(self.correo_electronico),

        }
        return usuario_json
 #no funciona el put

    @staticmethod 
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre y apellido')
        telefono = usuario_json.get('telefono')
        correo_electronico = usuario_json.get('correo electronico')
        return Usuario(id=id,
                    nombre=nombre,
                    telefono=telefono,
                    correo_electronico=correo_electronico)

