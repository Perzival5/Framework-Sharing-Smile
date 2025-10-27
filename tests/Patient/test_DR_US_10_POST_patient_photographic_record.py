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

def test_Verificar_registro_fotografico_de_un_paciente(get_url, setup_patient):
    allure.dynamic.title("DR-TC318: Verificar el registro fotográfico de un paciente")
    response = request_function(StaticDataVerbs.post.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value, payload={}, files=get_file_patient_photo())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post_photo.json", StaticDataModules.patients.name)
    assert_response_photo(response,setup_patient['id'])

def test_Verificar_registro_fotografico_fallido_sin_photo_path(get_url, setup_patient):
    allure.dynamic.title("DR-TC319: Verificar registro fotográfico fallido sin photo_path")
    response = request_function(StaticDataVerbs.post.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value, payload={})
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.patients.name)
    assert_reponse_item(response, "file")

def test_Verificar_registro_fotografico_fallido_formato_invalido_photo_path(get_url, setup_patient):
    allure.dynamic.title("DR-TC320: Verificar registro fotográfico fallido con formato invalido en photo_path")
    response = request_function(StaticDataVerbs.post.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value, payload={},files= get_file_txt_photo())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.photo.value)

@pytest.mark.parametrize("date", id_invalid)
def test_Verificar_registro_fotografico_fallido_de_un_paciente_con_ID_invalido(get_url, date):
    allure.dynamic.title("DR-TC321: Verificar registro fotográfico fallido de un paciente con ID inválido")
    response = request_function(StaticDataVerbs.post.value, get_url, f"{StaticDataModules.patients.value}{date['input']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value, payload={},files= get_file_patient_photo())
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.patients.name)

@pytest.mark.parametrize("date", id_not_exist)
def test_Verificar_registro_fotografico_fallido_de_un_paciente_con_ID_que_no_existe(get_url, date):
    allure.dynamic.title("DR-TC322: Verificar registro fotográfico fallido con ID que no existe")
    response = request_function(StaticDataVerbs.post.value, get_url, f"{StaticDataModules.patients.value}{date['input']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value, payload={},files= get_file_patient_photo())
    assert_response_status_code(response.status_code, StaticStatus.not_found.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.patient_not_found.value)

@pytest.mark.parametrize("date", token)
def test_Verificar_que_no_se_pueda_obtener_la_lista_de_pacientes(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar registro fotográfico fallido de paciente {date['title']}")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=date['header'], payload={},files= get_file_patient_photo())
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, date['message'])