
def login_payload(username: str | None = None, password: str | None = None) -> dict:
    payload = {}

    if username is not None: payload["username"] = username
    if password is not None: payload["password"] = password
    
    return payload
