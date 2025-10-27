from faker import Faker
from src.resources.countries_profesional import COUNTRIES
import random

fake = Faker()

def build_patient_payload(
    first_name: str | None = None,
    last_name: str | None = None,
    date_of_birth: str | None = None,
    sex: str | None = None,
    country: str | None = None,
    dni: str | None = None,
    father_name: str | None = None,
    mother_name: str | None = None,
    fissure_type: str | None = None,
    ref_number_1: str | None = None,
    ref_number_2: str | None = None,
    city: str | None = None,
    province: str | None = None,
    address: str | None = None,
) -> dict:
    payload = {
        "first_name": fake.first_name() if first_name is None else first_name,
        "last_name": fake.last_name() if last_name is None else last_name,
        "date_of_birth": (
            fake.date_of_birth(minimum_age=1, maximum_age=18).strftime("%d/%m/%Y")
            if date_of_birth is None else date_of_birth
        ),
        "sex": random.choice(["masculino", "femenino"]) if sex is None else sex,
        "country": random.choice(list(COUNTRIES.values())) if country is None else country,
        "dni": str(fake.random_number(digits=8, fix_len=True)) if dni is None else dni,
        "father_name": fake.first_name_male() if father_name is None else father_name,
        "mother_name": fake.first_name_female() if mother_name is None else mother_name,
        "fissure_type": random.choice(["Flap izq", "Flap Bilateral", "Flap der"]) if fissure_type is None else fissure_type,
        "ref_number_1": str(fake.random_number(digits=8, fix_len=True)) if ref_number_1 is None else ref_number_1,
        "ref_number_2": str(fake.random_number(digits=8, fix_len=True)) if ref_number_2 is None else ref_number_2,
        "city": fake.city() if city is None else city,
        "province": fake.state() if province is None else province,
        "address": fake.address() if address is None else address,
    }
    return payload


def build_patch_payload(field, value) -> dict:
    return {field: value}


def build_random_field(field) -> str:
    if field == "first_name":
        return fake.first_name()
    if field == "last_name":
        return fake.last_name()
    if field == "date_of_birth":
        return fake.date_of_birth(minimum_age=1, maximum_age=18).strftime("%d/%m/%Y")
    if field == "sex":
        return random.choice(["masculino", "femenino"])
    if field == "country":
        return random.choice(list(COUNTRIES.values()))
    if field == "dni":
        return str(fake.random_number(digits=8, fix_len=True))
    if field == "father_name":
        return fake.first_name_male()
    if field == "mother_name":
        return fake.first_name_female()
    if field == "fissure_type":
        return random.choice(["Flap izq", "Flap Bilateral", "Flap der"])
    if field == "ref_number_1":
        return str(fake.random_number(digits=8, fix_len=True))
    if field == "ref_number_2":
        return str(fake.random_number(digits=8, fix_len=True))
    if field == "city":
        return fake.city()
    if field == "province":
        return fake.state()
    if field == "address":
        return fake.address()

    raise ValueError(f"Campo no soportado: {field}")