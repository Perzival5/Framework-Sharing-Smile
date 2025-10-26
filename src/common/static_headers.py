from enum import Enum

class StaticDataHeaders(Enum):
    header_login = "header_login"
    header_void = "header_void"
    header_professional = "header_professional"
    header_delete_profesional = "header_delete_profesional"
    header_patient = "header_patient"
    header_delete_patient = "header_delete_patient"
    header_without_permits = "header_without_permits"
    header_token_invalid = "header_token_invalid"