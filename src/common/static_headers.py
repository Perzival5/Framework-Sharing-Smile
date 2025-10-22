from enum import Enum

class StaticDataHeaders(Enum):
    header_login = "header_login"
    header_void = "header_void"
    header_professional = "header_professional"
    header_delete_profesional = "header_delete_profesional"
    
    no_accept_header = "no_accept_header"
    no_token_header = "no_token_header"
    invalid_token_header = "invalid_token_header"