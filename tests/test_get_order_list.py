# ручка GET /api/v1/orders - получение списка заказов

import requests
import allure
from data import Endpoints


class TestGetOrdersList:

    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    @allure.description('Передаем ID заранее созданного курьера ручкой /api/v1/orders Код ответа 200, можно вывести')
    @allure.description('... список всех заказов, принятых данным курьером')
    def test_orders_list_returns_to_response_body(self):

        courier_id = 359430

        payload = {
            "firstName": "Platon",
            "lastName": "Tikhomirov",
            "address": "Nahabino",
            "metroStation": 4,
            "phone": "+7-906-083-7008",
            "rentTime": 5,
            "deliveryDate": "2024-08-06",
            "comment": "s.u.k.a"
        }

        response_create_order = requests.post(Endpoints.ADD_ORDER, data=payload)
        track_number = list(response_create_order.json().values())[0]
        print(track_number)

        url_get_order_details = f'{Endpoints.ORDERS_LIST}/track?t={track_number}'  # передаем трек-номер созданного заказа для получения id заказа
        response_get_details = requests.get(url_get_order_details)
        print(response_get_details.json())              # ЭТО ВЕРНЫЙ ЗАКАЗ

        order_id = response_get_details.json()['order']['id']
        print(order_id)   # ЭТО ID ЗАКАЗА

        url_accept_order = f'{Endpoints.ORDERS_LIST}/accept/{order_id}?courierId={courier_id}'
        response_give_order_to_courier = requests.put(url_accept_order)

        url_get_list_of_couriers_orders = f'{Endpoints.ORDERS_LIST}?courierId={courier_id}'
        response_get_list_of_couriers_orders = requests.get(url_get_list_of_couriers_orders)

        assert response_get_list_of_couriers_orders.status_code == 200
