from flask import Blueprint

from ..controllers.servidor_u_s import ServidorController

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/<int:server_id>/channels', methods=['GET'])(ServidorController.get_salas)
#server_bp.route('/', methods=['GET'])(ServidorController.get)
#server_bp.route('/<int:server_id>', methods=['GET'])(ServidorController.get)