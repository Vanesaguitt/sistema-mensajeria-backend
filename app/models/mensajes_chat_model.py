from ..database import DatabaseConnection

class Mensaje:

    def __init__(self, id_mensajes_chat = None, mensaje = None, usuario = None, id_salas = None):
                 
        self.id_mensajes_chat = id_mensajes_chat
        self.mensaje = mensaje
        self.usuario = usuario
        self.id_salas = id_salas
    
    @classmethod
    def get_all(cls):
       
        query = """SELECT id_mensajes_chat, mensaje, usuario,
        id_salas FROM app_discord.mensajes_chat"""
        results = DatabaseConnection.fetch_all(query)

        mensajes_chat = []
        if results is not None:
            for result in results:
                mensajes_chat.append(cls(*result))
        return mensajes_chat
    
    @classmethod
    def create(cls, mensajes_chat, usuario, id_salas):
        
        query = """INSERT INTO app_discord.mensajes_chat (`mensaje`, `usuario`, `id_salas`)
        VALUES (%s, %s, %s);"""
        params = (mensajes_chat, usuario, id_salas)
        
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, mensajes_chat, usuario, id_salas):
       
        query = "DELETE FROM app_discord.mensajes_chat WHERE id_mensajes_chat = %s"
        params = (mensajes_chat, usuario, id_salas)
        
        DatabaseConnection.execute_query(query, params=params)
        