from ..database import DatabaseConnection

class Servidor:

    def __init__(self, id_servidor_u_s = None, nombre_servidor = None):
                 
        self.id_servidor_u_s = id_servidor_u_s
        self.nombre_servidor = nombre_servidor
    
    
    @classmethod
    def get_all(cls):
       
        query = """SELECT id_servidor_u_s, nombre_servidor FROM app_discord.servidor_u_s"""
        results = DatabaseConnection.fetch_all(query)

        servidor = []
        if results is not None:
            for result in results:
                servidor.append(cls(*result))
        return servidor
    
    @classmethod
    def create(cls, nombre_servidor):
        
        query = """INSERT INTO app_discord.servidor_u_s (`nombre_servidor`) VALUES (%s);"""
        params = (nombre_servidor)
        
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, nombre_servidor):
       
        query = "DELETE FROM app_discord.servidro_u_s WHERE id_servidor_u_S = %s"
        params = (nombre_servidor)
        DatabaseConnection.execute_query(query, params=params)