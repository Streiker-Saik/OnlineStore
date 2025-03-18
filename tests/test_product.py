from src.product import Product


def test_init_product(first_product: Product) -> None:
    """Тестирование корректной инициализации класса Product"""
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5
