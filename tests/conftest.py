import pytest
import config 

@pytest.fixture(scope="session")
def get_url():
    return config.BASE_URL

