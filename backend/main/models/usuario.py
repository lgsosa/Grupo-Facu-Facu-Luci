from .. import db 

class Usuario(db.Model):

    __tableusuario__= "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable = False)
    telefono = db.Column(db.Integer)
    correo_electronico = db.Column(db.String(100),nullable = False)

    #nombre de la relacion
    
    prestamos = db.relationship("Prestamos", back_populates="usuario", cascade= "all, delete-orphan")
    notificaciones = db.relationship("Notificaciones", back_populates="usuario", cascade= "all, delete-orphan")
    reseñas = db.relationship("Reseñas", secondary = "usuario_reseñas", back_populates="usuarios")


    def to_json(self):
        usuario_json = {
            "id": self.id,
            "nombre y apellido ": str(self.nombre),
            "telefono": self.telefono,
            "correo electronico": str(self.correo_electronico),

        }
        return usuario_json
    
    def to_json_complete (self):
        prestamos = [prestamo.to_json() for prestamo in self.prestamos]
        notificaciones = [notificaciones.to_json() for notificaciones in self.notificaciones]
        reseñas = [reseñas.to_json() for reseñas in self.reseñas]
        usuario_json = {
            "id": self.id,
            "nombre y apellido ": str(self.nombre),
            "telefono": self.telefono,
            "correo electronico": str(self.correo_electronico),
            "prestamos": prestamos,
            "notificaciones" : notificaciones,
            "reseñas": reseñas

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

