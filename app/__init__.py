from flask import Flask
from config import Config

from .routes.servers_bp import server_bp

from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(server_bp, url_prefix = "/servers")

    return app