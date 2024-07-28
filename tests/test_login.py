# ручка POST /api/v1/courier/login - логин курьера в системе
import requests
import allure
import pytest
from conftest import generator
from conftest import create_user
from data import Endpoints
from data import FakeData


class TestLoginCourier:

    @allure.title('Курьер может авторизоватся')
    @allure.title('Успешный запрос возвращает id')
    @allure.description("Проверка того, что при передаче валидных данных курьер создастся и сервер вернет код 200")
    def test_courier_is_able_to_login(self, generator, create_user):

        login, password, firstName = generator

        data_login = {
            "login": login,
            "password": password
        }

        url = Endpoints.LOGIN
        response = requests.post(url, data_login)
        identifier = list(response.json().values())[0]

        print(identifier)
        print(response.json()['id'])
        assert response.status_code == 200
        assert identifier == response.json()['id']

    data_log = [
        [FakeData.get_sign_up_data()[1], ''],    # Преобразовали кортеж - выбрали данные по индексу из возвращенных данных метода get_sign_up_data() файла data
        ['', FakeData.get_sign_up_data()[1]]     # Без этого действия будет ошибка - AttributeError: 'tuple' object has no attribute

    ]

    @allure.title('Проверка того, что для авторизации нужно передать все обязательные поля, ')
    @allure.title('... а также того, что если одно из полей не заполнено, вернется ошибка ("недостаточно данных"')
    @allure.description("Для проверки отправляем два запроса: один без логина, другой - без пароля.")
    @allure.description("Реализована параметризация")
    @pytest.mark.parametrize("login, password", data_log)
    def test_error_returns_if_login_or_password_not_filled(self, generator, create_user, login, password):
        # login, password, firstName = generator - лишнеее, или он опять возьмет верные данные

        url = Endpoints.LOGIN
        login_response = requests.post(url, json={"login": login, "password": password})

        assert login_response.status_code == 400
        assert 'Недостаточно данных для входа' in login_response.text
        print(login_response.json())

    data_wrong = [
        [FakeData.get_sign_up_data()[0], 'набор_русских_букв_невалидная_длина_и_тип_символов'],
        ['999999999999999999999999999999_невалидный_логин', FakeData.get_sign_up_data()[1]],
        [FakeData.get_sign_up_data()[0], 'nonexistent'],
        ['nonexistent', FakeData.get_sign_up_data()[1]]
    ]

    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль, ')
    @allure.title('... а также что если авторизоваться под несуществующим пользователем, запрос тоже вернет ошибку')
    @allure.description("Отправляем два запроса. С существующим логином и несуществующим паролем, и наоборот.")
    @allure.description("Несуществующие логин и пароль названы nonexistent")
    @pytest.mark.parametrize("login, password", data_wrong)
    def test_error_returns_if_incorrect_login_or_password_sent(self, generator, create_user, login, password):

        url = Endpoints.LOGIN
        response = requests.post(url, json={"login": login, "password": password})

        assert response.status_code == 404
        print(response.json())
