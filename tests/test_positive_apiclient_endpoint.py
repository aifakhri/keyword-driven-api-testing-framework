import pytest
from endpoints.apiClient import ApiClient



@pytest.mark.parametrize("custName, custEmail, expected_status_code", [ 
    ("random", "random@something.com", 201),
    ("random", "random@something.com", 409),
])
def test_api_client_endpoint(custName, custEmail, expected_status_code):
    api_client = ApiClient()
    api_client.setup_api_client_detail(name=custName, email=custEmail)
    api_client.register_api_client()

    assert api_client.checking_status_code() == expected_status_code