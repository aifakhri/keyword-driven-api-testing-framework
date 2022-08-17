import pytest
from endpoints.books import BookEndpoint



@pytest.mark.parametrize("bookId", [
    "someString",
])
def test_book_endpoint_path_attribute(bookId):
    book = BookEndpoint()
    book.getting_single_book(bookId=bookId)
    
    assert book.checking_status_code() == 404


@pytest.mark.parametrize("type, limit", [
    ("sport", ""),
    ("", "21"),
    ("sport", "100"),
])
def test_book_endpoint_query_param(type, limit):
    book = BookEndpoint()
    book.getting_multiple_books(type=type, limit=limit)
    
    assert book.checking_status_code() == 400