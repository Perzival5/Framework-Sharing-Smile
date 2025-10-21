import pytest
import json
from src.assertions.global_assertions import assert_response_status_code
from src.resources.users import users
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.common.static_headers import StaticDataHeaders
from src.common.static_status import StaticStatus
from src.common.payloads.payload_login import login_payload
from src.utils.api_calls import request_function

@pytest.mark.parametrize("user", users)
def test_login(get_url, user):
    request=login_payload(user["username"], user["password"])
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.auth.value,
                                header_type=StaticDataHeaders.header_login.value, payload=request)
    assert_response_status_code(response.status_code, StaticStatus.ok.value)