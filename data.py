import faker
import requests
import allure
import random
import string


class FakeData:

    @allure.description('Метод генерации данных с использованием модуля Faker')
    @staticmethod
    def get_sign_up_data():  # выделить в класс
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        firstName = generate_random_string(10)

        return login, password, firstName

        #fake = faker.Faker()
        #login = fake.text(max_nb_chars=10)
        #password = fake.password(4, False, True, False, True)
        #firstName = fake.text(max_nb_chars=10)
        # return login, password, firstName

@allure.title('URL и ручки')
class Endpoints:

    ADD_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier' # URL добавления курьера. Метод POST

    LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login' # URL логина курьера. Метод POST

    ADD_ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders' # URL добавления заказа. Метод POST

    ORDERS_LIST = 'https://qa-scooter.praktikum-services.ru/api/v1/orders' # URL получения списка заказов. Метод GET
