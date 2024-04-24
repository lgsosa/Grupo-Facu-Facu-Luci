from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

#iniciamos restful

api = Api()

#inicializamos SQLAlchemy
db = SQLAlchemy()

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

    api.add_resource(resources.LibrosResources, "/libros") #ruta

    api.add_resource(resources.LibroResources, "/libro/<id>") #ruta

    api.add_resource(resources.LoginResources, "/login/<id>") #ruta

    api.add_resource(resources.Sign_inResources, "/signin") #ruta

    api.add_resource(resources.PrestamosResource, "/prestamos") #ruta

    api.add_resource(resources.PrestamoResource, "/prestamo/<id>") #ruta

    api.add_resource(resources.NotificacionesResource, "/notificacion") #ruta

    api.add_resource(resources.ConfiguracionResource, "/configuracion/<id>") #ruta

    api.add_resource(resources.ValoracionResource, "/valoracion") #ruta

    api.add_resource(resources.ValoracionAdminResource, "/valoraciones") #ruta

    api.add_resource(resources.ComentarioResource, "/comentarios") #ruta

    api.init_app(app)

    return app  