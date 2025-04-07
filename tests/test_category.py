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
    assert "Не является классом Product или подклассом" in str(exc_info)


def test_category_products_list_property(first_category: Category) -> None:
    """Тестирование получение информации по списку продуктов"""
    assert first_category.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )


def test_category_str(first_category: Category) -> None:
    """Тестирование строкового отображения класса"""
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_category_middle_price(first_category: Category) -> None:
    """Тестирование подсчитывания средних цен всех товаров в категории"""
    assert first_category.middle_price() == 195000


def test_category_middle_price_empty_products() -> None:
    """Тестирование подсчитывания средних цен всех товаров в категории, при отсутствии товаров"""
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [],
    )
    assert category.middle_price() == 0


def test_category_add_product_invalid(
    capsys: pytest.CaptureFixture, first_category: Category, invalid_product: Product
) -> None:
    """тестирование, добавление продукта с нулевым количеством"""
    first_category.add_product(invalid_product)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар с нулевым количеством не может быть добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
