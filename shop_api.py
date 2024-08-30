import requests

import urls


class ShopApi:
    @staticmethod
    def registration(body):
        return requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=body)

    @staticmethod
    def login(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, data=body)


