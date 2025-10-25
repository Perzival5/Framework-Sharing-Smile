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
from src.resources.request_GET_profesional import id_invalid, id_not_exist, token, http_methods_invalid


def test_Verificar_obtencion_de_lista_de_profesionales(get_url):
    allure.dynamic.title("DR-TC72: Verificar obtención de lista de profesionales")
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value)
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_200_get.json", StaticDataModules.professionals.name)
    assert_professionals_list_format(response.json())

def test_Verificar_obtencion_de_lista_de_profesionales_id(get_url):
    allure.dynamic.title("DR-TC73: Verificar obtención de datos de un profesional por ID")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.professionals.value}{StaticInputs.id.value}",
                                header_type=StaticDataHeaders.header_professional.value)
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_professionals_list_format(response.json())

@pytest.mark.parametrize("date", id_invalid)
def test_Verificar_que_no_se_pueda_obtener_los_datos_de_un_profesional_con_ID_invalido(get_url, date):
    allure.dynamic.title("DR-TC74:  Verificar que no se pueda obtener los datos de un profesional con ID inválido")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.professionals.value}{date['input']}",
                                header_type=StaticDataHeaders.header_professional.value)
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.professionals.name)

@pytest.mark.parametrize("date", id_not_exist)
def test_Verificar_que_no_se_pueda_obtener_los_datos_de_un_profesional_con_ID_que_no_existe(get_url, date):
    allure.dynamic.title("DR-TC75:  Verificar que no se pueda obtener los datos de un profesional con ID que no existente")
    response = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.professionals.value}{date['input']}",
                                header_type=StaticDataHeaders.header_professional.value)
    assert_response_status_code(response.status_code, StaticStatus.not_found.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.professional_not_found.value)

@pytest.mark.parametrize("date", token)
def test_Verificar_que_no_se_pueda_obtener_la_lista_de_profesionales(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda obtener la lista de profesionales {date['title']}")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=date['header'])
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, date['message'])

@pytest.mark.parametrize("date", http_methods_invalid)
def test_Verificar_fallo_en_obtencion_de_lista_de_profesional_con_metodo_HTTP_incorrecto(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar fallo en obtención de lista de profesionales con método HTTP incorrecto {date['item']}")
    response = request_function(date['item'], get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value)
    assert_responde_falled_http(response, StaticDataModules.professionals.name, date['id'])