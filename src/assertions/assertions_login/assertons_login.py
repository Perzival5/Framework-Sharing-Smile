
def assert_payload(request, user, password):
    assert request["username"] == user
    assert request["password"] == password

def assert_response(response):
    assert "eyJhbGciOiJIUzI1NiIsInR" in response.json()["access_token"]
    assert response.json()["token_type"] == "Bearer"