from typing import List, Optional

from src.interfaces import BaseEntity
from src.product import Product


class Category(BaseEntity):
    """
    Класс категорий продукта

    Атрибуты:
        name(str): Название категории
        description(str): Описание категории
        products(List[Product]): Список продукта (private)
        category_count(int): Общее количество созданных категорий
        product_count(int): Общее количество продуктов во всех категориях

    Методы:
        __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
            Инициализирует экземпляр класса Category с заданными атрибутам
        __str__(self) -> str:
            Магический метод, возвращает строковое отображение класса Category.
            Формат: <name>, количество продуктов: <sum(product.quantity)> шт.
        get_products(self) -> List[Product]:
            Getter: возвращает список продуктов в категории
        add_product(self, product: Product) -> None:
            Метод: добавляет в категорию продукт и обновляет счетчик, если его нет в списке
        products(self) -> str:
            Getter: возвращает строку с информацией о продуктах о продуктах в категории. Формат:
            <name>, <price> руб. Остаток: <quantity> шт.
    """

    name: str
    description: str
    __products: List[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
        Метод для инициализации экземпляра категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов (по умолчанию пустой список)

        Увеличивает счетчик категорий при создании нового экземпляра
        и устанавливает количество продуктов в данной категории
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)
        super().__init__()

    def __str__(self) -> str:
        """
        Магический метод, строковое отображение класса.
        :return: Строка отображения класса. Формат:
        <name>, количество продуктов: <sum(product.quantity)> шт.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def get_products(self) -> List[Product]:
        """
        Getter выводит список продуктов
        :return: Список продуктов в категории
        """
        return self.__products

    def add_product(self, product: Product) -> None:
        """
        Метод добавляет в категорию продукт и обновляет счетчик, если его нет в списке
        :param product: Продукт который нужно добавить
        :raises TypeError: Если переданный аргумент не является экземпляром класса Product или подклассом.
        """
        if not isinstance(product, Product):
            raise TypeError("Не является классом Product или подклассом")

        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Getter выводит строку информации о продуктах
        :return: Строку с информацией о продуктах в категории. Формат:
            <name>, <price> руб. Остаток: <quantity> шт
        """
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str.strip()

    def middle_price(self):
        """"""
        pass
