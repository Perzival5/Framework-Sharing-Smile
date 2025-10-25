from enum import Enum

class StaticStatus(Enum):
    ok = 200
    created = 201
    no_content = 204
    bad_request = 400
    unauthorized = 401
    method_not_allowed = 405
    not_found = 404
    unprocessable_entity = 422
    internal_server_error = 500
    