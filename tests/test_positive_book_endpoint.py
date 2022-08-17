import pytest
from endpoints.books import BookEndpoint



def test_multiple_books_endpoint():
    books = BookEndpoint()
    books.getting_multiple_books()
    assert books.checking_status_code() == 200


@pytest.mark.parametrize("bookId", [
    "1", "2", "3", "4", "5", "6"
])
def test_single_books_endpoint(bookId):
    books = BookEndpoint()
    books.getting_single_book(bookId=bookId)
    assert books.checking_status_code() == 200


@pytest.mark.parametrize("type, limit", [
    ("fiction", ""), ("non-fiction", ""), ("", "3"), ("fiction", "2"), ("non-fiction", "2")
])
def test_filtering_books(type, limit):
    books = BookEndpoint()
    books.getting_multiple_books(type=type, limit=limit)
    assert books.checking_status_code() == 200