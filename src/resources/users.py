import config

users = [
    {"id": "DR-TC01", "role": "admin", "username": config.ADMIN_USER, "password": config.ADMIN_PASS},
    {"id": "DR-TC02", "role": "professional", "username": config.PRO_USER, "password": config.PRO_PASS},
]

users_valid = [
    {"id": "DR-TC03", "title": "usuario inválido", "username": "noregistrado@hotmail.com", "password": config.ADMIN_PASS},
    {"id": "DR-TC04", "title": "contraseña inválida", "username":  config.ADMIN_USER, "password": "error"},
    {"id": "DR-TC05", "title": "usuario y contraseña vacíos", "username": "", "password": ""},
    {"id": "DR-TC06", "title": "usuario vacío y contraseña válida", "username": "", "password": config.PRO_PASS},
    {"id": "DR-TC07", "title": "usuario válido y contraseña vacía", "username": config.PRO_USER, "password": ""},
    {"id": "DR-TC08", "title": "credenciales que exceden longitud máxima", "username": "x" * 100, "password": config.ADMIN_PASS},
]

http_methods_invalid = [
    {"id": "DR-TC09", "method": "GET", "username": config.ADMIN_USER, "password": config.ADMIN_PASS},
    {"id": "DR-TC10", "method": "PUT", "username": config.ADMIN_USER, "password": config.ADMIN_PASS},
    {"id": "DR-TC11", "method": "DELETE", "username": config.ADMIN_USER, "password": config.ADMIN_PASS},
]

