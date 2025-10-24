from faker import Faker
from src.resources.countries_profesional import COUNTRIES
import random

fake = Faker()

def build_user_payload(
    first_name: str | None = None,
    last_name: str | None = None,
    date_of_birth: str | None = None,
    sex: str | None = None,
    country: str | None = None,
    dni: str | None = None,
    personal_email: str | None = None,
    phone: str | None = None,
    profession: str | None = None,
    specialty: str | None = None,
    city: str | None = None,
    province: str | None = None,
    address: str | None = None,
) -> dict:
    payload = {
        "first_name": fake.first_name() if first_name is None else first_name,
        "last_name": fake.last_name() if last_name is None else last_name,
        "date_of_birth": (
            fake.date_of_birth(minimum_age=18, maximum_age=70).strftime("%d/%m/%Y")
            if date_of_birth is None else date_of_birth
        ),
        "sex": random.choice(["masculino", "femenino"]) if sex is None else sex,
        "country": random.choice(list(COUNTRIES.values())) if country is None else country,
        "dni": str(fake.random_number(digits=8, fix_len=True)) if dni is None else dni,
        "personal_email": fake.email() if personal_email is None else personal_email,
        "phone": str(fake.random_number(digits=8, fix_len=True)) if phone is None else phone,
        "profession": fake.job() if profession is None else profession,
        "specialty": fake.word() if specialty is None else specialty,
        "city": fake.city() if city is None else city,
        "province": fake.state() if province is None else province,
        "address": fake.address() if address is None else address,
    }
    
    return payload

def build_patch_payload(
    first_name: str | None = None,
    last_name: str | None = None,
    date_of_birth: str | None = None,
    sex: str | None = None,
    country: str | None = None,
    dni: str | None = None,
    personal_email: str | None = None,
    phone: str | None = None,
    profession: str | None = None,
    specialty: str | None = None,
    city: str | None = None,
    province: str | None = None,
    address: str | None = None,
) -> dict:
    payload = {}

    if first_name is not None:
        payload["first_name"] = first_name
    if last_name is not None:
        payload["last_name"] = last_name
    if date_of_birth is not None:
        payload["date_of_birth"] = date_of_birth
    if sex is not None:
        payload["sex"] = sex
    if country is not None:
        payload["country"] = country
    if dni is not None:
        payload["dni"] = dni
    if personal_email is not None:
        payload["personal_email"] = personal_email
    if phone is not None:
        payload["phone"] = phone
    if profession is not None:
        payload["profession"] = profession
    if specialty is not None:
        payload["specialty"] = specialty
    if city is not None:
        payload["city"] = city
    if province is not None:
        payload["province"] = province
    if address is not None:
        payload["address"] = address

    return payload

def build_random_field(field) -> dict:
    if field == "first_name":
        return {"first_name": fake.first_name()}
    if field == "last_name":
        return {"last_name": fake.last_name()}
    if field == "date_of_birth":
        return {"date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=70).strftime("%d/%m/%Y")}
    if field == "sex":
        return {"sex": random.choice(["masculino", "femenino"])}
    if field == "country":
        return {"country": random.choice(list(COUNTRIES.values()))}
    if field == "dni":
        return {"dni": str(fake.random_number(digits=8, fix_len=True))}
    if field == "personal_email":
        return {"personal_email": fake.email()}
    if field == "phone":
        return {"phone": str(fake.random_number(digits=8, fix_len=True))}
    if field == "profession":
        return {"profession": fake.job()}
    if field == "specialty":
        return {"specialty": fake.word()}
    if field == "city":
        return {"city": fake.city()}
    if field == "province":
        return {"province": fake.state()}
    if field == "address":
        return {"address": fake.address()}

    raise ValueError(f"Campo no soportado: {field}")