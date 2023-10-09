import DATA
import configuration
import requests
import sender_stand_request

""" Cдвижкова Ольга, QA-8a. Дипломная работа, автотест"""

def test_can_get_order_by_track():
    """Тест проверяет возможность получить заказ по его треку"""
    response = sender_stand_request.post_new_order(DATA.new_order_body)
    order_track = response.json()['track']
    assert requests.get(configuration.URL_SERVICES+configuration.API_GET_ORDER_BY_TRACK +
                        str(order_track)).status_code == 200
