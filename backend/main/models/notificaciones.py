from .. import db

class Notificaciones (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notificacion  = db.Column(db.String(100), nullable = False)



    def to_json(self):
        notificaciones_json = {
            "id": self.id,
            "notificacion": self.notificacion
        }   
        return notificaciones_json
    
    @staticmethod
    def from_json(notificacion_json):
        id = notificacion_json.get('id')
        notificacion = notificacion_json.get('notificacion')
        return Notificaciones(id=id, notificacion=notificacion)