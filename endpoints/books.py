from requests import request
from .bases import BaseClass


class BookEndpoint(BaseClass):
    
    __endpoint = "/books/"

    def send_http_get_request(self, bookId=None):
        if bookId != None:
            endpoint_url = self.BASE_URL + self.__endpoint
            return self.request.get(endpoint_url)
        else:
            endpoint_url = self.BASE_URL + self.__endpoint + bookId
            return self.request.get(endpoint_url)