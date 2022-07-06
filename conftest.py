import copy
import pytest
import requests





@pytest.fixture
def apiKey():
    endpoint = '/api-clients/'
    baseUrl = "https://simple-books-api.glitch.me"
    endpoint_url = baseUrl + endpoint
    body_parameter = {
        "clientName": "clientName",
        "clientEmail": "clientEmail"
    }
    response = requests.post(endpoint_url, json=body_parameter)
    
    # From the documentation the API Key for one user will last for 7-days.
    # If the same username is used, the endpoint will respond with 409 Error Code
    # In order to use the same username for each test, we use OS library to store the
    # API Key in system environment variable so, so it can be reusable.
    if response.status_code == 409:
        api_key = open('api_key.txt', 'r').read()
        return api_key
    else:
        api_key = response.json()['accessToken']
        open('api_key.txt', mode='w').write(copy.deepcopy(api_key))
        return api_key