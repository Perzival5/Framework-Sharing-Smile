import pytest
import config 
from src.utils.api_calls import request_function
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders

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

