from ..database import DatabaseConnection

class Salas:

    def __init__(self, nombre_sala = None, id_servidor_u_s = None, usuario_adm = None):
                 
        self.nombre_sala = nombre_sala
        self.id_servidor_u_s = id_servidor_u_s
        self.usuario_adm = usuario_adm
    
    @classmethod
    def get_by_server(cls, server_name):
       
        query = """SELECT nombre_sala, FROM app_discord.salas WHERE id_servidor_u_s = (SELECT id_servidor_u_s FROM app_discord.servidor_u_s WHERE nombre_servidor = %s)"""
        params = (server_name,)
        results = DatabaseConnection.fetch_all(query=query, params=params)

        salas = []
        if results is not None:
            for result in results:
                salas.append(cls(*result))
        return salas