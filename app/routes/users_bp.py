from flask import Blueprint

from ..controllers.usuarios import UsuariosController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/<string:user_name>', methods=['GET'])(UsuariosController.get_usuario)