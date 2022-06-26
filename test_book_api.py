import requests



def test_getting_all_books(baseUrl):
    endpoint = "/books/"
    endpoint_url = baseUrl + endpoint
    response = requests.get(endpoint_url)
    assert response.status_code == 200

def test_getting_single_book(baseUrl):
    endpoint = "/books/1"
    endpoint_url = baseUrl + endpoint
    status_code = requests.get(endpoint_url).status_code
    assert status_code == 200

def test_submitting_order(baseUrl, httpHeaders):
    endpoint = "/orders/"
    endpoint_url = baseUrl + endpoint

    request_body = {
        "bookId": 4,
        "customerName": "Bourne"
    }
    status_code = requests.post(endpoint_url, json=request_body,
        headers=httpHeaders).status_code
    assert status_code == 201

def test_geting_all_ordered_books(baseUrl, httpHeaders, orderId):
    endpoint = f"/orders/{orderId}"
    endpoint_url = baseUrl + endpoint
    status_code = requests.get(endpoint_url, headers=httpHeaders).status_code
    assert status_code == 200

def test_getting_single_ordered_books(baseUrl, httpHeaders, orderId):
    endpoint = f"/orders/{orderId}"
    endpoint_url = baseUrl + endpoint
    status_code = requests.get(endpoint_url, headers=httpHeaders).status_code
    assert status_code == 200

def test_updating_ordered_book(baseUrl, httpHeaders, orderId):
    endpoint = f"/orders/{orderId}"
    endpoint_url = baseUrl + endpoint
    request_body = {
        "customerName": "Borneo"
    }

    status_code = requests.patch(endpoint_url, json=request_body,
        headers=httpHeaders).status_code
    assert status_code == 204

def test_delete_order(baseUrl, httpHeaders, orderId):
    endpoint = f"/orders/{orderId}"
    endpoint_url = baseUrl + endpoint

    status_code = requests.patch(endpoint_url, headers=httpHeaders).status_code
    assert status_code == 204