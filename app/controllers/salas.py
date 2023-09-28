from ..models.salas_model import Salas

from flask import request

class SalasController:
    @classmethod
    def create_sala(cls):
        sala_data = request.json
        sala = Salas(
            id_salas = sala_data.get('id_salas'),
            nombre_sala = sala_data.get('nombre_sala'),
            id_servidor_u_s = sala_data.get('id_servidor_u_s'),
            usuario_adm = sala_data.get('usuario_adm')
        )
        
        Salas.create(sala)
        return {'message': 'La Sala ha sido creado con exito'}, 200
    
    @classmethod
    def get_sala(cls, id_salas):
        sala = Salas(id_salas=id_salas)
        result = sala.get(sala)
        if result is not None:
            return result.serialize(), 20
        
    @classmethod
    def get_salas(cls):
        sala_objects = Salas.get_all()
        salas = []
        for sala in sala_objects:
            sala.append(sala.serialize())
        return salas, 200
    
    @classmethod
    def update_sala(cls, id_salas):
        sala_data = request.json
        query= "UPDATE app_discord SET nombre_sala = %s WHERE salas.id_salas = %s;"
        params = request.args.get('usuario'), id_salas
        
        return {"msg": "Datos del nombre de sala actualizados con éxito"}, 200
    @classmethod
    def delete_sala(id_salas):
        query= "DELETE FROM app_discord WHERE salas.id_salas = %s;"
        params = id_salas,
 
        return {"msg": "Sala eliminado con éxito"}, 204