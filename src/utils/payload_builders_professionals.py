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
        "first_name": first_name or fake.first_name(),
        "last_name": last_name or fake.last_name(),
        "date_of_birth": date_of_birth or fake.date_of_birth(minimum_age=18, maximum_age=70).strftime("%d/%m/%Y"),
        "sex": sex or random.choice(["masculino", "femenino"]),
        "country": country or random.choice(list(COUNTRIES.values())),
        "dni": dni or str(fake.random_number(digits=8, fix_len=True)),
        "personal_email": personal_email or fake.email(),
        "phone": phone or str(fake.random_number(digits=8, fix_len=True)),
        "profession": profession or fake.job(),
        "specialty": specialty or fake.word(),
        "city": city or fake.city(),
        "province": province or fake.state(),
        "address": address or fake.address(),
    }
    
    return payload
