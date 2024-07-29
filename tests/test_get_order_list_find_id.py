# ручка GET /api/v1/orders - получение списка заказов

import requests
import json
import allure
from conftest import create_courier_and_authorize
from test_create_order import TestOrderCreating
from data import Endpoints
import time


class TestGetOrdersList:

    def test_orders_list_returns_to_response_body(self):  # фикстура создания заказа?      , create_courier_and_authorize Ошибка так как не передается авторизованный и созданный курьер

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

        #json_string = json.dumps(payload)

        # СОЗДАЕМ ЗАКАЗ

        response_create_order = requests.post(Endpoints.ADD_ORDER, data=payload)
        track_number = list(response_create_order.json().values())[0]
        print(track_number)

        # ПОЛУЧАЕМ ID ЗАКАЗА ПО ТРЕК НОМЕРУ

        url_get_order_details = f'{Endpoints.ORDERS_LIST}/track?t={track_number}'  # передаем трек-номер созданного заказа для получения id заказа
        response_get_details = requests.get(url_get_order_details)
        print(response_get_details.json())              # ЭТО ВЕРНЫЙ ЗАКАЗ

        order_id = response_get_details.json()['order']['id']
        print(order_id)   # ЭТО ID ЗАКАЗА

        # ПЕРЕДАЕМ ЗАКАЗ СОЗДАННОМУ КУРЬЕРУ № 359430

        url_accept_order = f'{Endpoints.ORDERS_LIST}/accept/{order_id}?courierId={courier_id}'
        response_give_order_to_courier = requests.put(url_accept_order)
        print(response_give_order_to_courier.status_code)  # ЗАКАЗ ПЕРЕДАН КУРЬЕРУ НОМЕР 359430

        # ПОЛУЧАЕМ СПИСОК ЗАКАЗОВ КУРЬЕРА № 359430

        url_get_list_of_couriers_orders = f'{Endpoints.ORDERS_LIST}?courierId={courier_id}'
        response_get_list_of_couriers_orders = requests.get(url_get_list_of_couriers_orders)

        assert response_get_list_of_couriers_orders.status_code == 200

        # ПЕЧАТАЕМ СПИСОК ЗАКАЗОВ КУРЬЕРА 359430. НО НАШЕГО СГЕНЕРИРВОАННОГО ЗАКАЗА ТАМ НЕТ!

        print(response_get_list_of_couriers_orders.json())

        print()


        list_of_orders_json = response_get_list_of_couriers_orders.json()

        my_list = list_of_orders_json["orders"]

        for i in my_list:

            if list(i.values())[0] == order_id:

                print(i)
            else:
                print("ОТСУТСТВУЕТ")














      #  assert 327710 in list_of_orders_json['orders']

      #  order_track_number =



        print(list_of_orders_json["orders"][0]["id"])

        print(list_of_orders_json["orders"][0])

        print(order_id)

        print(list_of_orders_json["orders"][0]["id"]) ################ это. а тогда что order id?  order_id = response_get_details.json()['order']['id']

            # list_of_orders_json: = response_get_list_of_couriers_orders.json()                            # response_get_details: = requests.get(url_get_order_details)

            # А response_get_list_of_couriers_orders - это requests.get(url_get_list_of_couriers_orders)
        #
    # То есть list_of_orders_json - это requests.get(url_get_list_of_couriers_orders).json()
        #
        #

       # assert order_id in list_of_orders_json["orders"][0]

      #  assert order_id in list_of_orders_json["orders"]

        print(list_of_orders_json["orders"])

        print(list(list_of_orders_json["orders"]))



     #   print(list(list_of_orders_json["orders"].values()))



        print(order_id)

        print(my_list)

        print(list(my_list))






    #    a = list_of_orders_json["orders"]

     #   key = 'id'
     #   val = order_id    # order_id

        #b = next(filter(lambda b: b.get(key) == val, a), None)

        #b = next((b for b in a if b.get(key) == val), None)

     #   for i in a:
     #       if key in i:
    #            print(val)
    #        else:
    #            print("Не найден")

      #  print(b)

     #   print(val)

       # b = filter(lambda x: order_id, a)

        #c = dict(b)

        #print(c)


        #print(list(list_of_orders_json[0].values()))






     #   assert order_id in list_of_orders_json["orders"].values()





     #   assert str(order_id) in str(list_of_orders_json["orders"][0]["id"])


      #  assert order_track_number in list_of_orders_json['orders']






        #assert list_of_orders_json['orders'] in order_track_number
