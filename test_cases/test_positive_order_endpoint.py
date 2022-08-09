import pytest

from endpoints.orders import OrderEndpoint



@pytest.mark.parametrize("bookId, status_code", [
    (1, 201), (2, 404)
])
def test_submitting_book_order(apiToken, bookId, status_code):
    orders = OrderEndpoint()
    orders.setup_request_body(bookId=bookId, customerName="Jumbo")
    orders.setup_auth_headers(apiToken)

    orders.submitting_book_order()
    assert orders.checking_status_code() == status_code

def test_multiple_ordered_books_record(apiToken):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiToken)
    
    orders.getting_all_ordered_books_record()
    assert orders.checking_status_code() == 200

def test_single_ordered_book_record(apiToken):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiToken)
    orders.getting_order_id()

    orders.getting_single_ordered_book_record()
    assert orders.checking_status_code() == 200

def test_updating_ordered_book_record(apiToken):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiToken)
    orders.getting_order_id()

    orders.updating_ordered_book_record(customerName="Yotsuba")
    assert orders.checking_status_code() == 204

def test_delete_ordered_book_record(apiToken):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiToken)
    orders.getting_order_id()

    orders.deleting_ordered_book_entry()
    assert orders.checking_status_code() == 204