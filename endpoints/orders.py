from .bases import BaseClass

class OrderEndpoint(BaseClass):
    
    _endpoint = "/orders/"

    def __init__(self):
        super().__init__(endpoint=self._endpoint)

    def setup_request_body(self, bookId, customerName):
        self._request_body["bookId"] = bookId
        self._request_body["customerName"] = customerName

    def setup_auth_headers(self, apiKey):
        self._auth_header["Authorization"] = apiKey

    def update_customer_name(self, customerName):
        self._customer_name["customerName"] = customerName

    def submitting_book_order(self):
        return self._send_post_requests()

    def getting_book_order_record(self, allOrder=False):
        if allOrder == False:
            return self._send_get_requests(auth=True)
        else:
            return self._send_get_requests(auth=True, orderId=True)
            
    def updating_ordered_book_record(self):
        return self._send_patch_requests()

    def deleting_ordered_book_entry(self):
        return self._send_delete_requests()


if __name__ == "__main__":
    pass