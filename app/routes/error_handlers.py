from flask import Blueprint
from ..models.exceptions import UserNotFound, InvalidDataError

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(UserNotFound)
def handle_film_not_found(error):
    return error.get_response()

@errors.app_errorhandler(InvalidDataError)
def handle_invalid_data_error(error):
    return error.get_response()