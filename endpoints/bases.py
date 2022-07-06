import requests
from abc import ABC


class BaseClass(ABC):

    _BASE_URL = "https://simple-books-api.glitch.me"

    def __init__(self, endpoint):
        self._endpoint_url = self._BASE_URL + endpoint
        self._response = object()
        self._auth_header = {}
        self._request_body = {}
        self._customer_name = {}
        self._orderId = ""

    def _send_get_requests(self, auth=False, orderId=False):
        if auth == False:
            self._response = requests.get(self._endpoint_url)
            return self._response
        else:
            if orderId == False:
                self._endpoint_url += self._orderId
            
            self._response = requests.get(self._endpoint_url, headers=self._auth_header)
            return self._response

    def _send_post_requests(self):
        self._response = requests.post(
            url=self._endpoint_url,
            json=self._request_body,
            headers=self._auth_header
        )
        self._orderId = self._response.json()["orderId"]
        return self._response 

    def _send_patch_requests(self):
        self._response = requests.patch(
            url=self._endpoint_url,
            json=self._customer_name,
            headers=self._auth_header
        )
        return self._response

    def _send_delete_requests(self):
        self._response = requests.delete(
            url=self._endpoint_url,
            headers=self._auth_header
        )
        return self._response

    def checking_status_code(self):
        return self._response.status_code