import pytest
import allure
from src.utils.logger import *
from src.assertions.global_assertions import *
from src.assertions.assertions_professional.assertions_professional import *
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.common.static_status import StaticStatus
from src.common.static_inputs import StaticInputs
from src.utils.api_calls import request_function
from src.resources.request_professional.request_DELETE_professional import id_invalid, id_not_exist, token

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_Verificar_eliminación_de_profesional_existente(get_url,setup_create_professional):
    allure.dynamic.title("DR-TC158: Verificar eliminación de profesional existente")
    response = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.professionals.value}{setup_create_professional['id']}",
                                header_type=StaticDataHeaders.header_professional.value)
    assert_response_status_code(response.status_code, StaticStatus.no_content.value)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", id_invalid)
def test_Verificar_eliminación_de_profesional_fallida_con_ID_invalido(get_url, date):
    allure.dynamic.title("DR-TC159: Verificar eliminación de profesional fallida con ID inválido")
    response = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.professionals.value}{date['input']}",
                                header_type=StaticDataHeaders.header_professional.value)
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.professionals.name)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", id_not_exist)
def test_Verificar_eliminación_de_profesional_con_ID_no_existente(get_url, date):
    allure.dynamic.title("DR-TC160: Verificar eliminación de profesional con ID no existente")
    response = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.professionals.value}{date['input']}",
                                header_type=StaticDataHeaders.header_professional.value)
    assert_response_status_code(response.status_code, StaticStatus.not_found.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.professional_not_found.value)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", token)
def test_Verificar_eliminación_de_profesional_fallida_con_token_invalido(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar eliminación de profesional fallida {date['title']}")
    response = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.professionals.value}{StaticInputs.id.value}",
                                header_type=date['header'])
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, date['message'])