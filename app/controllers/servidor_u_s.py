from ..models.servidor_u_s_model import Servidor
from ..models.salas_model import Salas

from ..database import DatabaseConnection
from flask import request, jsonify

class ServidorController:
    @classmethod
    def create_servidor(cls):
        servidor_data = request.json
        servidor = Servidor(
            id_servidor_u_s = servidor_data.get('id_servidor_u_s'),
            nombre_servidor = servidor_data.get('nombre_servidor'),
        )
        
        Servidor.create(servidor)
        return {'message': 'El Servidor ha sido creado con exito'}, 200
    
    @classmethod
    def get_servidor(cls, id_servidor_u_s):
        servidor = Servidor(id_servidor_u_s=id_servidor_u_s)
        result = servidor.get(servidor)
        if result is not None:
            return result.serialize(), 20
        
    @classmethod
    def get_salas_by_server(cls, server_name):

        salas_objects = Salas.get_by_server(server_name)
        if salas_objects is not None:
            salas = []
            for sala in salas_objects:
                salas.append(sala.serialize())
                
        return jsonify(salas), 200
        
    
    @classmethod
    def update_servidor(cls, id_servidor_u_s):
        servidor_data = request.json
        query= "UPDATE app_discord SET nombre_servidor = %s WHERE servidor_u_s.id servidor_u_s = %s;"
        params = request.args.get('nombre_servidor'), id_servidor_u_s
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Datos del nombre de servidor ha sido actualizados con éxito"}, 200
    @classmethod
    def delete_servidor(id_servidor_u_s):
        query= "DELETE FROM app_discord WHERE servidor_u_s.id_servidor_u_s = %s;"
        params = id_servidor_u_s,
        DatabaseConnection.execute_query(query, params)
 
        return {"msg": "El Servidor eliminado con éxito"}, 204