from typing import Any, Type

import pytest

from src.exceptions import ZeroQuantityError
from src.order import Order
from src.product import Product


def test_order_init(test_order: Order) -> None:
    """Тестирование корректной инициализации класса Order"""
    assert test_order.product.name == "Samsung Galaxy C23 Ultra"
    assert test_order.quantity == 2
    assert test_order.total_price == 360000.0


def test_order_str(test_order: Order) -> None:
    """Тестирование строкового отображения класса"""
    assert str(test_order) == "Samsung Galaxy C23 Ultra, 2 шт: 360000.0 руб"


def test_order_update_quantity(test_order: Order) -> None:
    """Тестирование изменение количества"""
    assert test_order.quantity == 2
    test_order.update_quantity(1)
    assert test_order.quantity == 1
    assert test_order.total_price == 180000.0


@pytest.mark.parametrize(
    "new_quantity, expected, exc_message",
    [
        ("a", TypeError, "Переданный аргумент не является целым числом"),
        (-1, ValueError, "Количество не может быть меньше 0"),
    ],
)
def test_order_update_quantity_error(
    test_order: Order, new_quantity: Any, expected: Type[Exception], exc_message: str
) -> None:
    """Тестирование изменение количества, ошибкой аргумента"""
    with pytest.raises(expected) as exc_info:
        test_order.update_quantity(new_quantity)
    assert exc_message in str(exc_info.value)


def test_orders_init_error(invalid_product: Product) -> None:
    """Тестирование при создании заказа с продуктом количество которое равно 0"""
    with pytest.raises(ZeroQuantityError) as exc_info:
        Order(invalid_product, 5)
    assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)
