# ручка POST /api/v1/orders - создание заказа - 4 теста

import requests
import json
import allure
import pytest
from data import Endpoints


class TestOrderCreating:

    colors = [

        [
            ["BLACK"]
        ],

        [
            ["GREY"]
        ],

        [
            ["BLACK", 'GRAY'],
        ],

        [
            [""]
        ]

    ]

    @allure.title("Можно выбрать черный или серый самокат, либо выбрать оба цвета, либо не выбирать никакой")
    @allure.title("Ответ содержит трек-номер заказа")
    @allure.description("С помощью параметризации передаем в payload цвет(а) самоката или запрос без цвета")
    @allure.description("Трек-номер заказа вынесен в переменную track")
    @allure.description("В строке № 53 выполнена сериализация словаря payload, чтобы данные ушли на серв. в форм. JSON")
    @pytest.mark.parametrize("color", colors)
    def test_able_to_choose_one_from_two_colors_while_creating_order(self, color):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }

        json_string = json.dumps(payload)
        response = requests.post(Endpoints.ADD_ORDER, data=json_string)

        track = list(response.json().values())[0]
        print(response.json())

        assert response.status_code == 201
        assert track in response.json().values()
