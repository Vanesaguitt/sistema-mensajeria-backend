from ..models.auth.user_model import User
from ..models.exceptions import UserNotFound, InvalidDataError
from flask import request, session, render_template

class UserController:

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            username = data.get('username'),
            password = data.get('password')
        )
        
        if User.is_registered(user):
            session['username'] = data.get('username')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401

            
    @classmethod
    def show_profile(cls):
        username = session.get2('username')
        user = User.get2(User(username = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200


    
    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200
    

    
    
    @classmethod
    def logren(cls):
        return render_template('/login.html')
    
    @classmethod
    def inicio(cls):
        return render_template('/index.html')
    
    
    @classmethod
    def formulario(cls):
        if request.method == 'POST':
            
            usuario = request.form['usuario']
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            email = request.form['email']
            contrasena = request.form['contrasena']
            User.regist(usuario,contrasena,email,nombre,apellido)
            
            return render_template('/login.html'), 200
        else:
            return render_template('/registro.html')
    
    
    @classmethod
    def get(cls, usuario):
        """Get a film by id"""
        user = User(usuario=usuario)
        result = User.get(user)

        if result is None:
            raise UserNotFound(usuario)

        return result.serialize(), 200