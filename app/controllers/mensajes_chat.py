from ..models.mensajes_chat_model import Mensajes
from ..database import DatabaseConnection
from flask import request, session

class MensajesController:
    @classmethod
    def create_mensaje_chat(cls):
        mensaje_data = request.json

        mensaje = Mensajes(
            mensaje = mensaje_data.get('message'),
            usuario = session['username'],
            id_salas = mensaje_data.get('nombre_sala')
        )

        Mensajes.create(mensaje)
        return {'message': 'Mensaje creado con exito'}, 200
    
    @classmethod
    def get_mensaje_chat(cls, id_mensajes_chat):
        mensaje = Mensajes(id_mensajes_chat=id_mensajes_chat)
        result = mensaje.get(mensaje)
        if result is not None:
            return result.serialize(), 20
        
    @classmethod
    def get_mensajes_by_sala(cls, sala):
        mensaje_objects = Mensajes.get_by_sala(sala)
        mensajes = []
        for mensaje in mensaje_objects:
            mensajes.append(mensaje.serialize())
            
        return mensajes, 200
    
    @classmethod
    def delete_mensaje_chat(id_mensajes_chat):
        query= "DELETE FROM app_discord WHERE mensajes_chat.id_mensajes_chat = %s;"
        params = id_mensajes_chat,
        DatabaseConnection.execute_query(query, params)
 
        return {"msg": "El mensaje ha sido eliminado con éxito"}, 204

    

        