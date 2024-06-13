from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


#importar Flask Mail
from flask_mail import Mail
#importar Flask JWT
#iniciamos restful

api = Api()

#inicializamos SQLAlchemy
db = SQLAlchemy()

#Inicializar Migrate
migrate = Migrate()

#Inicializar JWT
jwt = JWTManager()

#Inicializar 
mailsender = Mail()

#este metodo create_app inicializa la app y todos los modulos

def create_app():
    #Inicio flask
    app = Flask(__name__)

    #cargamos las variables del archivo .env
    load_dotenv()

    #Si no existe el archivo de base de datos crearlo (solo válido si se utiliza SQLite)

    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #Url de configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

    import main.resources as resources

    api.add_resource(resources.UsuariosResources, '/usuarios')

    api.add_resource(resources.UsuarioResources, "/usuario/<id>")#ruta

    api.add_resource(resources.LibroResources, "/libro/<id>") #ruta

    api.add_resource(resources.LibrosResources, "/libros") #ruta

    api.add_resource(resources.PrestamosResource, "/prestamos") #ruta

    api.add_resource(resources.PrestamoResource, "/prestamo/<id>") #ruta

    api.add_resource(resources.NotificacionesResource, "/notificacion") #ruta

    api.add_resource(resources.ValoracionResource, "/valoracion") #ruta

    api.add_resource(resources.ValoracionAdminResource, "/valoraciones") #ruta

    api.add_resource(resources.ComentarioResource, "/comentarios") #ruta

    api.add_resource(resources.AutoresResource, "/autores") #ruta

    api.add_resource(resources.AutorResource, "/autor/<id>") #ruta

    api.add_resource(resources.ReseñasResource, "/reseñas/<id>") #ruta


    api.init_app(app)

    #Cargar clave secreta
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    #Cargar tiempo de expiracion de los tokens
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))
    jwt.init_app(app)
    
    from main.auth import routes
    #Import blueprint
    app.register_blueprint(routes.auth)

    # Configuración de mail
    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))  # Convertir a entero
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'  # Convertir a booleano
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')
    app.config['MAIL_TEMPLATE_FOLDER'] = 'templates'  # Directorio de plantillas
    #Inicializar en app
    mailsender.init_app(app)

    return app  