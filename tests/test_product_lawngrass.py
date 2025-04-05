from src.product_lawngrass import LawnGrass


def test_grass_init(first_grass: LawnGrass) -> None:
    """Тестирование корректной инициализации класса LawnGrass"""
    assert first_grass.name == "Газонная трава"
    assert first_grass.description == "Элитная трава для газона"
    assert first_grass.price == 500.0
    assert first_grass.quantity == 20
    assert first_grass.country == "Россия"
    assert first_grass.germination_period == "7 дней"
    assert first_grass.color == "Зеленый"


def test_grass_add(first_grass: LawnGrass, second_grass: LawnGrass) -> None:
    """Тестирование операции сложения двух продуктов 'Трава газонна'"""
    sum_grass = first_grass + second_grass
    assert sum_grass == 16750.0


def test_created_product() -> None:
    """Тестирование на создание нового продукта"""
    product_one = {
        "name": "Газонная трава",
        "description": "Элитная трава для газона",
        "price": 500.0,
        "quantity": 20,
        "country": "Россия",
        "germination_period": "7 дней",
        "color": "Зеленый",
    }
    product = LawnGrass.created_product(product_one)
    assert product.name == "Газонная трава"
    assert product.description == "Элитная трава для газона"
    assert product.price == 500.0
    assert product.quantity == 20
    assert product.country == "Россия"
    assert product.germination_period == "7 дней"
    assert product.color == "Зеленый"
