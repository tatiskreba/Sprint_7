
import requests
import allure
from data import Url

class CourierMethods:
    @staticmethod
    @allure.step("Логин курьера с логином: {login}")
    def login_courier(login, password):
        response = requests.post(
            Url.url_login_courier,
            json={'login': login, 'password': password}
        )
        return response

    @staticmethod
    @allure.step("Создание курьера с телом запроса: {create_body}")
    def create_courier(create_body):
        return requests.post(
            Url.url_create_courier,
            json=create_body
        )

    @staticmethod
    @allure.step("Удаление курьера с ID: {courier_id}")
    def delete_courier(courier_id):
        return requests.delete(
            f"{Url.url_delete_courier}/{courier_id}"
        )
