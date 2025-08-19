from generators import generate_body_order
import copy

def modify_body_order(key, value):
    """Возвращает тело заказа с изменённым полем key."""
    body = copy.deepcopy(generate_body_order())
    body[key] = value
    return body
