from typing import Any

import pytest

from src.category import Category
from src.product import Product


def test_init_category(first_category: Category) -> None:
    """Тестирование корректной инициализации класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и получение " "дополнительных функций для удобства жизни"
    )
    assert first_category.category_count == 1
    assert first_category.product_count == 2


def test_category_product_setter(first_category: Category) -> None:
    """Тестирование на добавление продуктов в список у категории"""
    assert len(first_category.get_products) == 2
    first_category.add_product(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14))
    assert len(first_category.get_products) == 3


def test_category_product_setter_error(first_category: Category) -> None:
    """Тестирование добавление экземпляра в список продуктов не класс Product"""
    with pytest.raises(TypeError) as exc_info:
        error_category: Any = "Xiaomi Redmi Note 11"
        first_category.add_product(error_category)
    assert "Не является классом Product" in str(exc_info)


def test_category_products_list_property(first_category: Category) -> None:
    """Тестирование получение информации по списку продуктов"""
    assert first_category.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )


def test_product_str(first_category: Product) -> None:
    """Тестирование строкового отображения класса"""
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."
