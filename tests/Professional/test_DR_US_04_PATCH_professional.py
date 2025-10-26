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
from src.resources.request_PATCH_profesional import *

def test_Verificar_actualizar_datos_de_un_profesional_con_todos_los_campos_válidos(get_url,setup_professional):
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
    request=build_patch_payload(input['item'], random)
    assert_field_value_input(request, input['item'], random)
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
    request=build_patch_payload(input['item'], input['input'])
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
    request=build_patch_payload(input['item'], "")
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
                                header_type=StaticDataHeaders.header_professional.value, files={"photo": ""})
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_field_value_response(response.json(), "photo_path", setup_professional["photo_path"])

#bug
@pytest.mark.xfail(raises= "se puede actualizar los campos por espacios vacios", run=False)
@pytest.mark.parametrize("input", input_space)
def test_Verificar_que_no_se_pueda_actualizar_un_profesional_con_valor_solo_de_espacios(get_url,setup_professional,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda actualizar {input['item']} con un valor de solo espacios")
    request=build_patch_payload(input['item'], " ")
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, input['item'], " ")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_field_value_response(response.json(), input['item'], setup_professional[input['item']])

def test_Verificar_que_no_se_pueda_actualizar_un_profesional_con_valor_solo_de_espacios_date_of_birth(get_url,setup_professional):
    allure.dynamic.title("DR‑TC120: Verificar que no se pueda actualizar date_of_birth con un valor de solo espacios")
    request=build_patch_payload(StaticInputs.date_of_birth.name, " ")
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, "date_of_birth", " ")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

@pytest.mark.parametrize("input", input_space_special)
def test_Verificar_que_no_se_pueda_actualizar_un_profesional_con_valor_solo_de_espacios_date_of_birth_sex_country_personal_email(get_url,setup_professional,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda actualizar {input['item']} con un valor de solo espacios")
    request=build_patch_payload(input['item'], " ")
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, input['item'], " ")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

#bug
@pytest.mark.xfail(raises= "se puede actualizar los campos con solo caracteres especiales", run=False)
@pytest.mark.parametrize("input", special)
def test_Verificar_que_no_se_pueda_actualizar_un_profesional_con_caracteres_especiales(get_url,setup_professional,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda actualizar {input['item']} con caracteres especiales")
    request=build_patch_payload(input['item'], input['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, input['item'], input['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400(response)

@pytest.mark.parametrize("date", date_birth)
def test_Verificar_que_no_se_actualize_un_profesional_con_date_of_birth_en_formato_invalido(get_url,setup_professional,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda actualizar {date['item']} con formato inválido {date['title']}")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

#bug
@pytest.mark.xfail(raises= "si se puede cambiar la fecha de un profesional a una fecha futura", run=False)
def test_Verificar_que_no_se_pueda_actualizar_un_profesional_con_date_of_birth_en_el_futuro(get_url,setup_professional):
    allure.dynamic.title("DR‑TC127: Verificar que no se pueda actualizar date_of_birth a una fecha futura")
    request=build_patch_payload("date_of_birth" , StaticInputs.date_future.value)
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, StaticInputs.date_of_birth.name, StaticInputs.date_future.value)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

@pytest.mark.parametrize("date", input_invalid)
def test_Verificar_que_no_se_pueda_actualizar_un_profesional_con_un_valor_invalido(get_url,date,setup_professional):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda actualizar {date['item']} con un valor inválido")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, date['item'], date['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

def test_Verificar_que_no_se_actualizar_un_profesional_con_photo_path_invalido(get_url,setup_professional):
    allure.dynamic.title("DR‑TC132: Verificar que no se pueda actualizar photo con un formato invalido")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, files=get_file_txt())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_field_value_response(response.json(), "photo_path", setup_professional["photo_path"])

@pytest.mark.parametrize("date", input_large)
def test_Verificar_rechazo_en_actualizar_un_profesional_excediendo_longitud_maxima(get_url,setup_professional,date):
    allure.dynamic.title(f"{date['id']}: Verificar rechazo en actualizar un profesional con {date['item']} excediendo longitud máxima")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, date['item'], date['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

@pytest.mark.parametrize("date", input_large_special_pro)
def test_Verificar_rechazo_en_actualizar_un_profesional_excediendo_longitud_maxima_sex_country(get_url,setup_professional,date):
    allure.dynamic.title(f"{date['id']}: Verificar rechazo en actualizar un profesional con {date['item']} excediendo longitud máxima")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, date['item'], date['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

@pytest.mark.xfail(raises= "si deja crear duplicados", run=False)
@pytest.mark.parametrize("date", duplicate)
def test_Verificar_que_no_actualize_un_profesional_con_datos_duplicados(get_url,setup_professional,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda actualizar {date['item']} a un valor ya existente en otro profesional")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.professionals.name)
    assert_field_value_response(request, date['item'], date['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400(response)

@pytest.mark.parametrize("date", id_not_exist)
def test_Verificar_que_no_se_pueda_actualizar_los_datos_de_un_profesional_con_ID_que_no_existe(get_url, date):
    allure.dynamic.title("DR‑TC148: Verificar que no se pueda actualizar un profesional inexistente")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{date['input']}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.not_found.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.professional_not_found.value)

@pytest.mark.parametrize("date", token)
def test_Verificar_que_no_se_pueda_actualizar_un_profesional_con_token_invalido(get_url,setup_professional,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda actualizar un profesional {date['title']}")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{setup_professional["id"]}",
                                header_type=date['header'], payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, date['message'])
