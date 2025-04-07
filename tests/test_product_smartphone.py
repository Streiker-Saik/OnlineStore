from src.product_smartphone import Smartphone


def test_smartphone_init(first_smartphone: Smartphone) -> None:
    """Тестирование корректной инициализации класса Smartphone"""
    assert first_smartphone.name == "Samsung Galaxy C23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_smartphone_add(first_smartphone: Smartphone, second_smartphone: Smartphone) -> None:
    """Тестирование операции сложения двух смартфонов"""
    sum_smartphone = first_smartphone + second_smartphone
    assert sum_smartphone == 2580000.0


def test_created_product() -> None:
    """Тестирование на создание нового продукта"""
    product_one = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "efficiency": 95.5,
        "model": "S23 Ultra",
        "memory": 256,
        "color": "Серый",
    }
    product = Smartphone.created_product(product_one)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert product.efficiency == 95.5
    assert product.model == "S23 Ultra"
    assert product.memory == 256
    assert product.color == "Серый"
