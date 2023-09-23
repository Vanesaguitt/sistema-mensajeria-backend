from ..models.usuarios_model import Usuarios
from database import DatabaseConnection
from flask import request

class UsuariosController:
    @classmethod
    def create_usuarios(cls):
        usuario_data = request.json
        usuario = Usuarios(
            usuario = usuario_data.get('usuari'),
            nombre_apellido = usuario_data.get('nombre_apellido'),
            email = usuario_data.get('email'),
            fecha_nacimiento= usuario_data.get('fecha_nacimiento'),
            contraseña = usuario_data.get('contraseña'),
            id_status = usuario_data.get('id_status')
        )
        
        Usuarios.create(usuario)
        return {'message': 'Usuario creado con exito'}, 200
    
    @classmethod
    def get_usuario(cls, id_satus):
        usuario = Usuarios(id_satus=id_satus)
        result = Usuarios.get(usuario)
        if result is not None:
            return result.serialize(), 20
        
    @classmethod
    def get_usuarios(cls):
        usuario_objects = Usuarios.get_all()
        usuarios = []
        for usuario in usuario_objects:
            usuarios.append(usuario.serialize())
        return usuarios, 200
    
    @classmethod
    def update_usuario(cls, id_status):
        usuario_data = request.json
        query= "UPDATE app_discord SET usuario = %s WHERE usuarios.id_status = %s;"
        params = request.args.get('usuario'), id_status
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Datos del usuario actualizados con éxito"}, 200
    @classmethod
    def delete_usuario(id_stauts):
        query= "DELETE FROM app_discord WHERE usuarios.id_status = %s;"
        params = id_stauts,
        DatabaseConnection.execute_query(query, params)
 
        return {"msg": "Usuario eliminado con éxito"}, 204

    