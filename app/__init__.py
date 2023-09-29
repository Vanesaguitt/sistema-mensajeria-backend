from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.mensajes_chat_bp import mensajes_chat_bp
from .routes.salas_bp import salas_bp
from .routes.servidor_u_s_bp import servidor_u_s_bp


from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(mensajes_chat_bp, url_prefix = '/mensajes_chat')
    app.register_blueprint(salas_bp, url_prefix = '/salas')
    app.register_blueprint(servidor_u_s_bp, url_prefix = '/servidores')
    
    

    return app