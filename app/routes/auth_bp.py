from flask import Blueprint

from ..controllers.auth_controller import UserController

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(UserController.login)
#auth_bp.route('/logren', methods=['GET'])(UserController.logren)
auth_bp.route('/')(UserController.inicio)
auth_bp.route('/formulario', methods=['POST', 'GET'])(UserController.formulario)
auth_bp.route('/perfil/<cookie>', methods=['POST', 'GET'])(UserController.leerusuario)
auth_bp.route('/mainserver', methods=['GET','POST'])(UserController.mainserver)



auth_bp.route('/logout', methods=['GET'])(UserController.logout)
auth_bp.route('/profile', methods=['GET'])(UserController.show_profile)