from .. import db

class Notificaciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notificacion = db.Column(db.String(100), nullable=False)
    
    # Clave foránea
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)

    # Nombre de la relación
    usuario = db.relationship("Usuario", back_populates="notificaciones")

    def to_json_short(self):
        return {
            "id": self.id,
            "notificacion": self.notificacion
        }

    def to_json(self):
        return {
            "id": self.id,
            "notificacion": self.notificacion,
            "usuario": self.usuario.to_json() if self.usuario else None
        }

    @staticmethod
    def from_json(notificacion_json):
        return Notificaciones(
            id=notificacion_json.get('id'),
            notificacion=notificacion_json.get('notificacion'),
            id_usuario=notificacion_json.get('id_usuario')
        )
