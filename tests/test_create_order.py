import pytest
import allure
from methods.order_method import OrderMethods
from helpers import modify_body_order

@allure.feature('API: Создание заказа')
@allure.story('Создание заказа на самокат')
class TestCreateOrder:

    @allure.title('Создание заказа с цветом BLACK')
    def test_create_order_with_black_color(self):
        order_body = modify_body_order('color', ['BLACK'])

        response = OrderMethods.create_order(order_body)
        allure.attach(str(response.json()), name="Response JSON",
                      attachment_type=allure.attachment_type.JSON)

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert 'track' in response.json(), "В ответе отсутствует поле 'track'"

    @allure.title('Создание заказа с цветом GREY')
    def test_create_order_with_grey_color(self):
        order_body = modify_body_order('color', ['GREY'])

        response = OrderMethods.create_order(order_body)
        allure.attach(str(response.json()), name="Response JSON",
                      attachment_type=allure.attachment_type.JSON)

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert 'track' in response.json(), "В ответе отсутствует поле 'track'"

    @allure.title('Создание заказа без указания цвета')
    def test_create_order_without_color(self):
        order_body = modify_body_order('color', [])

        response = OrderMethods.create_order(order_body)
        allure.attach(str(response.json()), name="Response JSON",
                      attachment_type=allure.attachment_type.JSON)

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert 'track' in response.json(), "В ответе отсутствует поле 'track'"

    @allure.title('Создание заказа с цветами BLACK и GREY')
    def test_create_order_with_black_and_grey_colors(self):
        order_body = modify_body_order('color', ['BLACK', 'GREY'])

        response = OrderMethods.create_order(order_body)
        allure.attach(str(response.json()), name="Response JSON",
                      attachment_type=allure.attachment_type.JSON)

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert 'track' in response.json(), "В ответе отсутствует поле 'track'"

