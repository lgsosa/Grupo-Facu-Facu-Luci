from .. import db

class Prestamos (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario  = db.Column(db.String(100), nullable = False)
    cantidad = db.Column(db.Integer, nullable=False)
    tiempo_de_devolucion = db.Column(db.Integer, nullable=False)

    #clave foranea

    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    id_libro = db.Column(db.Integer, db.ForeignKey("libros.id"), nullable=False)

    #nombre de la relacion
    
    usuario = db.relationship("Usuario", back_populates="prestamos", uselist = False, single_parent =True)
    libros = db.relationship("Libros", back_populates="prestamos", uselist = False, single_parent =True)

    def to_json_short(self):
        prestamos_json = {
            "id": self.id,
            "nombre_usuario": str(self.nombre_usuario),
            "cantidad": self.cantidad,
            "tiempo_de_devolucion": (self.tiempo_de_devolucion),
        }   
        return prestamos_json


    def to_json(self):
        prestamos_json = {
            "id": self.id,
            "nombre_usuario": str(self.nombre_usuario),
            "cantidad": self.cantidad,
            "tiempo_de_devolucion": (self.tiempo_de_devolucion),
            "usuario" : self.usuario.to_json(), #le paso el usuario pasado a JSON / tengo todos los datos juntos 
            "libros" :self.libros.to_json()
        }   
        return prestamos_json
    

    @staticmethod
    def from_json(prestamos_json):
        id = prestamos_json.get('id')
        nombre_usuario = prestamos_json.get('nombre_usuario')
        cantidad = prestamos_json.get('cantidad')
        tiempo_de_devolucion = prestamos_json.get('tiempo_de_devolucion')
        id_usuario = prestamos_json.get('id_usuario')
        id_libro = prestamos_json.get('id_libro')
        return Prestamos(
            id=id,
            nombre_usuario=nombre_usuario,
            cantidad=cantidad,
            tiempo_de_devolucion=tiempo_de_devolucion,
            id_usuario=id_usuario,
            id_libro=id_libro
        )