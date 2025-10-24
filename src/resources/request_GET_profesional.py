import config

id_invalid = [
    {"input":"letras", "item": "prof_id"},
]

id_not_exist = [
    {"input":1654555612, "title": "que no existente"},
]

token = [
    {"id": "DR-TC76", "header":"header_login", "title":"sin autenticación", "message":"Not authenticated", "status":401},
    {"id": "DR-TC77", "header":"header_token_invalid", "title":"con token invalido", "message":"Invalid token", "status":401},
    {"id": "DR-TC78", "header":"header_without_permits", "title":"con token sin permisos", "message":"Not enough permissions", "status":403},
]

http_methods_invalid = [
    {"id": "DR-TC79", "item": "PATCH"},
    {"id": "DR-TC80", "item": "DELETE"},
]
