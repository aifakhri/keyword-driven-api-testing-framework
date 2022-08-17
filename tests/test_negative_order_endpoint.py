import pytest
from endpoints.orders import OrderEndpoint



@pytest.mark.parametrize("bookId, custName", [
    ("someBook", "Some Customer"),
    (1, 2022),
    ("1", "Some Customer"),
    (21, "Some Customer")
])
def test_submit_string_bookId(apiToken, bookId, custName):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiToken)
    orders.setup_request_body(bookId=bookId, customerName=custName)
    
    orders.submitting_book_order()
    assert orders.checking_status_code() == 400


@pytest.mark.parametrize("custName", [
    200, 1.2, True
])
def test_update_customer_with_integer(apiToken, custName):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiToken)
    orders.updating_ordered_book_record(customerName=custName)
    
    assert orders.checking_status_code() == 404


@pytest.mark.parametrize("method, orderId", [
    ("GET", True), ("GET", False), ("PATCH", ""), ("DELETE", "")
])
def test_order_endpoint_method_with_random_apikey(method, orderId):
    apikey = "RandomAPIKey"
    orders = OrderEndpoint()
    orders.setup_auth_headers(apikey)
    orders.setup_request_body(bookId=1, customerName="John")
    orders.getting_order_id()
    
    if method == "GET" and orderId == False:
        orders.getting_all_ordered_book_records()
    elif method == "GET" and orderId == True:
        orders.getting_single_ordered_book_record()
    elif method == "PATCH":
        orders.updating_ordered_book_record(customerName="Kevin")
    elif method == "DELETE":
        orders.deleting_ordered_book_entry()

    assert orders.checking_status_code() == 401


@pytest.mark.parametrize("method", [
    "GET", "PATCH", "DELETE"
])
def test_order_endpoint_with_random_orderId(apiToken, method):
    orderId = "RandomOrderId"
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiToken)

    if method == "GET":
        orders.getting_single_ordered_book_record(orderId=orderId)
    elif method == "PATCH":
        orders.updating_ordered_book_record(customerName="gru")
    elif method == "DELETE":
        orders.deleting_ordered_book_entry(orderId=orderId)

    assert orders.checking_status_code() == 404