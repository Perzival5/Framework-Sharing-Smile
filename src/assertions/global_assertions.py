import json
import os
import jsonschema
import pytest

def assert_response_status_code(status_code, expected_code):
    assert status_code == expected_code, f"Status esperado {expected_code}, Status obtenido {status_code}"

def assert_schema_resource(json_name, file):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas',f"schema_{file}", json_name)
    with open(file_path) as schema_file:
        return json.load(schema_file)
    
def assert_schema(response, json_file, file):
    schema = assert_schema_resource(json_file, file)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match: {err}")