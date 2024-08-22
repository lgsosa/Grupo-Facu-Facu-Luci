from .. import db
from werkzeug.security import generate_password_hash, check_password_hash #importo estas 2 funciones para la pass

class Usuario(db.Model):

    __tablename__= "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable = False)
    telefono = db.Column(db.Integer)
    correo_electronico = db.Column(db.String(64),unique=True, index = True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    rol = db.Column(db.String(10), nullable =False, server_default = "users")

    #Getter de la contraseña plata no permite leerla
    @property
    def plain_password(self):
        raise AttributeError("Password cant be read ")
    #Setter de la contraseña toma un valor en texto plano.
    #calcula el hash y lo guarda en el atributo password.
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    #Metodo que compara una contraseña en texto plano con el hash guardado en la db
    def validate_password(self,password):
        return check_password_hash(self.password, password)




    #nombre de la relaciones
    
    prestamos = db.relationship("Prestamos", back_populates="usuario", cascade= "all, delete-orphan")
    notificaciones = db.relationship("Notificaciones", back_populates="usuario", cascade= "all, delete-orphan")
    reseñas = db.relationship("Reseñas", secondary = "usuario_reseñas", back_populates="usuarios")



    def to_json(self):
        usuario_json = {
            "id": self.id,
            "nombre ": str(self.nombre),
            "telefono": self.telefono,
            "correo_electronico": str(self.correo_electronico),

        }
        return usuario_json
    
    def to_json_complete (self):
        prestamos = [prestamo.to_json() for prestamo in self.prestamos]
        notificaciones = [notificaciones.to_json() for notificaciones in self.notificaciones]
        reseñas = [reseñas.to_json() for reseñas in self.reseñas]
        usuario_json = {
            "id": self.id,
            "nombre": str(self.nombre),
            "telefono": self.telefono,
            "correo_electronico": str(self.correo_electronico),
            "prestamos": prestamos,
            "notificaciones" : notificaciones,
            "reseñas": reseñas

        }
        return usuario_json


    @staticmethod 
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        telefono = usuario_json.get('telefono')
        correo_electronico = usuario_json.get('correo_electronico')
        password = usuario_json.get("password")
        rol = usuario_json.get ("rol")
        return Usuario(id=id,
                    nombre=nombre,
                    telefono=telefono,
                    correo_electronico=correo_electronico,
                    plain_password = password,
                    rol = rol
                    )

