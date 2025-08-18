import pytest
import allure
from methods.courier_method import CourierMethods

@allure.feature('API: Авторизация курьера')
class TestAuthCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверяем, что зарегистрированный курьер может успешно авторизоваться и получить id')
    def test_success_auth_courier(self, create_and_delete_courier):
        login, password = create_and_delete_courier
        with allure.step('Отправляем запрос на логин с валидными данными'):
            auth_response = CourierMethods.login_courier(login, password)
        with allure.step('Проверяем, что сервер возвращает статус 200 и в теле ответа есть id курьера'):
            assert auth_response.status_code == 200
            assert 'id' in auth_response.json()
        with allure.step('Проверяем, что значение поля "id" — число'):
            assert isinstance(auth_response.json()['id'], int)

    @allure.title('Ошибка при входе с пустым логином')
    @allure.description('Проверяем, что нельзя авторизоваться без логина')
    def test_failure_auth_courier_empty_login(self, create_and_delete_courier):
        _, password = create_and_delete_courier
        with allure.step('Отправляем запрос с пустым логином'):
            response = CourierMethods.login_courier('', password)

        with allure.step('Ожидаем статус 400 и сообщение об ошибке'):
            assert response.status_code == 400
            assert 'message' in response.json()
            assert 'Недостаточно данных для входа' in response.json()['message']

    @allure.title('Ошибка при входе с пустым паролем')
    @allure.description('Проверяем, что нельзя авторизоваться без пароля')
    def test_failure_auth_courier_empty_password(self, create_and_delete_courier):
        login, _ = create_and_delete_courier
        with allure.step('Отправляем запрос с пустым паролем'):
            response = CourierMethods.login_courier(login, '')

        with allure.step('Ожидаем статус 400 и сообщение об ошибке'):
            assert response.status_code == 400
            assert 'message' in response.json()
            assert 'Недостаточно данных для входа' in response.json()['message']

    @allure.title('Ошибка при входе с неверным логином')
    @allure.description('Проверяем, что нельзя авторизоваться с несуществующим логином')
    def test_failure_auth_courier_invalid_login(self, create_and_delete_courier):
        _, password = create_and_delete_courier
        with allure.step('Отправляем запрос с неверным логином'):
            response = CourierMethods.login_courier('none_login', password)

        with allure.step('Ожидаем статус 404 и сообщение об ошибке'):
            assert response.status_code == 404
            assert 'message' in response.json()
            assert 'Учетная запись не найдена' in response.json()['message']

    @allure.title('Ошибка при входе с неверным паролем')
    @allure.description('Проверяем, что нельзя авторизоваться с неправильным паролем')
    def test_failure_auth_courier_invalid_password(self, create_and_delete_courier):
        login, _ = create_and_delete_courier
        with allure.step('Отправляем запрос с неверным паролем'):
            response = CourierMethods.login_courier(login, 'none_pass')

        with allure.step('Ожидаем статус 404 и сообщение об ошибке'):
            assert response.status_code == 404
            assert 'message' in response.json()
            assert 'Учетная запись не найдена' in response.json()['message']

