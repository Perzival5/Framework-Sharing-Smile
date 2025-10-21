from .logger import *
from src.common.url import get_url_parametrized
from src.headers.headers import generate_headers
import requests

def request_function(method ,get_url, module, code = None, header_type = None, payload = None):
    url = get_url_parametrized(get_url, module, code)
    headers = generate_headers(header_type)
    response = requests.request(method, url, headers=headers, data=payload)
    log_method(method)
    log_domain(get_url)
    log_request(url, headers, payload)
    log_timestamp()
    return response