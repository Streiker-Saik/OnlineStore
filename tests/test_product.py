from typing import Any, List
from unittest.mock import MagicMock, patch

import pytest

from src.product import Product
from src.product_lawngrass import LawnGrass
from src.product_smartphone import Smartphone


def test_init_product(first_product: Product) -> None:
    """Тестирование корректной инициализации класса Product"""
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_new_product() -> None:
    """Тестирование на создание нового продукта"""
    product_one = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
    product = Product.new_product(product_one)
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_new_product_in_existing_products() -> None:
    """Тестирование на создание нового продукта, c проверкой и изменением в списке созданных"""
    product_one = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
    product_two = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 45000.0, "quantity": 6}
    product_free = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
    existing_products: List = []

    product = Product.new_product(product_one, existing_products)
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14
    assert len(existing_products) == 1

    product = Product.new_product(product_two, existing_products)
    assert product.price == 45000.0
    assert product.quantity == 20
    assert len(existing_products) == 1

    product = Product.new_product(product_free, existing_products)
    assert product.price == 210000.0
    assert product.quantity == 8
    assert len(existing_products) == 2


def test_product_update(capsys: pytest.CaptureFixture, first_product: Product) -> None:
    """Тестирование на ввод корректной цены больше 0"""
    first_product.price = -100.5
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


@patch("builtins.input")
def test_product_correct(mock_input: MagicMock, first_product: Product) -> None:
    """Тестирование на наличие предупреждения при уменьшении цены"""
    assert first_product.price == 180000.0
    mock_input.return_value = "n"
    first_product.price = 120000.0
    assert first_product.price == 180000.0
    mock_input.return_value = "y"
    first_product.price = 120000.0
    assert first_product.price == 120000.0


def test_product_str(first_product: Product) -> None:
    """Тестирование строкового отображения класса"""
    assert str(first_product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(first_product: Product, second_product: Product) -> None:
    """Тестирование операции сложения двух продуктов"""
    sum_product = first_product + second_product
    assert sum_product == 2580000.0


def test_product_add_error(first_product: Product) -> None:
    """Тестирование операции сложения двух продуктов, если добавленный не класс Product"""
    with pytest.raises(TypeError) as exc_info:
        error_category: Any = "Any"
        first_product + error_category
    assert "Не возможно сложить разные классы/подклассы" in str(exc_info)


def test_smartphone_add_error(first_smartphone: Smartphone, first_grass: LawnGrass) -> None:
    """Тестирование операции сложения двух подклассов 'Смартфон', если добавленный не класс Smartphone"""
    with pytest.raises(TypeError) as exc_info:
        first_smartphone + first_grass
    assert "Не возможно сложить разные классы/подклассы" in str(exc_info)
