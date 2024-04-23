from .. import db 

class Valoracion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    valoracion = db.Column(db.Integer, nullable=False)

    def to_json(self):
        prestamos_json = {
            "id": self.id,
            "nombre_del_libro": str(self.nombre),
            "valoracion": self.valoracion,

        }
        return prestamos_json
