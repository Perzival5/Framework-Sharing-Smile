from enum import Enum

class StaticStatus(Enum):
    ok = 200
    bad_request = 400
    unauthorized = 401
    methodNotAllowed = 405
    not_found = 404
    unprocessable_entity = 422
    internal_server_error = 500
    