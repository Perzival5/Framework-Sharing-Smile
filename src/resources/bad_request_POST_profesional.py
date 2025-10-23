import config

register = [
    {"id": "DR-TC15", "item": "first_name"},
    {"id": "DR-TC16", "item": "last_name"},
    {"id": "DR-TC17", "item": "date_of_birth"},
    {"id": "DR-TC18", "item": "sex"},
    {"id": "DR-TC19", "item": "country"},
    {"id": "DR-TC20", "item": "dni"},
    {"id": "DR-TC21", "item": "personal_email"},
    {"id": "DR-TC22", "item": "phone"},
    {"id": "DR-TC23", "item": "profession"},
    {"id": "DR-TC24", "item": "specialty"},
]

special = [
    {"id": "DR-TC26", "item": "first_name", "input": "!!!!!!"},
    {"id": "DR-TC27", "item": "last_name", "input": "@@@@@@"},
    {"id": "DR-TC56", "item": "date_of_birth", "input": "######"},
    {"id": "DR-TC57", "item": "sex", "input": "$$$$$$"},
    {"id": "DR-TC58", "item": "country", "input": "%"},
    {"id": "DR-TC59", "item": "dni", "input": "^^^^^^^^"},
    {"id": "DR-TC60", "item": "personal_email", "input": "&&&&&&&"},
]

date_birth = [
    {"id": "DR-TC28", "title": "mm/dd/aaaa", "item": "date_of_birth", "input": "07/28/1999"},
    {"id": "DR-TC29", "title": "aaaa/dd/mm", "item": "date_of_birth", "input": "1997/15/12"},
]

input_invalid = [
    {"id": "DR-TC31", "item": "sex", "input": "sin genero"},
    {"id": "DR-TC32", "item": "country", "input": "japon"},
    {"id": "DR-TC33", "item": "personal_email", "input": "esto no es un correo"},
    {"id": "DR-TC34", "item": "phone", "input": "letras"},
]

http_methods_invalid = [
    {"id": "DR-TC09", "method": "GET", "username": config.ADMIN_USER, "password": config.ADMIN_PASS},
    {"id": "DR-TC10", "method": "PUT", "username": config.ADMIN_USER, "password": config.ADMIN_PASS},
    {"id": "DR-TC11", "method": "DELETE", "username": config.ADMIN_USER, "password": config.ADMIN_PASS},
]