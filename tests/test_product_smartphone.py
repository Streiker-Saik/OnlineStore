import pytest

from src.product_lawngrass import LawnGrass
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


def test_smartphone_add_error(first_smartphone: Smartphone, first_grass: LawnGrass) -> None:
    """Тестирование операции сложения двух продуктов 'Смартфон', если добавленный не класс Smartphone"""
    with pytest.raises(TypeError) as exc_info:
        first_smartphone + first_grass
    assert "Переданный аргумент, не является классом Smartphone" in str(exc_info)
