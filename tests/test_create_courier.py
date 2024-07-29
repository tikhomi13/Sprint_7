# ручка POST /api/v1/courier - Создание курьера

import requests
import allure
import pytest

from conftest import generator
from conftest import create_user

from data import Endpoints
from data import FakeData


class TestCreateCourier:

    @allure.title('Проверка возможности создания курьера, возврата верного кода ответа - 201, а также ')
    @allure.title('...возврата валидного тела ответа - {"ok":true}')
    @allure.description("Для проверки успешного запроса генерируем два набора данных - логин, пароль, имя")
    def test_able_to_create_courier(self, generator):

        login, password, firstName = generator
        url = Endpoints.ADD_COURIER
        data = {
            "login": login,
            "password": password,
            "firstName": firstName
        }

        response = requests.post(url, data)

        assert 201 == response.status_code     # Код ответа
        assert '{"ok":true}' == response.text  # Тело ответа
        assert 'Created' == response.reason    # статус ответа

        print(response.status_code)
        print(response.text)

    @allure.title('Проверка на невозможность создания двух курьеров с одинаковыми данными, ')
    @allure.title('... и, соответственно, что при создании курьеров с одинаковыми логинами сервер возвращает ошибку')
    @allure.title('Приведены код, статус и тело ответа')
    def test_unable_to_create_two_same_couriers(self):

        url = Endpoints.ADD_COURIER
        data = {
            "login": 'SameCourier',
            "password": '1234',
            "firstName": "Konstantin_Shvets"
        }

        response_201 = requests.post(url, data)
        response_409 = requests.post(url, data)

        assert 409 == response_409.status_code                      # Код ответа
        assert 'Conflict' == response_409.reason                    # Статус ответа
        assert 'Этот логин уже используется' in response_409.text   # Текст ответа

        print(response_409.json())

    data_reg = [
        [FakeData.get_sign_up_data()[0], ''],
        ['', FakeData.get_sign_up_data()[1]]

    ]

    @allure.title('Проверка того, что для регистрации курьера нужно передать обязательные поля - логин и пароль, ')
    @allure.title('... а также того, что если одно из полей не заполнено, запрос возвращает ошибку')
    @allure.description("Отправляем два запроса: один без логина, другой - без пароля.")
    @pytest.mark.parametrize("login, password", data_reg)
    def test_unable_to_create_courier_with_unfilled_necessary_fields(self, generator, create_user, login, password):

        url = Endpoints.ADD_COURIER
        login_response = requests.post(url, json={"login": login, "password": password})

        assert login_response.status_code == 400
        print(login_response.json())
