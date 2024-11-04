from .. import db

class Notificaciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notificacion = db.Column(db.String(100), nullable=False)
    
    # Clave foránea
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)

    # Nombre de la relación
    usuario = db.relationship("Usuario", back_populates="notificaciones")

    def to_json_short(self):
        notificaciones_json = {
            "id": self.id,
            "notificacion": self.notificacion
        }
        return notificaciones_json

    def to_json(self):
        notificaciones_json = {
            "id": self.id,
            "notificacion": self.notificacion,
            "usuario": self.usuario.to_json() if self.usuario else None
        }
        return notificaciones_json

    @staticmethod
    def from_json(notificacion_json):
        id = notificacion_json.get('id')
        notificacion = notificacion_json.get('notificacion')
        id_usuario = notificacion_json.get('id_usuario')
        return Notificaciones(
            id=id,
            notificacion=notificacion,
            id_usuario=id_usuario
        )