from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.auth_bp import auth_bp
from .routes.error_handlers import errors
<<<<<<< Updated upstream
from .routes.mensajes_chat_bp import mensajes_chat_bp
from .routes.servers_bp import server_bp

=======
from .routes.servers_bp import server_bp
>>>>>>> Stashed changes
from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(errors)
    app.register_blueprint(auth_bp, url_prefix = '/')
    app.register_blueprint(server_bp, url_prefix = "/servers")
<<<<<<< Updated upstream
    app.register_blueprint(mensajes_chat_bp, url_prefix="/channels")
=======
  
>>>>>>> Stashed changes

    return app