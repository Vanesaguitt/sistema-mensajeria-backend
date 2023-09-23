from ..models.mensajes_chat_model import Mensajes
from database import DatabaseConnection
from flask import request

class MensajesController:
    @classmethod
    def create_mensaje_chat(cls):
        mensaje_data = request.json
        mensaje = Mensajes(
            id_mensajes_chat = mensaje_data.get('id_mensajes_chat'),
            mensaje = mensaje_data.get('mensaje'),
            usuario = mensaje_data.get('usuario'),
            id_salas = mensaje_data.get('id_salas')
        )
        
        Mensajes.create(mensaje)
        return {'message': 'Mensaje creado con exito'}, 200
    
    @classmethod
    def get_mensaje_chat(cls, id_mensajes_chat):
        mensaje = mensaje(id_mensajes_chat=id_mensajes_chat)
        result = mensaje.get(mensaje)
        if result is not None:
            return result.serialize(), 20
        
    @classmethod
    def get_mensajes_chats(cls):
        mensaje_objects = mensaje.get_all()
        mensajes = []
        for mensaje in mensaje_objects:
            mensajes.append(mensaje.serialize())
        return mensajes, 200
    
    @classmethod
    def update_mensaje_chat(cls, id_mensajes_chat):
        mensaje_data = request.json
        query= "UPDATE app_discord SET mensaje = %s WHERE mensajes_chat.id_mensajes_chat = %s;"
        params = request.args.get('mensaje'), id_mensajes_chat
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Datos del mensaje ha actualizados con éxito"}, 200
    @classmethod
    def delete_mensaje_chat(id_mensajes_chat):
        query= "DELETE FROM app_discord WHERE mensajes_chat.id_mensajes_chat = %s;"
        params = id_mensajes_chat,
        DatabaseConnection.execute_query(query, params)
 
        return {"msg": "El mensaje ha sido eliminado con éxito"}, 204

    

        