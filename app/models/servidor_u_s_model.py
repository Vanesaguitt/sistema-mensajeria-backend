from ..database import DatabaseConnection

class Servidor:

    def __init__(self, name: str):
        self.name = name


    @classmethod
    def get_all(self, server_name: str):
        
        query = "SELECT 'salas'.'nombre_sala' FROM salas WHERE id_servidor_u_s = (SELECT nombre_servidor FROM servidor_u_s WHERE id_servidor_u_s = %s)"
        params = (server_name,)
        results = DatabaseConnection.fetch_all(query=query, params=params)
        return 