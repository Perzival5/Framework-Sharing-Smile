import pytest
from src.utils.api_calls import request_function
from src.utils.payload_builders_patient import build_patient_payload
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.common.static_status import StaticStatus
from src.resources.files import *
from src.assertions.global_assertions import *

@pytest.mark.e2e
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC_130_Patient(get_url):
    request=build_patient_payload()
    response_post = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.patients.value,
                                header_type=StaticDataHeaders.header_patient.value, payload=request, files=get_file_patient())
    
    response_get = request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.patients.value}{response_post.json()['id']}",
                                header_type=StaticDataHeaders.header_patient.value)
    
    request_patch=build_patient_payload()
    response_patch = request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.patients.value}{response_get.json()['id']}",
                                header_type=StaticDataHeaders.header_patient.value, payload=request_patch, files=get_file_edit())
    
    request_function(StaticDataVerbs.post.value, get_url, f"{StaticDataModules.patients.value}{response_patch.json()['id']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value, payload={}, files=get_file_patient_photo())

    request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.patients.value}{response_patch.json()['id']}{StaticDataModules.photo.value}",
                                header_type=StaticDataHeaders.header_patient.value)
    
    response_delete = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.patients.value}{response_patch.json()['id']}",
                                header_type=StaticDataHeaders.header_delete_patient.value)
    
    assert_response_status_code(response_delete.status_code, StaticStatus.no_content.value)