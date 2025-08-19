import pytest
from generators import generate_create_body_courier
from methods.courier_method import CourierMethods

@pytest.fixture
def create_and_delete_courier():
    courier_body = generate_create_body_courier()
    login = courier_body['login']
    password = courier_body['password']
    response_create = CourierMethods.create_courier(courier_body)
    courier_id = None
    if response_create.status_code == 201:
        login_courier = CourierMethods.login_courier(login, password)
        if login_courier.status_code == 200:
            courier_id = login_courier.json().get('id')
    yield login, password
    CourierMethods.delete_courier(courier_id)

@pytest.fixture
def delete_courier():
    created_credentials = []
    yield created_credentials
    for login, password in created_credentials:
        login_response = CourierMethods.login_courier(login, password)
        if login_response.status_code == 200:
            courier_id = login_response.json().get('id')
            if courier_id:
                CourierMethods.delete_courier(courier_id)
