import pytest
import allure
from src.utils.logger import *
from src.assertions.global_assertions import *
from src.assertions.assertions_login.assertions_login import *
from src.resources.request_login.request_login import users, users_valid, http_methods_invalid
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.common.static_status import StaticStatus
from src.utils.payload_login import login_payload
from src.utils.api_calls import request_function

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize("user", users)
def test_Verificar_login_exitoso_con_credenciales_válidas(get_url, user):
    allure.dynamic.title(f"{user['id']}: Verificar login exitoso con credenciales válidas como {user['role']}")
    request=login_payload(user["username"], user["password"])
    assert_schema(request, "schema_input.json", StaticDataModules.login.name)
    assert_payload(request, user["username"], user["password"])
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.login.value,
                                header_type=StaticDataHeaders.header_login.value, payload=request)
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_200.json", StaticDataModules.login.name)
    assert_response(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("user", users_valid)
def test_Verificar_login_fallido(get_url, user):
    allure.dynamic.title(f"{user['id']}: Verificar login fallido con {user['title']}")
    request=login_payload(user["username"], user["password"])
    assert_schema(request, "schema_input.json", StaticDataModules.login.name)
    assert_payload(request, user["username"], user["password"])
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.login.value,
                                header_type=StaticDataHeaders.header_login.value, payload=request)
    assert_reponse_falled(response, StaticDataModules.login.name, user["id"])

@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.xfail(reason= "bug conocido: el mensaje del error 400 esta mal escrito")
@pytest.mark.parametrize("http", http_methods_invalid)
def test_Verificar_login_fallido_con_metodo_HTTP_incorrecto(get_url, http):
    allure.dynamic.title(f"{http['id']}: Verificar login fallido con método HTTP incorrecto {http['method']}")
    request=login_payload(http["username"], http["password"])
    assert_schema(request, "schema_input.json", StaticDataModules.login.name)
    assert_payload(request, http["username"], http["password"])
    response = request_function(http["method"], get_url, StaticDataModules.login.value,
                                header_type=StaticDataHeaders.header_login.value, payload=request)
    assert_responde_falled_http(response, StaticDataModules.login.name, http["id"])

@pytest.mark.negative
@pytest.mark.regression
def test_Verificar_login_fallido_con_payload_invalido(get_url):
    allure.dynamic.title(f"DR-TC12: Verificar login fallido con un payload invalido")
    request=login_payload(None, None)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.login.value,
                                header_type=StaticDataHeaders.header_login.value, payload=request)
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422.json", StaticDataModules.login.name)
    assert_link_error(response)
    