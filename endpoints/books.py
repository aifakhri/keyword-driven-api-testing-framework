from .bases import BaseClass


class BookEndpoint(BaseClass):
    
    _endpoint = "/books/"

    def __init__(self):
        super().__init__(endpoint=self._endpoint)
    
    def getting_single_book(self, bookId) -> str:
        self._endpoint_url += bookId
        return self._send_get_requests()
    
    def getting_multiple_books(self):
        return self._send_get_requests()

 
if __name__ == "__main__":
    pass