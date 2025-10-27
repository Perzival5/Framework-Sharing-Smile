import re
from datetime import datetime
from src.assertions.global_assertions import *
from src.common.static_status import StaticStatus

def assert_payload_patient(request):
    required_fields = [
        "address",
        "city",
        "country",
        "date_of_birth",
        "dni",
        "father_name",
        "first_name",
        "fissure_type",
        "last_name",
        "mother_name",
        "province",
        "ref_number_1",
        "ref_number_2",
        "sex",
    ]

    for field in required_fields:
        value = request[field]
        assert value not in (None, ""), f" Campo '{field}' está vacío o None"


def normalize_date(date_str):
    if not date_str:
        return None
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha no reconocido: {date_str}")

def assert_response_patient(response, request):
    fields_to_check = [
        "address",
        "city",
        "country",
        "date_of_birth",
        "dni",
        "father_name",
        "first_name",
        "fissure_type",
        "last_name",
        "mother_name",
        "province",
        "ref_number_1",
        "ref_number_2",
        "sex",
    ]

    for field in fields_to_check:
        req_val = request.get(field)
        res_val = response.get(field)

        if field == "date_of_birth":
            req_date = normalize_date(req_val)
            res_date = normalize_date(res_val)
            assert req_date == res_date, (
                f"Campo '{field}' no coincide. "
                f"Esperado: {req_date}, Recibido: {res_date}"
            )
            continue

        if req_val in ("", None) and res_val is None:
            continue

        assert res_val == req_val, (
            f"Campo '{field}' no coincide. "
            f"Esperado: {req_val}, Recibido: {res_val}"
        )

    photo_path = response.get("photo_path")
    assert isinstance(photo_path, str) and re.match(r"^https?://", photo_path), \
        f"photo_path no es un link válido: {photo_path}"

    assert isinstance(response.get("id"), int), \
        f"id no es un entero: {response.get('id')}"

    assert response.get("is_deleted") is False, \
        f"is_deleted debería ser False, recibido: {response.get('is_deleted')}"

def assert_reponse_item(response, missing_field):
    detail = response.json().get("detail", [])
    assert any(
        err.get("loc") == ["body", missing_field] and err.get("type") == "missing"
        for err in detail
    ), f"No se encontró error de campo requerido para '{missing_field}' en {detail}"

def assert_response_validation_error_400(response):
    detail = response.json().get("detail", "")
    expected = "1 validation error for PatientCreate"
    assert expected in detail, (
        f"No se encontró el mensaje esperado en detail.\n"
        f"Esperado (parcial): {expected}\n"
        f"Recibido: {detail}"
    )

def assert_response_validation_error_400_date_photo(response, expected_message):
    detail = response.json().get("detail")
    assert detail == expected_message, (
        f"Mensaje inesperado en detail.\n"
        f"Esperado: {expected_message}\n"
        f"Recibido: {detail}"
    )

def assert_response_500(response):

    body = getattr(response, "text", None) or getattr(response, "content", b"")
    if isinstance(body, bytes):
        try:
            body = body.decode("utf-8", errors="ignore")
        except Exception:
            body = str(body)

    expected = "Internal Server Error"
    assert body.strip() == expected, (
        f"Mensaje inesperado en body.\n"
        f"Esperado: {expected}\n"
        f"Recibido: {body}"
    )

def assert_responde_falled_http(response, file, type):
    if type == "DR-TC220":
        assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
        assert "<title>Error 400 (Bad Request)!!1</title>" in response.text

    elif type == "DR-TC221" or type == "DR-TC222" or type == "DR-TC232" or type == "DR-TC233":
        assert_response_status_code(response.status_code, StaticStatus.method_not_allowed.value)
        assert_schema(response.json(), "schema_405.json", file)
        assert response.json()["detail"] == "Method Not Allowed"

    else:
        raise ValueError(f"Tipo de caso no soportado: {type}")
    
#get

def assert_patients_list_format(response_data):
    if isinstance(response_data, dict):
        response_list = [response_data]
    elif isinstance(response_data, list):
        response_list = response_data
    else:
        raise AssertionError(f"Respuesta inesperada: {type(response_data)}")

    assert len(response_list) > 0, "La lista de pacientes está vacía"
    nullable_fields = {"city", "province", "address", "ref_number_2"}

    for idx, prof in enumerate(response_list, start=1):
        for field, value in prof.items():
            if field not in nullable_fields:
                assert value not in ("", None), f"Campo '{field}' vacío en item {idx}"

            if field == "date_of_birth":
                try:
                    datetime.strptime(value, "%Y-%m-%d")
                except Exception:
                    raise AssertionError(f"date_of_birth inválido en item {idx}: {value}")

            if field == "photo_path":
                assert re.match(r"^https?://", value), \
                    f"photo_path inválido en item {idx}: {value}"

            if field == "id":
                assert isinstance(value, int) and value > 0, \
                    f"id inválido en item {idx}: {value}"

            if field == "is_deleted":
                assert isinstance(value, bool), f"is_deleted no es booleano en item {idx}: {value}"
                assert value is False, f"is_deleted debería ser False en item {idx}, recibido: {value}"

#patch

def assert_field_value_response(response_json, field, expected_value):

    actual_value = response_json.get(field)

    if field == "date_of_birth" and expected_value:
        try:
            if "/" in expected_value and "-" not in expected_value:
                parts = expected_value.split("/")
                if len(parts[0]) == 4:  
                    expected_value = datetime.strptime(expected_value, "%Y/%m/%d").strftime("%Y-%m-%d")
                elif int(parts[0]) > 12:
                    expected_value = datetime.strptime(expected_value, "%d/%m/%Y").strftime("%Y-%m-%d")
                else:
                    expected_value = datetime.strptime(expected_value, "%m/%d/%Y").strftime("%Y-%m-%d")
            elif "-" in expected_value:
                datetime.strptime(expected_value, "%Y-%m-%d")
        except ValueError:
            raise AssertionError(f"Formato inválido para expected_value en date_of_birth: {expected_value}")

    assert str(actual_value) == str(expected_value), (
        f"El campo '{field}' no coincide. "
        f"Esperado: {expected_value}, Recibido: {actual_value}"
    )

def assert_photo_response(response_json, old_value):
    actual_value = response_json.get("photo_path")
    assert actual_value == old_value

def assert_field_value_input(response_json, field, expected_value):
    actual_value = response_json.get(field)
    assert str(actual_value) == str(expected_value), (
        f"El campo '{field}' no coincide. "
        f"Esperado: {expected_value}, Recibido: {actual_value}"
    )

#photo
def assert_response_photo(response_json, expected_value):
    actual_value = response_json.json()["id"]
    assert str(actual_value) == str(expected_value), (
        f"El id no coincide."
        f"Esperado: {expected_value}, Recibido: {actual_value}"
    )

def assert_response_photo_id(response):
    expected = {
        "id": 1,
        "url": "https://i.ibb.co/DDZmmxj6/7762183001d7.jpg",
        "filename": "ddf5736f3b364ae5ae247e68b57caee0.jpeg",
        "created_at": "2025-10-27T01:03:49"
    }
    data = response.json()[0] 
    assert data == expected

