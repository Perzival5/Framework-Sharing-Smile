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
