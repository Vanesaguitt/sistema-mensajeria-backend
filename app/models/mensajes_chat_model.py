<<<<<<< Updated upstream
from ..database import DatabaseConnection
=======
from database import DatabaseConnection
>>>>>>> Stashed changes

class Mensajes:
    """Film model class"""

<<<<<<< Updated upstream
    def __init__(self, mensaje = None, usuario = None, id_salas = None, id_mensaje_chat = None):
=======
    def __init__(self, id_mensaje_chat = None, mensaje = None, usuario = None, id_salas = None):
>>>>>>> Stashed changes
        """Constructor method"""
        self.id_mensaje_chat = id_mensaje_chat
        self.mensaje = mensaje
        self.usuario = usuario
<<<<<<< Updated upstream
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

=======
        self.id_salas = id_salas
>>>>>>> Stashed changes
        
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
<<<<<<< Updated upstream
                id_salas = result[3]
=======
                ld_salas = result[3]
>>>>>>> Stashed changes
        )
        else:
            return None
    
    @classmethod
<<<<<<< Updated upstream
    def get_by_sala(cls, sala):
       
        query = """SELECT mensaje, usuario, id_salas FROM app_discord.mensajes_chat WHERE id_salas = (SELECT id_salas FROM app_discord.salas WHERE nombre_sala = %s)"""
        params = (sala,)

        results = DatabaseConnection.fetch_all(query=query, params=params)
=======
    def get_mensajes(cls):
       
        query = """SELECT id_mensaje_chat, mensaje, usuario, id_salas FROM app_discord.mensajes_chat"""
        results = DatabaseConnection.fetch_all(query)
>>>>>>> Stashed changes

        mensajes = []
        if results is not None:
            for result in results:
                mensajes.append(cls(*result))
<<<<<<< Updated upstream

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

=======
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
    
>>>>>>> Stashed changes
    @classmethod
    def delete_mensaje(cls, mensaje):
        query = "DELETE FROM app_discord.mensajes_chat WHERE id_mensajes_chat = %s"
        DatabaseConnection.execute_query(query, mensaje)
