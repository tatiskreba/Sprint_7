import pytest
import allure
from methods.order_method import OrderMethods
from helpers import modify_body_order
from generators import generate_body_order

@allure.feature('API: Создание заказа')
@allure.story('Создание заказа на самокат')
class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @allure.description(
        'Проверяем, что заказ можно создать с цветом BLACK, GREY, с обоими цветами или без цвета. '
        'Успешный запрос возвращает статус 201 и номер заказа (track).'
    )
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], [], ['BLACK', 'GREY']])
    def test_create_order_with_different_color_combinations(self, color):
        color_desc = ', '.join(color) if color else 'не указан'
        with allure.step(f'Формируем тело заказа с цветом: {color_desc}'):
            order_body = modify_body_order('color', color)

        with allure.step('Отправляем запрос на создание заказа'):
            response = OrderMethods.create_order(order_body)

        with allure.step('Логируем тело ответа для Allure'):
            allure.attach(
                str(response.json()),
                name="Response JSON",
                attachment_type=allure.attachment_type.JSON
            )

        with allure.step('Проверяем, что сервер вернул статус 201 (Created)'):
            assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"

        with allure.step('Проверяем, что в ответе есть номер заказа (track)'):
            assert 'track' in response.json(), "В ответе отсутствует поле 'track'"
