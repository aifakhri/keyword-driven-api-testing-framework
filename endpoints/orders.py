from .bases import BaseClass

class OrderEndpoint(BaseClass):
    
    __endpoint = "/orders/"
    __request_body = {}
    __auth_header = {}
    __customer_name = {}
    __orderId = ""


    def setup_request_body(self, bookId, customerName):
        self.__request_body["bookId"] = bookId
        self.__request_body["customerName"] = customerName

    def setup_auth_headers(self, apiKey):
        self.__auth_header["Authorization"] = apiKey

    def update_customer_name(self, customerName):
        self.__customer_name["customerName"] = customerName

    def send_get_requests(self, orderId=False):
        if orderId == False:
            return self.request.get(
                url=self.BASE_URL+self.__endpoint,
                headers=self.__auth_header
            )
        else:
            return self.request.get(
                url=self.BASE_URL+self.__endpoint+self.__orderId,
                headers=self.__auth_header
            )

    def send_post_requests(self):
        response = self.request.post(
            url=self.BASE_URL+self.__endpoint,
            json=self.__request_body,
            headers=self.__auth_header
        )
        self.__orderId = response.json()["orderId"]
        return response

    def send_patch_request(self):
        return self.request.patch(
            url=self.BASE_URL+self.__endpoint+self.__orderId,
            json=self.__customer_name,
            headers=self.__auth_header
        )

    def send_delete_request(self):
        return self.request.delete(
            url=self.BASE_URL+self.__endpoint+self.__orderId,
            headers=self.__auth_header
        )