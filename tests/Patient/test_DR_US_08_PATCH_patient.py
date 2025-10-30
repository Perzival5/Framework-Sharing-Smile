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
from src.utils.payload_builders_patient import *
from src.utils.api_calls import request_function
from src.resources.files import *
from src.resources.request_patient.request_PATCH_patient import *

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_Verificar_actualizar_datos_de_un_paciente_con_todos_los_campos_válidos(get_url,setup_patient):
    allure.dynamic.title("DR‑TC234: Verificar actualización de datos de un paciente con todos los campos válidos")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_response_patient(response.json(),request)

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize("input", input_patch)
def test_Verificar_actualización_exitosa_de_un_paciente_modificando_solo_un_campo(get_url,setup_patient,input):
    allure.dynamic.title(f"{input['id']}: Verificar actualización exitosa de un paciente modificando solo el campo {input['item']}")
    random = build_random_field(input['item'])
    request=build_patch_payload(input['item'], random)
    assert_field_value_input(request, input['item'], random)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_value_response(response.json(), input['item'], random)

@pytest.mark.positive
@pytest.mark.regression
def test_Verificar_actualización_exitosa_de_un_paciente_modificando_el_campo_photo(get_url,setup_patient):
    allure.dynamic.title("DR‑TC247: Verificar actualización exitosa de un paciente modificando solo el campo photo")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_photo_response(response.json(), setup_patient["photo_path"])

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize("input", input_sex_country_fissure_type)
def test_Verificar_que_se_pueda_actualizar_un_paciente_con_datos_validos_es_sex_country_fissure_type(get_url,setup_patient,input):
    allure.dynamic.title(f"{input['id']}: Verificar que se pueda actualizar un paciente con {input['title']}")
    request=build_patch_payload(input['item'], input['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, input['item'], input['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_field_value_response(response.json(), input['item'], input['input'])

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("input", input_patch_void)
def test_Verificar_que_no_se_pueda_actualizar_un_paciente_con_valor_vacio(get_url,setup_patient,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda actualizar {input['item']} con un valor vacio")
    request=build_patch_payload(input['item'], "")
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, input['item'], "")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_field_value_response(response.json(), input['item'], setup_patient[input['item']])

@pytest.mark.negative
@pytest.mark.regression
def test_Verificar_que_no_se_pueda_actualizar_photo_por_uno_vacio(get_url,setup_patient):
    allure.dynamic.title("DR‑TC267: Verificar que no se pueda actualizar photo por uno vacio")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, files={"photo": ""})
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_field_value_response(response.json(), "photo_path", setup_patient["photo_path"])

#bug
@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("input", input_space)
def test_Verificar_que_no_se_pueda_actualizar_un_paciente_con_valor_solo_de_espacios(get_url,setup_patient,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda actualizar {input['item']} con un valor de solo espacios")
    pytest.skip("Bug conocido: permite actualizar los datos por espacios vacios de un paciente")
    request=build_patch_payload(input['item'], " ")
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, input['item'], " ")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_field_value_response(response.json(), input['item'], setup_patient[input['item']])

@pytest.mark.negative
@pytest.mark.regression
def test_Verificar_que_no_se_pueda_actualizar_un_paciente_con_valor_solo_de_espacios_date_of_birth(get_url,setup_patient):
    allure.dynamic.title("DR‑TC273: Verificar que no se pueda actualizar date_of_birth con un valor de solo espacios")
    request=build_patch_payload(StaticInputs.date_of_birth.name, " ")
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, "date_of_birth", " ")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("input", input_space_special)
def test_Verificar_que_no_se_pueda_actualizar_un_paciente_con_valor_solo_de_espacios_date_of_birth_sex_country_fissure_type(get_url,setup_patient,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda actualizar {input['item']} con un valor de solo espacios")
    request=build_patch_payload(input['item'], " ")
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, input['item'], " ")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

#bug
@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("input", special)
def test_Verificar_que_no_se_pueda_actualizar_un_paciente_con_caracteres_especiales(get_url,setup_patient,input):
    allure.dynamic.title(f"{input['id']}: Verificar que no se pueda actualizar {input['item']} con caracteres especiales")
    pytest.skip(f"Bug conocido: se puede actualizar el campo {input['item']} con solo caracteres especiales")
    request=build_patch_payload(input['item'], input['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, input['item'], input['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", date_birth)
def test_Verificar_que_no_se_actualize_un_paciente_con_date_of_birth_en_formato_invalido(get_url,setup_patient,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda actualizar {date['item']} con formato inválido {date['title']}")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

#bug
@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
def test_Verificar_que_no_se_pueda_actualizar_un_paciente_con_date_of_birth_en_el_futuro(get_url,setup_patient):
    allure.dynamic.title("DR‑TC287: Verificar que no se pueda actualizar date_of_birth a una fecha futura")
    pytest.skip("Bug conocido: si se puede cambiar la fecha de nacimiento de un paciente a una fecha futura")
    request=build_patch_payload("date_of_birth" , StaticInputs.date_future.value)
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, StaticInputs.date_of_birth.name, StaticInputs.date_future.value)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.date_of_birth.value)

@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(reason= "bug conocido: dni, ref_number_1, ref_number_2 y country se pueden actualizar con un valor invalido")
@pytest.mark.parametrize("date", input_invalid)
def test_Verificar_que_no_se_pueda_actualizar_un_paciente_con_un_valor_invalido(get_url,date,setup_patient):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda actualizar {date['item']} con un valor inválido")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, date['item'], date['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

@pytest.mark.negative
@pytest.mark.regression
def test_Verificar_que_no_se_actualizar_un_paciente_con_photo_path_invalido(get_url,setup_patient):
    allure.dynamic.title("DR‑TC294: Verificar que no se pueda actualizar photo con un formato invalido")
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, files=get_file_txt())
    assert_response_status_code(response.status_code, StaticStatus.ok.value)
    assert_schema(response.json(), "schema_201_post.json", StaticDataModules.patients.name)
    assert_field_value_response(response.json(), "photo_path", setup_patient["photo_path"])

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", input_large)
def test_Verificar_rechazo_en_actualizar_un_paciente_excediendo_longitud_maxima(get_url,setup_patient,date):
    allure.dynamic.title(f"{date['id']}: Verificar rechazo en actualizar un paciente con {date['item']} excediendo longitud máxima")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, date['item'], date['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", input_large_special_pa)
def test_Verificar_rechazo_en_actualizar_un_paciente_excediendo_longitud_maxima_sex_country(get_url,setup_patient,date):
    allure.dynamic.title(f"{date['id']}: Verificar rechazo en actualizar un paciente con {date['item']} excediendo longitud máxima")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, date['item'], date['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.internal_server_error.value)
    assert_response_500(response)

#bug
@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("date", duplicate)
def test_Verificar_que_no_actualize_un_paciente_con_datos_duplicados(get_url,setup_patient,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda actualizar {date['item']} a un valor ya existente en otro paciente")
    pytest.skip("Bug conocido: permite registrar paciente con dni igual a de otro paciente")
    request=build_patch_payload(date['item'], date['input'])
    assert_schema(request, "schema_input_patch.json", StaticDataModules.patients.name)
    assert_field_value_response(request, date['item'], date['input'])
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", id_not_exist)
def test_Verificar_que_no_se_pueda_actualizar_los_datos_de_un_paciente_con_ID_que_no_existe(get_url, date):
    allure.dynamic.title("DR‑TC309: Verificar que no se pueda actualizar un paciente inexistente")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{date['input']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.not_found.value)
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, StaticInputs.patient_not_found.value)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", id_invalid)
def test_Verificar_que_no_se_pueda_actualizar_los_datos_de_un_paciente_con_ID_invalido(get_url, date):
    allure.dynamic.title("DR‑TC310: Verificar que no se pueda actualizar un paciente con id invalido")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{date['input']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, StaticStatus.unprocessable_entity.value)
    assert_schema(response.json(), "schema_422_post.json", StaticDataModules.patients.name)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("date", token)
def test_Verificar_que_no_se_pueda_actualizar_un_paciente_con_token_invalido(get_url,setup_patient,date):
    allure.dynamic.title(f"{date['id']}: Verificar que no se pueda actualizar un paciente {date['title']}")
    request=build_patient_payload()
    assert_schema(request, "schema_input.json", StaticDataModules.patients.name)
    assert_payload_patient(request)
    response = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{setup_patient['id']}",
                                header_type=date['header'], payload=request, files=get_file_edit())
    assert_response_status_code(response.status_code, date['status'])
    assert_schema(response.json(), "schema_400_post.json", StaticDataModules.patients.name)
    assert_response_validation_error_400_date_photo(response, date['message'])