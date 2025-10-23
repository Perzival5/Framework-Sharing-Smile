import re
from datetime import datetime

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
    expected = "1 validation error for ProfessionalCreate\nsex\n  Value error"
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

