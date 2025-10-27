import pytest
import allure
from src.utils.logger import *
from src.assertions.global_assertions import *
from src.assertions.assertions_patient.assertions_patient import *
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.common.static_status import StaticStatus
from src.common.static_inputs import StaticInputs
from src.utils.api_calls import request_function
from src.resources.request_DELETE_patient import *

def test_Verificar_eliminación_de_paciente_existente(get_url,setup_create_patient):
    allure.dynamic.title("DR-TC313: Verificar eliminación de paciente existente")
    response = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.patients.value}{setup_create_patient["id"]}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.no_content.value)

@pytest.mark.parametrize("date", id_invalid)
def test_Verificar_eliminación_de_paciente_fallida_con_ID_invalido(get_url, date):
    allure.dynamic.title("DR-TC314: Verificar eliminación de paciente fallida con ID inválido")
    response = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.patients.value}{date['input']}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.patients.name)

@pytest.mark.parametrize("date", id_not_exist)
def test_Verificar_eliminación_de_paciente_con_ID_no_existente(get_url, date):
    allure.dynamic.title("DR-TC315: Verificar eliminación de paciente con ID no existente")
    response = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.patients.value}{date['input']}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.not_found.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.patient_not_found.value)

@pytest.mark.parametrize("date", token)
def test_Verificar_eliminación_de_paciente_fallida_con_token_invalido(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar eliminación de paciente fallida {date['title']}")
    response = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.patients.value}{StaticInputs.id.value}",
                                header_type=date['header'])
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, date['message'])