from faker import Faker
fake = Faker()

def generate_body_order():

    return {
    "firstName": fake.first_name(),
    "lastName": fake.last_name(),
    "address": fake.address(),
    "metroStation": fake.random_int(min=1, max=20),
    "phone": fake.phone_number(),
    "rentTime": fake.random_int(min=1, max=10),
    "deliveryDate": fake.date_between(start_date="today", end_date="+10d").isoformat(),
    "comment": fake.sentence(nb_words=5),
    "color": []
    }

def generate_create_body_courier():

    return {
    "login": fake.user_name(),
    "password": fake.password(),
    "firstName": fake.first_name()
    }