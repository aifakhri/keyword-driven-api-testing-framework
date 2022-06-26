import copy
import pytest
import requests





@pytest.fixture
def baseUrl():
    return "https://simple-books-api.glitch.me"

@pytest.fixture
def httpHeaders(baseUrl):
    endpoint = '/api-clients/'
    endpoint_url = baseUrl + endpoint
    body_parameter = {
        "clientName": "tester3",
        "clientEmail": "tester3@zeit.de"
    }
    response = requests.post(endpoint_url, json=body_parameter)
    
    # From the documentation the API Key for one user will last for 7-days.
    # If the same username is used, the endpoint will respond with 409 Error Code
    # In order to use the same username for each test, we use OS library to store the
    # API Key in system environment variable so, so it can be reusable.
    if response.status_code == 409:
        api_key = open('api_key.txt', 'r').read()
        headers = {'Authorization': api_key}
        return headers
    else:
        api_key = response.json()['accessToken']
        open('api_key.txt', mode='w').write(copy.deepcopy(api_key))
        headers = {'Authorization': api_key}
        return headers

@pytest.fixture
def orderId(baseUrl, httpHeaders):
    endpoint = "/orders/"
    endpoint_url = baseUrl + endpoint
    body_parameter = {
        "bookId": 1,
        "customerName": "Maximilan"
    }
    response = requests.post(endpoint_url, json=body_parameter,
        headers=httpHeaders).json()
    order_id = response['orderId']
    return order_id