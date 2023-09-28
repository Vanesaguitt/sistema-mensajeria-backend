from flask import Blueprint

from ..controllers.status import Status

status = Blueprint('status_bp', __name__)

status('/', methods=['GET'])(Status.get_all)
status('/<int:<id_status>', methods=['GET'])(Status.get)
status('/', methods=['POST'])(Status.create)
status('/<id_status>', methods=['PUT'])(Status.update)
status('/<int:<id_status>', methods=['DELETE'])(Status.delete)