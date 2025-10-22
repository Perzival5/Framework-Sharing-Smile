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

