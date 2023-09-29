from ..database import DatabaseConnection

class Mensajes:
    """Film model class"""

    def __init__(self, mensaje = None, usuario = None, id_salas = None, id_mensaje_chat = None):
        """Constructor method"""
        self.id_mensaje_chat = id_mensaje_chat
        self.mensaje = mensaje
        self.usuario = usuario
        if type(id_salas) is str:
            print("___________________________________________________")
            print("ENTRE AL IF")
            self.id_salas = self.get_sala_id(id_salas)
        else:
            self.id_salas = id_salas


    def get_sala_id(self, sala):

        query = "SELECT id_salas FROM app_discord.salas WHERE nombre_sala = %s"
        params = (sala,)
        result = DatabaseConnection.fetch_one(query=query, params=params)
        
        return result[0]

        
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
                id_salas = result[3]
        )
        else:
            return None
    
    @classmethod
    def get_by_sala(cls, sala):
       
        query = """SELECT mensaje, usuario, id_salas FROM app_discord.mensajes_chat WHERE id_salas = (SELECT id_salas FROM app_discord.salas WHERE nombre_sala = %s)"""
        params = (sala,)

        results = DatabaseConnection.fetch_all(query=query, params=params)

        mensajes = []
        if results is not None:
            for result in results:
                mensajes.append(cls(*result))

        return mensajes
    
    def serialize(self):
        return {
            "id_channel": self.id_salas,
            "message": self.mensaje,
            "user": self.usuario
        }
        


    @classmethod
    def create(cls, mensaje):
        
        query = """INSERT INTO app_discord.mensajes_chat (mensaje, usuario, id_salas) VALUES (%s, %s, %s)"""
        params = (mensaje.mensaje, mensaje.usuario, mensaje.id_salas)
        DatabaseConnection.execute_query(query=query, params=params)

    @classmethod
    def delete_mensaje(cls, mensaje):
        query = "DELETE FROM app_discord.mensajes_chat WHERE id_mensajes_chat = %s"
        DatabaseConnection.execute_query(query, mensaje)
