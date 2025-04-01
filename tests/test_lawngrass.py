from src.lawngrass import LawnGrass


def test_smartphone_init(first_grass: LawnGrass) -> None:
    """Тестирование корректной инициализации класса LawnGrass"""
    assert first_grass.name == "Газонная трава"
    assert first_grass.description == "Элитная трава для газона"
    assert first_grass.price == 500.0
    assert first_grass.quantity == 20
    assert first_grass.country == "Россия"
    assert first_grass.germination_period == "7 дней"
    assert first_grass.color == "Зеленый"