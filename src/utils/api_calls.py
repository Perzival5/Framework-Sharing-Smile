
import requests
from src.common.url import get_url_parametrized
from src.headers.headers import generate_headers

def request_function(method ,get_url, module, code = None, header_type = None, payload = None):
    url = get_url_parametrized(get_url, module, code)
    headers = generate_headers(header_type)
    response = requests.request(method, url, headers=headers, data=payload)
    return response