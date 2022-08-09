import pytest
from endpoints.apiClient import ApiClient



@pytest.mark.parametrize("clientName, clientEmail", [
    (12345, 12345), ("JohnDoe", 12345), (12345, "JohnDoe@example.com")
])
def test_api_client_body_parameter(clientName, clientEmail):

    api_client = ApiClient()
    api_client.setup_api_client_detail(name=clientName, email=clientEmail)
    api_client.register_api_client()

    assert api_client == 400