import pytest
import allure
from generators import generate_create_body_courier
from methods.courier_method import CourierMethods

@allure.feature('API: Курьер')
@allure.story('Создание курьера')
class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_success_create_courier(self, delete_courier):
        courier_body = generate_create_body_courier()
        login, password = courier_body['login'], courier_body['password']

        with allure.step('Отправляем запрос на создание курьера'):
            response = CourierMethods.create_courier(courier_body)
            allure.attach(str(response.json()), name="Response JSON", attachment_type=allure.attachment_type.JSON)

        with allure.step('Проверяем успешный ответ'):
            assert response.status_code == 201
            assert response.json() == {'ok': True}

        delete_courier.append((login, password))

    @allure.title('Нельзя создать курьера с дублирующимся логином')
    def test_duplicate_courier_failed(self, delete_courier):
        courier_body = generate_create_body_courier()
        login, password = courier_body['login'], courier_body['password']

        # Создаём первого курьера
        first_response = CourierMethods.create_courier(courier_body)
        allure.attach(str(first_response.json()), name="First Response JSON", attachment_type=allure.attachment_type.JSON)
        assert first_response.status_code == 201
        delete_courier.append((login, password))

        # Пытаемся создать курьера с тем же логином
        second_response = CourierMethods.create_courier(courier_body)
        allure.attach(str(second_response.json()), name="Second Response JSON", attachment_type=allure.attachment_type.JSON)
        assert second_response.status_code == 409
        assert 'message' in second_response.json()
        assert 'Этот логин уже используется' in second_response.json()['message']

    @allure.title('Ошибка при создании курьера без логина')
    def test_create_courier_empty_login_failed(self):
        courier_body = generate_create_body_courier()
        del courier_body['login']

        response = CourierMethods.create_courier(courier_body)
        allure.attach(str(response.json()), name="Response JSON", attachment_type=allure.attachment_type.JSON)
        assert response.status_code == 400
        assert 'message' in response.json()
        assert 'Недостаточно данных для создания учетной записи' in response.json()['message']

    @allure.title('Ошибка при создании курьера без пароля')
    def test_create_courier_empty_password_failed(self):
        courier_body = generate_create_body_courier()
        del courier_body['password']

        response = CourierMethods.create_courier(courier_body)
        allure.attach(str(response.json()), name="Response JSON", attachment_type=allure.attachment_type.JSON)
        assert response.status_code == 400
        assert 'message' in response.json()
        assert 'Недостаточно данных для создания учетной записи' in response.json()['message']
