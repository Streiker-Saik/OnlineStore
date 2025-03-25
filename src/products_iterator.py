from typing import Iterator

from src.category import Category
from src.product import Product


class ProductsIterator:
    """
    Итератор класса Category, позволяющий перебирать продукты в категории

    Атрибуты:
        category_obj(Category) - объект класса Category,
    Методы:
        __init__(self, category_obj: Category) -> None:
            Инициализирует объект класса Category
        __iter__(self) -> Iterator:
            Возвращает сам итератор
        __next__(self) -> Product:
            Возвращает следующий продукт в категории
    """

    category_obj: Category

    def __init__(self, category_obj: Category) -> None:
        """
        Метод для инициализации итератора
        :param category_obj: объект класса Category
        """
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> Iterator:
        """
        Возвращает сам итератор.
        :return: Возвращает объект итератора
        """
        self.index = 0
        return self

    def __next__(self) -> Product:
        """
        Возвращает следующий продукт в категории
        :return: Экземпляр класса Product
        :raises StopIteration: Если продукты в категории закончились
        """
        if self.index < len(self.category.get_products):
            product = self.category.get_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
