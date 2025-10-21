import logging
import allure
from datetime import datetime
from urllib.parse import urlparse
import requests

def setup_logger():
    logger = logging.getLogger("api_logger")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = logging.FileHandler("api.log", mode="a", encoding="utf-8")
        handler.setLevel(logging.DEBUG)
        fmt = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
    return logger

logger = setup_logger()

def log_method(method: str):
    logger.info(f"HTTP method: {method}")
    allure.attach(method or "", name="HTTP Method", attachment_type=allure.attachment_type.TEXT)

def log_domain(url: str):
    domain = urlparse(url).netloc
    logger.info(f"Domain: {domain}")
    allure.attach(domain, name="Domain", attachment_type=allure.attachment_type.TEXT)

def log_request(url: str, headers: dict, payload: dict | None):
    logger.debug(f"Request URL: {url}")
    logger.debug(f"Request headers: {headers}")
    logger.debug(f"Request payload: {payload}")
    allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(headers), name="Headers", attachment_type=allure.attachment_type.JSON)
    allure.attach(str(payload or {}), name="Payload", attachment_type=allure.attachment_type.JSON)

def log_timestamp():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Timestamp: {ts}")
    allure.attach(ts, name="Timestamp", attachment_type=allure.attachment_type.TEXT)

def log_response(response: requests.Response):
    code = response.status_code
    logger.info(f"Status code: {code}")
    allure.attach(str(code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

    hdrs = dict(response.headers)
    logger.debug(f"Response headers: {hdrs}")
    allure.attach(str(hdrs), name="Response Headers", attachment_type=allure.attachment_type.JSON)

    try:
        body = response.json()
        logger.debug(f"Response payload: {body}")
        allure.attach(str(body), name="Response Payload", attachment_type=allure.attachment_type.JSON)
    except ValueError:
        text = response.text
        logger.debug(f"Response text: {text}")
        allure.attach(text, name="Response Text", attachment_type=allure.attachment_type.TEXT)