import pytest
import allure
from src.utils.logger import *
from src.assertions.global_assertions import *
from src.assertions.assertions_professional.assertions_professional import *
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.common.static_status import StaticStatus
from src.utils.payload_builders_professionals import build_user_payload
from src.utils.api_calls import request_function
from src.resources.files import *

def test_Verificar_registro_de_profesional_con_todos_los_campos_válidos(get_url,teardown_professional):
    allure.dynamic.title(f"DR-TC13: Verificar registro de profesional con todos los campos válidos")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_response_profesional(response.json(),request)
    teardown_professional(response.json()["id"])
