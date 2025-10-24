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
from src.utils.payload_builders_professionals import *
from src.utils.api_calls import request_function
from src.resources.files import *
from src.resources.request_PATCH_profesional import input_patch, input_sex_country, input_patch_void, input_space, input_space_special, special

def test_Verificar_de_datos_de_un_profesional_con_todos_los_campos_válidos(get_url,setup_professional):
    allure.dynamic.title("DR-TC81: Verificar actualización de datos de un profesional con todos los campos válidos")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_response_profesional(response.json(),request)

@pytest.mark.parametrize("input", input_patch)
def test_Verificar_actualización_exitosa_de_un_profesional_modificando_solo_un_campo(get_url,setup_professional,input):
    allure.dynamic.title(f"{input['id']}: Verificar actualización exitosa de un profesional modificando solo el campo {input['item']}")
    random = build_random_field(input['item'])
    request=build_patch_payload(**{input['item']: random})
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, input['item'], random)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_field_value_response(response.json(), input['item'], random)

def test_Verificar_actualización_exitosa_de_un_profesional_modificando_el_campo_photo(get_url,setup_professional):
    allure.dynamic.title("DR‑TC93: Verificar actualización exitosa de un profesional modificando solo el campo photo")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_photo_response(response.json(), setup_professional["photo_path"])

@pytest.mark.parametrize("input", input_sex_country)
def test_Verificar_que_se_pueda_actualizar_un_profesional_con_datos_validos_es_sex_country(get_url,setup_professional,input):
    allure.dynamic.title(f"{input['id']}: Verificar que se pueda actualizar un profesional con {input['title']}")
    request=build_patch_payload(**{input['item']: input['input']})
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, input['item'], input['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_field_value_response(response.json(), input['item'], input['input'])

@pytest.mark.parametrize("input", input_patch_void)
def test_Verificar_que_no_se_pueda_actualizar_un_profesional_con_valor_vacio(get_url,setup_professional,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda actualizar {input['item']} con un valor vacio")
    request=build_patch_payload(**{input['item']: ""})
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, input['item'], "")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_field_value_response(response.json(), input['item'], setup_professional[input['item']])

def test_Verificar_que_no_se_pueda_actualizar_photo_por_uno_vacio(get_url,setup_professional):
    allure.dynamic.title("DR‑TC113: Verificar que no se pueda actualizar photo por uno vacio")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)