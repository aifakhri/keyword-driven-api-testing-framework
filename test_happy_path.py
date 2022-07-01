from endpoints.books import BookEndpoint
from endpoints.orders import OrderEndpoint




def test_books_endpoint():
    books = BookEndpoint()
    assert books.send_http_get_request() == 200
    assert books.send_http_get_request(bookId=1) == 200


def test_orders_endpoint(apiKey):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiKey)
    orders.setup_request_body(bookId=1, customerName="Michael Scott")
    
    assert orders.send_post_requests().status_code == 201
    assert orders.send_get_requests().status_code == 200

    orders.update_customer_name("Dwight Schrute")

    assert orders.send_patch_request().status_code == 204
    assert orders.send_delete_request().status_code == 204
    