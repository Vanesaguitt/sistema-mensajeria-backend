from database import DatabaseConnection

class Mensajes:
    """Film model class"""

    def __init__(self, id_mensaje_chat = None, mensaje = None, usuario = None, id_salas = None):
        """Constructor method"""
        self.id_mensaje_chat = id_mensaje_chat
        self.mensaje = mensaje
        self.usuario = usuario
        self.id_salas = id_salas
        
    @classmethod
    def get_mensaje(cls, mensaje):

        query = """SELECT id_mensaje_chat, mensaje, usuario, id_salas FROM app_discord.mensajes_chat WHERE id_mensaje_chat = %s"""
        params = mensaje.id_mensaje_chat,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return Mensajes(
                id_mensaje_chat = mensaje.id_mensaje_chat,
                mensaje = result[1],
                usuario = result[2],
                ld_salas = result[3]
        )
        else:
            return None
    
    @classmethod
    def get_mensajes(cls):
       
        query = """SELECT id_mensaje_chat, mensaje, usuario, id_salas FROM app_discord.mensajes_chat"""
        results = DatabaseConnection.fetch_all(query)

        mensajes = []
        if results is not None:
            for result in results:
                mensajes.append(cls(*result))
        return mensajes
    
    @classmethod
    def create_mensaje(cls, mensaje):
        
        query = """INSERT INTO app_discord.mensajes_chat (mensaje, usuario) VALUES (%s, %s)"""
        params = (mensaje.mensaje, mensaje.usuario)
        DatabaseConnection.execute_query(query, params)
        
    @classmethod
    def update_mensaje(cls, mensaje):
        query = "UPDATE app_discord.mensajes_chat SET mensaje = %s WHERE mensae.id_mensajes_chat = %s;"      
        DatabaseConnection.execute_query(query, mensaje)
    
    @classmethod
    def delete_mensaje(cls, mensaje):
        query = "DELETE FROM app_discord.mensajes_chat WHERE id_mensajes_chat = %s"
        DatabaseConnection.execute_query(query, mensaje)
