import pytest
import config 
from src.utils.api_calls import request_function
from src.utils.payload_builders_professionals import build_user_payload
from src.utils.payload_builders_patient import build_patient_payload
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.resources.files import get_file_profile

@pytest.fixture(scope="session")
def get_url():
    return config.BASE_URL

@pytest.fixture(scope="function")
def teardown_professional(get_url):
    id_to_delete = {"value": None}

    def set_id(new_id):
        id_to_delete["value"] = new_id

    yield set_id 
    
    request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.professionals.value}{id_to_delete['value']}",
                                header_type=StaticDataHeaders.header_delete_profesional.value)

@pytest.fixture(scope="function")
def setup_professional(get_url):
    request=build_user_payload()
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    yield response.json()
    request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.professionals.value}{response.json()['id']}",
                                header_type=StaticDataHeaders.header_delete_profesional.value)
    
@pytest.fixture(scope="function")
def setup_create_professional(get_url):
    request=build_user_payload()
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    yield response.json()

#paciente

@pytest.fixture(scope="function")
def teardown_patient(get_url):
    id_to_delete = {"value": None}

    def set_id(new_id):
        id_to_delete["value"] = new_id

    yield set_id 
    
    request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.patients.value}{id_to_delete['value']}",
                                header_type=StaticDataHeaders.header_delete_patient.value)

@pytest.fixture(scope="function")
def setup_create_patient(get_url):
    request=build_patient_payload()
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_profile())
    yield response.json()

@pytest.fixture(scope="function")
def setup_patient(get_url):
    request=build_patient_payload()
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_profile())
    yield response.json()
    request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.patients.value}{response.json()['id']}",
                                header_type=StaticDataHeaders.header_delete_patient.value)