from .bases import BaseClass


class BookEndpoint(BaseClass):
    
    _endpoint = "/books/"

    def __init__(self):
        super().__init__(endpoint=self._endpoint)
    
    def getting_single_book(self, bookId) -> str:
        self._endpoint_url += bookId
        return self._send_get_requests()
    
    def getting_multiple_books(self, type="", limit=""):
        if (type != "") and (limit == ""):
            self._endpoint_url += f"?type={type}"
        elif (type == "") and (limit != ""):
            self._endpoint_url += f"?limit={limit}"
        elif (type != "") and (type != ""):
            self._endpoint_url += f"?type={type}&limit={limit}"

        return self._send_get_requests()