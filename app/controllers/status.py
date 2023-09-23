from ..models.status_model import Status
from database import DatabaseConnection
from flask import request

class StatusController:
    @classmethod
    def create_statu(cls):
        status_data = request.json
        status = Status(
            id_status = status_data.get('id_status'),
            status_name = status_data.get('status_name'),
        )
        
        Status.create(status)
        return {'message': 'El Status ha sido creado con exito'}, 200
    
    @classmethod
    def get_statu(cls, id_status):
        status = Status(id_status=id_status)
        result = status.get(status)
        if result is not None:
            return result.serialize(), 20
        
    @classmethod
    def get_status(cls):
        status_objects = Status.get_all()
        status = []
        for status in status_objects:
            status.append(status.serialize())
        return status, 200
    
    @classmethod
    def update_status(cls, id_status):
        status_data = request.json
        query= "UPDATE app_discord SET status_name = %s WHERE status.id status = %s;"
        params = request.args.get('status_name'), id_status
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Datos del nombre de status ha sido actualizados con éxito"}, 200
    @classmethod
    def delete_status(id_status):
        query= "DELETE FROM app_discord WHERE status.id_status = %s;"
        params = id_status
        DatabaseConnection.execute_query(query, params)
 
        return {"msg": "El status ha sido eleminado con éxito"}, 204