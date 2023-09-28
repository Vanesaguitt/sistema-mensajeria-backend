from flask import Blueprint

from ..controllers.usuarios import Usuarios

usuarios = Blueprint('usuarios_bp', __name__)

usuarios('/', methods=['GET'])(Usuarios.get_all)
usuarios('/<int:<id_status>', methods=['GET'])(Usuarios.get)
usuarios('/', methods=['POST'])(Usuarios.create)
usuarios('/<id_status>', methods=['PUT'])(Usuarios.update)
usuarios('/<int:<id_status>', methods=['DELETE'])(Usuarios.delete)