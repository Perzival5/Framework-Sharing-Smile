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
from src.utils.payload_builders_patient import build_patient_payload, payload_bad
from src.utils.api_calls import request_function
from src.resources.files import *
from src.resources.request_patient.request_POST_patient import *

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_Verificar_registro_de_paciente_con_todos_los_campos_válidos(get_url,teardown_patient):
    allure.dynamic.title("DR-TC164: Verificar registro de paciente con todos los campos válidos")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_response_patient(response.json(),request)
    teardown_patient(response.json()["id"])

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_Verificar_registro_de_paciente_unicamente_con_los_campos_obligatorios(get_url,teardown_patient):
    allure.dynamic.title("DR-TC165: Verificar registro de paciente únicamente con los campos obligatorios")
    request=build_patient_payload(ref_number_2="",city="", province="", address="")
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_response_patient(response.json(),request)
    teardown_patient(response.json()["id"])

@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(reason= "bug conocido: el campo de tipo de fisura es obligatorio y no puede ser vacio")
@pytest.mark.parametrize("input", register)
def test_Verificar_que_no_se_pueda_registrar_un_paciente_sin(get_url,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda registrar un paciente sin {input['item']}")
    request=build_patient_payload(**{input['item']: ""})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.patients.name)
    assert_reponse_item(response, input['item'])

@pytest.mark.negative
@pytest.mark.regression
def test_Verificar_que_no_se_pueda_registrar_un_paciente_sin_photo(get_url):
    allure.dynamic.title("DR-TC176: Verificar que no se pueda registrar un paciente sin photo")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request)
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.patients.name)
    assert_reponse_item(response, "photo")

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("date", valid_sex)
def test_Verificar_que_se_pueda_registrar_un_paciente_con_datos_validos_es_sex(get_url,date,teardown_patient):
    allure.dynamic.title(f"{date['id']}: Verificar que se puede registrar un paciente con sex {date['input']}")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_response_patient(response.json(),request)
    teardown_patient(response.json()["id"])

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("date", valid_country)
def test_Verificar_que_se_pueda_registrar_un_paciente_con_datos_validos_en_country(get_url,date,teardown_patient):
    allure.dynamic.title(f"{date['id']}: Verificar que se puede registrar un paciente con country {date['title']}")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_response_patient(response.json(),request)
    teardown_patient(response.json()["id"])

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("date", valid_fissure_type)
def test_Verificar_que_se_pueda_registrar_un_paciente_con_datos_validos_en_fissure_type(get_url,date,teardown_patient):
    allure.dynamic.title(f"{date['id']}: Verificar que se puede registrar un paciente con country {date['title']}")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.created.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_response_patient(response.json(),request)
    teardown_patient(response.json()["id"])

#bug
@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("specials", special)
def test_Verificar_que_no_se_complete_el_registro_de_un_paciente_con_solo_caracteres_especiales(get_url,specials):
    allure.dynamic.title(f"{specials['id']}: Verificar que no se complete el registro de un paciente con solo caracteres especiales en {specials['item']}")
    pytest.skip(f"Bug conocido: se puede registrar un paciente con {specials['item']} con solo caracteres especiales")
    request=build_patient_payload(**{specials['item']: specials['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)

@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(reason= "bug conocido: dni, ref_number_1 y ref_number_2 se esta registrando con formato invalido")
@pytest.mark.parametrize("date", input_invalid)
def test_Verificar_que_no_se_pueda_registrar_un_paciente_con_datos_en_formato_invalido(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se registre un paciente con {date['item']} inválido")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)

@pytest.mark.negative
@pytest.mark.regression  
@pytest.mark.parametrize("date", date_birth)
def test_Verificar_que_no_se_complete_el_registre_un_paciente_con_date_of_birth_en_formato_invalido(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se registre un paciente con date_of_birth en formato inválido {date['title']}")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

#bug
@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
def test_Verificar_que_no_se_registre_un_paciente_con_date_of_birth_en_el_futuro(get_url):
    allure.dynamic.title("DR-TC198: Verificar que no se registre un paciente con date_of_birth en el futuro")
    pytest.skip("Bug conocido: si se puede registrar un paciente que aun no a nacio")
    request=build_patient_payload(date_of_birth = StaticInputs.date_future.value)
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

#bug
@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("date", country_invalid)
def test_Verificar_que_no_se_pueda_registrar_un_paciente_con_paises_invalidos(get_url,date,teardown_patient):
    allure.dynamic.title(f"{date['id']}: Verificar que no se registre un paciente con country inválido {date['title']}")
    pytest.skip("Bug conocido: se puede registrar un paciente con paises que no estan en la lista de paises válidos")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)
    teardown_patient(response.json()["id"])

@pytest.mark.negative
@pytest.mark.regression
def test_Verificar_que_no_se_registre_un_paciente_con_photo_path_invalido(get_url):
    allure.dynamic.title("DR-TC202: Verificar que no se registre un paciente con photo_path inválido")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_txt())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.photo.value)

@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(reason="bug conocido: si se pasa del limite de caracteres no te permite registrar un paciente, pero por que la api devuelve un status 500 cuando deberia ser 400 bad request")
@pytest.mark.parametrize("date", input_large)
def test_Verificar_rechazo_en_la_creacion_de_paciente_excediendo_longitud_maxima(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar rechazo en la creación de paciente con {date['item']} excediendo longitud máxima")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", input_large_special_pa)
def test_Verificar_rechazo_en_la_creacion_de_paciente_excediendo_longitud_maxima_sex_country(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar rechazo en la creación de paciente con {date['item']} excediendo longitud máxima")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)

@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
def test_Verificar_rechazo_en_la_creacion_de_paciente_excediendo_tamano_maximo_photo_path(get_url):
    allure.dynamic.title("DR-TC216: Verificar rechazo en la creación de paciente con photo_path excediendo tamaño máximo")
    pytest.skip("Bug conocido: acepta imagenes que superan el limite de tamano permitido")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_BIG())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)

#bug
@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("date", duplicate)
def test_Verificar_que_no_se_registre_un_paciente_con_datos_duplicados(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se registre un paciente con {date['item']} duplicado")
    pytest.skip("Bug conocido: permite registrar paciente con dni igual a de otro paciente")
    request=build_patient_payload(**{date['item']: date['input']})
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", token)
def test_Verificar_que_no_se_pueda_crear_un_paciente_token_invalido(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda crear un paciente {date['title']}")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=date['header'], payload=request, files=get_file_patient())
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, date['message'])

@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.xfail(reason= "bug conocido: el mensaje del error 400 esta mal escrito")
@pytest.mark.parametrize("date", http_methods_invalid)
def test_Verificar_fallo_en_el_registro_de_paciente_con_metodo_HTTP_incorrecto(get_url,date):
    allure.dynamic.title(f"{date['id']}: Verificar fallo en el registro de paciente con método HTTP incorrecto {date['item']}")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(date['item'], get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    assert_responde_falled_http(response, StaticDataModules.patients.name, date['id'])

@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
def test_Verificar_fallo_en_el_registro_de_paciente_con_payload_invalido(get_url):
    allure.dynamic.title("DR-TC225: Verificar fallo en el registro de paciente con payload invalido")
    pytest.skip("Bug conocido: se puede registra un paciente con phone y email que son parametros de profesional un paciente no tiene estos datos")
    request=build_patient_payload()
    request_bad=payload_bad(request)
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request_bad, files=get_file_patient())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)