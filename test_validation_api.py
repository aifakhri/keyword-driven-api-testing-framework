from endpoints.books import BookEndpoint
from endpoints.orders import OrderEndpoint
from endpoints.apiClient import ApiClient



def test_multiple_books_endpoint():
    books = BookEndpoint()
    books.getting_multiple_books()
    assert books.checking_status_code() == 201

def test_single_books_endpoint():
    books = BookEndpoint()
    books.getting_single_book(bookId="1")
    assert books.checking_status_code() == 200

def test_submitting_book_order(apiKey):
    orders = OrderEndpoint()
    orders.setup_request_body(bookId="1", customerName="Michael Scott")
    orders.setup_auth_headers(apiKey)

    orders.submitting_book_order()
    assert orders.checking_status_code() == 201

def test_multiple_ordered_books_record(apiKey):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiKey)
    
    orders.getting_all_ordered_books_record()
    assert orders.checking_status_code() == 200

def test_single_ordered_book_record(apiKey):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiKey)
    orders.getting_order_id()

    orders.getting_single_ordered_book_record()
    assert orders.checking_status_code() == 200

def test_updating_ordered_book_record(apiKey):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiKey)
    orders.update_customer_name(customerName="Dwight Schrute")
    orders.getting_order_id()

    orders.updating_ordered_book_record()
    assert orders.checking_status_code() == 204

def test_delete_ordered_book_record(apiKey):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiKey)
    orders.getting_order_id()

    orders.deleting_ordered_book_entry()
    assert orders.checking_status_code() == 204

def test_api_client_endpoint():
    api_client = ApiClient()
    api_client.setup_api_client_detail(name="test", email="test@something.com")
    api_client.register_api_client()

    assert api_client.checking_status_code() == 201