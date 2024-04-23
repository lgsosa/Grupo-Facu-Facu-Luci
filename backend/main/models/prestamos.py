from .. import db

class Prestamos (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario  = db.Column(db.String(100), nullable = False)
    cantidad = db.Column(db.Integer, nullable=False)
    tiempo_de_devolucion = db.Column(db.Integer, nullable=False)


    def to_json(self):
        prestamos_json = {
            "id": self.id,
            "usuario": self.usuario,
            "cantidad": self.cantidad,
            "tiempo_de_devolucion": self.tiempo_de_devolucion
        }   
        return prestamos_json