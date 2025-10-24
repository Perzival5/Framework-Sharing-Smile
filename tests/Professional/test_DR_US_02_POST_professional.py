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
from src.utils.payload_builders_professionals import build_user_payload
from src.utils.api_calls import request_function
from src.resources.files import *
from src.resources.bad_request_POST_profesional import register, special, date_birth, input_invalid, input_large, input_large_special_pro, token, http_methods_invalid, duplicate, valid_sex, valid_country

def test_Verificar_registro_de_profesional_con_todos_los_campos_válidos(get_url,teardown_professional):
    allure.dynamic.title("DR-TC13: Verificar registro de profesional con todos los campos válidos")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_response_profesional(response.json(),request)
    teardown_professional(response.json()["id"])

def test_Verificar_registro_de_profesional_unicamente_con_los_campos_obligatorios(get_url,teardown_professional):
    allure.dynamic.title("DR-TC14: Verificar registro de profesional únicamente con los campos obligatorios")
    request=build_user_payload(city="", province="", address="")
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_response_profesional(response.json(),request)
    teardown_professional(response.json()["id"])

@pytest.mark.parametrize("input", register)
def test_Verificar_que_no_se_pueda_registrar_un_profesional_sin(get_url,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda registrar un profesional sin {input['item']}")
    request=build_user_payload(**{input['item']: ""})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.professionals.name)
    assert_reponse_item(response, input['item'])

def test_Verificar_que_no_se_pueda_registrar_un_profesional_sin_photo(get_url):
    allure.dynamic.title(f"DR-TC25: Verificar que no se pueda registrar un profesional sin photo")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request)
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.professionals.name)
    assert_reponse_item(response, "photo")

#bug
@pytest.mark.parametrize("specials", special)
def test_Verificar_que_no_se_complete_el_registro_de_un_profesional_con_solo_caracteres_especiales(get_url,specials):
    allure.dynamic.title(f"{specials['id']}: Verificar que no se complete el registro de un profesional con solo caracteres especiales en {specials['item']}")
    request=build_user_payload(**{specials['item']: specials['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)

@pytest.mark.parametrize("date", date_birth)
def test_Verificar_que_no_se_complete_el_registre_un_profesional_con_date_of_birth_en_formato_invalido(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se registre un profesional con date_of_birth en formato inválido {date['title']}")
    request=build_user_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

#bug
@pytest.mark.xfail(raises= "si se puede registrar un prefesional que no nacio", run=False)
def test_Verificar_que_no_se_registre_un_profesional_con_date_of_birth_en_el_futuro(get_url):
    allure.dynamic.title("DR-TC30: Verificar que no se registre un profesional con date_of_birth en el futuro")
    request=build_user_payload(date_of_birth = StaticInputs.date_future.value)
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

@pytest.mark.parametrize("date", input_invalid)
def test_Verificar_que_no_se_complete_el_registre_un_profesional_con_date_of_birth_en_formato_invalido(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se registre un profesional con {date['item']} inválido")
    request=build_user_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400(response)

def test_Verificar_que_no_se_registre_un_profesional_con_photo_path_invalido(get_url):
    allure.dynamic.title("DR-TC35: Verificar que no se registre un profesional con photo_path inválido")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_txt())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.photo.value)

@pytest.mark.parametrize("date", input_large)
def test_Verificar_rechazo_en_la_creacion_de_profesional_excediendo_longitud_maxima(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar rechazo en la creación de profesional con {date['item']} excediendo longitud máxima")
    request=build_user_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

@pytest.mark.parametrize("date", input_large_special_pro)
def test_Verificar_rechazo_en_la_creacion_de_profesional_excediendo_longitud_maxima_sex_country(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar rechazo en la creación de profesional con {date['item']} excediendo longitud máxima")
    request=build_user_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400(response)

def test_Verificar_rechazo_en_la_creacion_de_profesional_excediendo_tamano_maximo_photo_path(get_url):
    allure.dynamic.title("DR-TC48: Verificar rechazo en la creación de profesional con photo_path excediendo tamaño máximo")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_BIG())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400(response)

@pytest.mark.parametrize("date", token)
def test_Verificar_que_no_se_pueda_crear_un_profesional_token_invalido(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda crear un profesional {date['title']}")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=date['header'], payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400_date_photo(response, date['message'])

@pytest.mark.parametrize("date", http_methods_invalid)
def test_Verificar_fallo_en_el_registro_de_profesional_con_metodo_HTTP_incorrecto(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar fallo en el registro de profesional con método HTTP incorrecto {date['item']}")
    request=build_user_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(date['item'], get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_responde_falled_http(response, StaticDataModules.professionals.name, date['id'])

@pytest.mark.xfail(raises= "si deja crear duplicados", run=False)
@pytest.mark.parametrize("date", duplicate)
def test_Verificar_que_no_se_registre_un_profesional_con_datos_duplicados(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se registre un profesional con {date['item']} duplicado")
    request=build_user_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.professionals.name)
    assert_response_validation_error_400(response)

@pytest.mark.parametrize("date", valid_sex)
def test_Verificar_que_se_pueda_registrar_un_profesional_con_datos_validos_es_sex(get_url,date,teardown_professional):
    allure.dynamic.title(f"{date['id']}: Verificar que se puede registrar un profesional con sex {date['input']}")
    request=build_user_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_response_profesional(response.json(),request)
    teardown_professional(response.json()["id"])

@pytest.mark.parametrize("date", valid_country)
def test_Verificar_que_se_pueda_registrar_un_profesional_con_datos_validos_en_country(get_url,date,teardown_professional):
    allure.dynamic.title(f"{date['id']}: Verificar que se puede registrar un profesional con country {date['title']}")
    request=build_user_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.professionals.name)
    assert_payload_professional(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.professionals.name)
    assert_response_profesional(response.json(),request)
    teardown_professional(response.json()["id"])