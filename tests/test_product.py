from src.product import Product


def test_init_product(first_product: Product) -> None:
    """Тестирование корректной инициализации класса Product"""
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_new_product() -> None:
    """Тестирование на создание нового продукта, а при существовании в списке продуктов обновление"""
    product_one = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
    existing_products = []
    product = Product.new_product(product_one, existing_products)
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14
    assert len(existing_products) == 1

    product_two = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 45000.0, "quantity": 6}
    product = Product.new_product(product_two, existing_products)
    assert product.price == 45000.0
    assert product.quantity == 20
    assert len(existing_products) == 1

    product_free = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
    product = Product.new_product(product_free, existing_products)
    assert product.price == 210000.0
    assert product.quantity == 8
    assert len(existing_products) == 2
