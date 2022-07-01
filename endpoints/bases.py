import requests



class BaseClass:

    BASE_URL = "https://simple-books-api.glitch.me"

    def __init__(self):
        self.request = requests