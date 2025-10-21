import json
import os
import jsonschema
import pytest

def assert_response_status_code(status_code, expected_code):
    assert status_code == expected_code, f"Status esperado {expected_code}, Status obtenido {status_code}"