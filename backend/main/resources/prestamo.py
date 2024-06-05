from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import PrestamosModel
from flask_jwt_extended import jwt_required
from main.auth.decorators import role_required


class Prestamo (Resource):
    @jwt_required(optional=True)
    def get(self,id):
        prestamos = db.session.query(PrestamosModel).get_or_404(id)
        return prestamos.to_json_short()
     #   if int(id) in PRESTAMOS:
      #      return PRESTAMOS [int(id)]
        
       # return "No existe el id", 404
    
    # Modificar el recurso préstamo
    @role_required(roles = ["admin"])
    def put(self, id):
        prestamo = db.session.query(PrestamosModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(prestamo, key, value)
        db.session.commit()
        return {'mensaje': 'El prestamo ha sido editado con éxito', 'prestamo_modificado': prestamo.to_json()}, 201

    # Eliminar recurso préstamo
    @role_required(roles = ["admin"])
    def delete(self, id):
        prestamo = db.session.query(PrestamosModel).get_or_404(id)
        db.session.delete(prestamo)
        db.session.commit()
        return ' Eliminado correctamente ', 204


class Prestamos (Resource):
    @role_required(roles = ["admin"])
    def get(self):
        # Página inicial por defecto
        page = 1
        # Cantidad de elementos por página por defecto
        per_page = 10
        
        # No ejecuto el .all()
        usuarios_execute = db.session.query(PrestamosModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        
        # Obtener valor paginado
        usuarios = usuarios_execute.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                        'total': usuarios.total,
                        'pages': usuarios.pages,
                        'page': page
                        })
    
    #insertar recurso
    @role_required(roles=["admin"])
    def post(self):
        data = request.get_json()
        print(data)  # Verificar los datos recibidos

        # Verificar que los campos necesarios existan en los datos JSON
        required_fields = ['nombre_usuario', 'cantidad', 'tiempo_de_devolucion', 'id_usuario', 'id_libro']
        for field in required_fields:
            if field not in data:
                return {'message': f'{field} is required'}, 400

        prestamo = PrestamosModel.from_json(data)
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201
    

