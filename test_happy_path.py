from endpoints.books import BookEndpoint
from endpoints.orders import OrderEndpoint




def test_books_endpoint():
    books = BookEndpoint()
    books.getting_book()
    assert books.checking_status_code() == 200

    books.getting_book(bookId="1")
    assert books.checking_status_code() == 200

def test_orders_endpoint(apiKey):
    orders = OrderEndpoint()
    orders.setup_auth_headers(apiKey)
    orders.setup_request_body(bookId=1, customerName="Michael Scott")
    
    orders.submitting_book_order()
    assert orders.checking_status_code() == 201

    orders.getting_book_order_record()
    assert orders.checking_status_code() == 200

    orders.getting_book_order_record(allOrder=True)
    assert orders.checking_status_code() == 200
    
    orders.update_customer_name("Dwight Schrute")
    orders.updating_ordered_book_record()
    assert orders.checking_status_code() == 204

    orders.deleting_ordered_book_entry()
    assert orders.checking_status_code() == 204
