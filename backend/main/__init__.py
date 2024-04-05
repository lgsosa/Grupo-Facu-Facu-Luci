from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

#iniciamos restful

api = Api()

#este metodo create_app inicializa la app y todos los modulos

def create_app():
    #Inicio flask
    app = Flask(__name__)

    #cargamos las variables del archivo .env
    load_dotenv()

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