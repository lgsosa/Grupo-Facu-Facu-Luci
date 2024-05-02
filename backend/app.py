# Al app.py no vamos a tener que agregarle nada

from main import create_app
import os

#Llamamos a la funcion que retorna la app
app = create_app()

# Hay que hacer push del contexto de la app
# Con esto la app quead disponible en todo los archivos
# Nos permite no tener conflictos con referencias circulares
# Recursividad en las importaciones

app.app_context().push()


from main import db
if __name__ == '__main__':
    db.create_all()
    port = os.getenv('PORT', 5000)  # Si no se ha configurado PORT, se usará el puerto 5001 por defecto
    app.run(debug=True, port=port)