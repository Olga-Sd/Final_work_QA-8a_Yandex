import DATA
import configuration
import requests


def post_new_order(body):
    """Функция создает заказ"""
    return requests.post(configuration.URL_SERVICES+configuration.API_CREATE_ORDER,
                         json = body,
                         headers = DATA.headers)


