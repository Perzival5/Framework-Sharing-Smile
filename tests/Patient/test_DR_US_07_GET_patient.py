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
from src.resources.request_GET_patient import *

def test_Verificar_obtencion_de_lista_de_pacientes(get_url):
    allure.dynamic.title("DR-TC226: Verificar obtención de lista de pacientes")
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_200_get.json", StaticDataModules.patients.name)
    assert_patients_list_format(response.json())

def test_Verificar_obtencion_de_lista_de_pacientes_id(get_url):
    allure.dynamic.title("DR-TC227: Verificar obtención de datos de un paciente por ID")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.patients.value}{StaticInputs.id.value}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_patients_list_format(response.json())

@pytest.mark.parametrize("date", id_invalid)
def test_Verificar_que_no_se_pueda_obtener_los_datos_de_un_paciente_con_ID_invalido(get_url, date):
    allure.dynamic.title("DR-TC228: Verificar que no se pueda obtener los datos de un paciente con ID inválido")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.patients.value}{date['input']}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.patients.name)

@pytest.mark.parametrize("date", id_not_exist)
def test_Verificar_que_no_se_pueda_obtener_los_datos_de_un_paciente_con_ID_que_no_existe(get_url, date):
    allure.dynamic.title("DR-TC229: Verificar que no se pueda obtener los datos de un paciente con ID que no existente")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.patients.value}{date['input']}",
                                header_type=StaticDataHeaders.header_patient.value)
    assert_response_status_code(response.status_code, StaticStatus.not_found.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.patient_not_found.value)

@pytest.mark.parametrize("date", token)
def test_Verificar_que_no_se_pueda_obtener_la_lista_de_pacientes(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda obtener la lista de pacientes {date['title']}")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=date['header'])
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, date['message'])

@pytest.mark.parametrize("date", http_methods_invalid)
def test_Verificar_fallo_en_obtencion_de_lista_de_paciente_con_metodo_HTTP_incorrecto(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar fallo en obtención de lista de pacientes con método HTTP incorrecto {date['item']}")
    response = request_function(date['item'], get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value)
    assert_responde_falled_http(response, StaticDataModules.patients.name, date['id'])