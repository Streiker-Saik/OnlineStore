import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


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


def test_grass_add_error(first_grass: LawnGrass, first_smartphone: Smartphone) -> None:
    """Тестирование операции сложения двух продуктов 'Трава газонна', если добавленный не класс LawnGrass"""
    with pytest.raises(TypeError) as exc_info:
        first_grass + first_smartphone
    assert "Переданный аргумент, не является классом LawnGrass" in str(exc_info)
