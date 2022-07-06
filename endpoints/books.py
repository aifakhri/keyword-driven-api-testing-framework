from .bases import BaseClass


class BookEndpoint(BaseClass):
    
    _endpoint = "/books/"

    def __init__(self):
        super().__init__(endpoint=self._endpoint)
    
    def getting_book(self, bookId=""):
        if bookId == "":
            return self._send_get_requests()
        else:
            self._endpoint_url += str(bookId)
            return self._send_get_requests()

 
if __name__ == "__main__":
    pass