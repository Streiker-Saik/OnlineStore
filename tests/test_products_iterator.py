import pytest

from src.products_iterator import ProductsIterator


def test_init_products_iterator(products_iterator: ProductsIterator) -> None:
    """Тестирование корректной инициализации класса ProductIterator"""
    assert products_iterator.index == 0
    assert products_iterator.category.name == "Смартфоны"


def test_products_iterator(products_iterator: ProductsIterator) -> None:
    """Тестирование работы итератора"""
    assert next(products_iterator).name == "Samsung Galaxy C23 Ultra"
    assert next(products_iterator).name == "Iphone 15"
    assert products_iterator.index == 2


def test_products_iterator_stop(products_iterator: ProductsIterator) -> None:
    """Тестирование, что итератор не бесконечный"""
    next(products_iterator)
    next(products_iterator)
    with pytest.raises(StopIteration):
        next(products_iterator)
