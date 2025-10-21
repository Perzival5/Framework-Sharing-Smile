import pytest
import allure
from src.utils.logger import *
from src.assertions.global_assertions import *
from src.assertions.assertions_login.assertons_login import *
from src.resources.users import users
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.common.static_status import StaticStatus
from src.common.payloads.payload_login import login_payload
from src.utils.api_calls import request_function

@pytest.mark.parametrize("user", users)
def test_Verificar_login_exitoso_con_credenciales_válidas(get_url, user):
    allure.dynamic.title(f"{user['id']}: Verificar login exitoso con credenciales válidas como {user['role']}")
    request=login_payload(user["username"], user["password"])
    assert_schema(request, "schema_input.json", StaticDataModules.login.name)
    assert_payload(request, user["username"], user["password"])
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.login.value,
                                header_type=StaticDataHeaders.header_login.value, payload=request)
    log_response(response)
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_200.json", StaticDataModules.login.name)
    assert_response(response)
    