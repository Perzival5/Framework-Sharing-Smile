
def generate_headers(header_type):
    match header_type:
        case "header_login":
            return get_header_login()
        case "header_void":
            return get_header_void()

def get_header_login():
    headers = {
        "accept": "application/json"
    }
    return headers

def get_header_void():
    headers = {}
    return headers
