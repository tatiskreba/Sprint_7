import requests
import allure
from data import Url

class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа с телом: {body}")
    def create_order(body):
        return requests.post(Url.url_orders, json=body)

    @staticmethod
    @allure.step("Получение списка всех заказов")
    def get_orders_list():
        return requests.get(Url.url_orders)
