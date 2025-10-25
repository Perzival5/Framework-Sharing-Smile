
id_invalid = [
    {"input":"letras", "item": "prof_id"},
]

id_not_exist = [
    {"input":1654555612, "title": "que no existente"},
]

token = [
    {"id": "DR-TC161", "header":"header_login", "title":"sin autenticación", "message":"Not authenticated", "status":401},
    {"id": "DR-TC162", "header":"header_token_invalid", "title":"con token invalido", "message":"Invalid token", "status":401},
    {"id": "DR-TC163", "header":"header_without_permits", "title":"con token sin permisos", "message":"Not enough permissions", "status":403},
]