
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
from src.resources.request_patien_photo import *
from src.resources.files import *

def test_Verificar_obtencion_de_registro_fotografico_de_un_paciente(get_url):
    allure.dynamic.title("DR-TC325: Verificar obtención de registro fotográfico de un paciente")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.patients.value}{StaticInputs.id.value}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_200_get_photo.json", StaticDataModules.patients.name)
    assert_response_photo_id(response)

@pytest.mark.parametrize("date", id_invalid)
def test_Verificar_que_no_se_pueda_obtener_el_registro_fotografico_fallido_de_un_paciente_con_ID_invalido(get_url, date):
    allure.dynamic.title("DR-TC326: Verificar que no se pueda obtener el registro fotográfico de un paciente con ID inválido")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.patients.value}{date['input']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.patients.name)

@pytest.mark.parametrize("date", id_not_exist)
def test_Verificar_que_no_se_pueda_obtener_el_registro_fotografico_de_un_paciente_con_ID_que_no_existe(get_url, date):
    allure.dynamic.title("DR-TC327: Verificar que no se pueda obtener el registro fotográfico de un paciente con ID que no existente")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.patients.value}{date['input']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.not_found.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.patient_not_found.value)

@pytest.mark.parametrize("date", token_delete)
def test_Verificar_que_no_se_pueda_obtener_el_registro_fotografico_de_pacientes(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda obtener el registro fotográfico de paciente{date['title']}")
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.patients.value,
                                header_type=date['header'])
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, date['message'])