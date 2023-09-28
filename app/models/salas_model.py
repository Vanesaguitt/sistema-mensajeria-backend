from ..database import DatabaseConnection

class Salas:

    def __init__(self, id_salas = None, nombre_sala = None, id_servidor_u_s = None, usuario_adm = None):
                 
        self.id_salas = id_salas
        self.nombre_sala = nombre_sala
        self.usuario_adm = usuario_adm
    
    @classmethod
    def get_all(cls):
       
        query = """SELECT id_salas, nombre_sala, id_servidor_u_s,
        usuario_adm FROM app_discord.salas"""
        results = DatabaseConnection.fetch_all(query)

        salas = []
        if results is not None:
            for result in results:
                salas.append(cls(*result))
        return salas
    
    @classmethod
    def create(cls, salas, nombre_sala, usuario_adm):
        
        query = """INSERT INTO `app_discord`.`salas` (`nombre_sala`, `usuario_adm`) VALUES (%s, %s, %s);"""
        params = (salas , nombre_sala, usuario_adm)
        
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, salas, nombre_sala, usuario_adm):
       
        query = "DELETE FROM app_discord.salas WHERE id_salas = %s"
        params = (salas , nombre_sala, usuario_adm)
        DatabaseConnection.execute_query(query, params=params)