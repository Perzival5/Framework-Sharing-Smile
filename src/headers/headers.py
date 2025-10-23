import config

def generate_headers(header_type):
    match header_type:
        case "header_login":
            return get_header_login()
        case "header_void":
            return get_header_void()
        case "header_professional":
            return header_professional()
        case "header_delete_profesional":
            return header_professional()
        case "header_without_permits":
            return header_without_permits()
        case "header_token_invalid":
            return header_token_invalid()
       

def get_header_login():
    headers = {
        "accept": "application/json"
    }
    return headers

def get_header_void():
    headers = {}
    return headers

def header_professional():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {config.ADMIN_TOKEN}"
    }
    return headers

def header_delete_profesional():
    headers = {
        "Authorization": f"Bearer {config.ADMIN_TOKEN}"
    }
    return headers

def header_without_permits():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {config.PRO_TOKEN}"
    }
    return headers

def header_token_invalid():
    headers = {
        "Authorization": "Bearer dasvasbrbebwebwbweb"
    }
    return headers

def header_patient():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {config.PRO_TOKEN}"
    }
    return headers

def header_delete_patient():
    headers = {
        "Authorization": f"Bearer {config.PRO_TOKEN}"
    }
    return headers