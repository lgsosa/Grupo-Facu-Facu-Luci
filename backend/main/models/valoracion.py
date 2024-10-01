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
    
    @staticmethod
    def from_json(valoracion_json):
        id = valoracion_json.get('id')
        nombre = valoracion_json.get('nombre_del_libro')
        valoracion = valoracion_json.get('valoracion')
        return Valoracion(id=id,
                          nombre=nombre,
                          valoracion=valoracion)