import allure
from methods.order_method import OrderMethods

@allure.feature('API: Заказы')
@allure.story('Получение списка заказов')
class TestGetOrdersList:

    @allure.title('Получение списка всех заказов')
    @allure.description(
        'Проверяем, что endpoint возвращает список всех заказов с кодом 200. '
        'Ответ должен содержать поле "orders", которое является массивом.'
    )
    def test_get_orders_list(self):
        with allure.step('Отправляем GET-запрос для получения списка всех заказов'):
            response = OrderMethods.get_orders_list()

        with allure.step('Логируем тело ответа для отчёта'):
            allure.attach(
                str(response.json()),
                name="Response JSON",
                attachment_type=allure.attachment_type.JSON
            )

        with allure.step('Проверяем корректность ответа'):
            assert response.status_code == 200, "Ожидался статус-код 200"
            assert 'orders' in response.json(), "В ответе нет ключа 'orders'"
            assert isinstance(response.json()['orders'], list), "Поле 'orders' должно быть списком"
