import re
from datetime import datetime
from src.assertions.global_assertions import *
from src.common.static_status import StaticStatus

def assert_payload_professional(request):
    required_fields = [
        "first_name",
        "last_name",
        "date_of_birth",
        "sex",
        "country",
        "dni",
        "personal_email",
        "phone",
        "profession",
        "specialty",
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

def assert_response_profesional(response, request):
    fields_to_check = [
        "first_name",
        "last_name",
        "date_of_birth",
        "sex",
        "country",
        "city",
        "province",
        "address",
        "dni",
        "personal_email",
        "phone",
        "profession",
        "specialty",
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
    expected = "1 validation error for ProfessionalCreate"
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
    if type == "DR-TC50":
        assert_response_status_code(response.status_code, StaticStatus.bad_request.value)
        assert "<title>Error 400 (Bad Request)!!!</title>" in response.text

    elif type == "DR-TC51" or type == "DR-TC52" or type == "DR-TC79" or type == "DR-TC80":
        assert_response_status_code(response.status_code, StaticStatus.method_not_allowed.value)
        assert_schema(response.json(), "schema_405.json", file)
        assert response.json()["detail"] == "Method Not Allowed"

    else:
        raise ValueError(f"Tipo de caso no soportado: {type}")
    
#get

def assert_professionals_list_format(response_data):
    if isinstance(response_data, dict):
        response_list = [response_data]
    elif isinstance(response_data, list):
        response_list = response_data
    else:
        raise AssertionError(f"Respuesta inesperada: {type(response_data)}")

    assert len(response_list) > 0, "La lista de profesionales está vacía"
    nullable_fields = {"city", "province", "address"}

    for idx, prof in enumerate(response_list, start=1):
        for field, value in prof.items():
            if field not in nullable_fields:
                assert value not in ("", None), f"Campo '{field}' vacío en item {idx}"


            if field == "date_of_birth":
                try:
                    datetime.strptime(value, "%Y-%m-%d")
                except Exception:
                    raise AssertionError(f"date_of_birth inválido en item {idx}: {value}")

            if field == "personal_email":
                assert re.match(r"[^@]+@[^@]+\.[^@]+", value), \
                    f"Email inválido en item {idx}: {value}"

            if field == "photo_path":
                assert re.match(r"^https?://", value), \
                    f"photo_path inválido en item {idx}: {value}"

            if field == "id":
                assert isinstance(value, int) and value > 0, \
                    f"id inválido en item {idx}: {value}"

            if field == "is_deleted":
                assert isinstance(value, bool), f"is_deleted no es booleano en item {idx}: {value}"
                assert value is False, f"is_deleted debería ser False en item {idx}, recibido: {value}"

