from flask import Flask, request, jsonify
from flask.views import MethodView

app = Flask(__name__)

comentarios = {}

class Comentario(MethodView):
    def post(self):
        data = request.json
        libro_id = data.get('libro_id')
        comentario = data.get('comentario')
        # Agrega el comentario a la base de datos simulada
        comentarios[libro_id] = comentario
        return jsonify({'message': 'Comentario agregado correctamente'}), 201
    
    def get(self, libro_id):
        comentario = comentarios.get(libro_id)
        if comentario is None:
            return jsonify({'message': 'El libro no tiene comentarios'}), 404
        return jsonify({'comentario': comentario}), 200