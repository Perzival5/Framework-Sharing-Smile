from src.common.static_status import StaticStatus
from src.assertions.global_assertions import *

def assert_payload(request, user, password):
    assert request["username"] == user
    assert request["password"] == password

def assert_response(response):
    assert "eyJhbGciOiJIUzI1NiIsInR" in response.json()["access_token"]
    assert response.json()["token_type"] == "Bearer"

def assert_reponse_falled(response, file, type):

    if type == "DR-TC03" or type == "DR-TC04" or type == "DR-TC08":
        assert_response_status_code(response.status_code, StaticStatus.unauthorized.value)
        assert_schema(response.json(), "schema_401.json", file)
        assert response.json()["detail"] == "Incorrect username or password"

    elif type == "DR-TC05":
        assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
        assert_schema(response.json(), "schema_422.json", file)
        assert_link_error(response)

    elif type == "DR-TC06" or type == "DR-TC07":
        assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
        assert_schema(response.json(), "schema_422_username_or_password_void.json", file)
        assert_link_error(response)

    else:
        raise ValueError(f"Tipo de caso no soportado: {type}")

def assert_link_error(response):
    assert response.json()["detail"][0]["url"] == "https://errors.pydantic.dev/2.8/v/missing"

def assert_responde_falled_http(response, file, type):
    if type == "DR-TC09":
        assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
        assert "<title>Error 400 (Bad Request)!!!</title>" in response.text

    elif type == "DR-TC10" or type == "DR-TC11":
        assert_response_status_code(response.status_code, StaticStatus.method_not_allowed.value)
        assert_schema(response.json(), "schema_405.json", file)
        assert response.json()["detail"] == "Method Not Allowed"

    else:
        raise ValueError(f"Tipo de caso no soportado: {type}")