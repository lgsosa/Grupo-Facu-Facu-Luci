from .. import db

class Reseñas (db.Model):

    __tablereseñas__ = "reseñas"
    id = db.Column(db.Integer, primary_key=True)
    valoracion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(100), nullable = False) 

    #clave foranea

    id_libro = db.Column(db.Integer, db.ForeignKey("libros.id"), nullable=False)

    libros = db.relationship("Libros", back_populates="reseñas", uselist = False, single_parent =True)

    usuarios = db.relationship("Usuario", secondary = "usuario_reseñas", back_populates="reseñas")

    def to_json(self):
        libros_json = {
            "libro": self.id,
            "valoracion ": self.valoracion,
            "comentario": str(self.comentario)
        }   
        return libros_json
    
usuario_reseñas = db.Table(
    "usuario_reseñas",

    db.Column("usuario_id", db.Integer, db.ForeignKey("usuario.id")),
    db.Column ("reseñas_id", db.Integer, db.ForeignKey("reseñas.id"))


)