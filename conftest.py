import pytest
import allure
import json
from data import FakeData
import requests
import random
import string


from data import FakeData


@pytest.fixture
def generator():

    login, password, firstName = FakeData.get_sign_up_data()  # генерация данных
    return login, password, firstName

@pytest.fixture
def create_user(generator):   # мб заменить это на метод

    login, password, firstName = generator

    url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'

    data = {
        "login": login,
        "password": password,
        "firstName": firstName
    }

    response = requests.post(url, data)

    return response

@pytest.fixture
def create_courier_and_authorize():

    @allure.title('метод регистрации нового курьера возвращает список из логина и пароля (из задания')
    @allure.description('если регистрация не удалась, возвращает пустой список')
    #@staticmethod
    def register_new_courier_and_return_login_password():    # попробовать убрать self
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
     #   yield login_pass

        return login_pass

         #   return login, password, first_name





