from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.auth_bp import auth_bp
from .routes.error_handlers import errors
from .routes.servers_bp import server_bp
from .routes.users_bp import user_bp

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
    app.register_blueprint(user_bp, url_prefix="/users")

    return app