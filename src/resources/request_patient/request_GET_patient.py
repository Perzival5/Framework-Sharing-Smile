
id_invalid = [
    {"input":"purasletras", "item": "prof_id"},
]

id_not_exist = [
    {"input":2654555613, "title": "que no existente"},
]

token = [
    {"id": "DR-TC230", "header":"header_login", "title":"sin autenticación", "message":"Not authenticated", "status":401},
    {"id": "DR-TC231", "header":"header_token_invalid", "title":"con token invalido", "message":"Invalid token", "status":401},
]

http_methods_invalid = [
    {"id": "DR-TC232", "item": "PATCH"},
    {"id": "DR-TC233", "item": "DELETE"},
]
