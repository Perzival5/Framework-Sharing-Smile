import pytest
from src.utils.api_calls import request_function
from src.utils.payload_builders_professionals import build_user_payload
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.common.static_status import StaticStatus
from src.resources.files import get_file_profile, get_file_edit
from src.assertions.global_assertions import *

def test_DR_TC_131_Professional(get_url):
    request=build_user_payload()
    response_post = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.professionals.value,
                                header_type=StaticDataHeaders.header_professional.value, payload=request, files=get_file_profile())
    
    request_function(StaticDataVerbs.get.value, get_url, f"{StaticDataModules.professionals.value}{response_post.json()['id']}",
                                header_type=StaticDataHeaders.header_professional.value)
    
    request_patch =build_user_payload()
    request_function(StaticDataVerbs.patch.value, get_url, f"{StaticDataModules.professionals.value}{response_post.json()['id']}",
                                header_type=StaticDataHeaders.header_professional.value, payload=request_patch, files=get_file_edit())
    
    response_delete = request_function(StaticDataVerbs.delete.value, get_url, f"{StaticDataModules.professionals.value}{response_post.json()['id']}",
                                header_type=StaticDataHeaders.header_delete_profesional.value)
    assert_response_status_code(response_delete.status_code, StaticStatus.no_content.value)