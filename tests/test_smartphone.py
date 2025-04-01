from src.smartphone import Smartphone


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