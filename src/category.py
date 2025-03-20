from typing import Optional, List

from src.product import Product


class Category:
    """
    Класс категорий продукта
    Атрибуты:
        name(str): Название категории
        description(str): Описание категории
        products(List[Product]): Список продукта
        category_count(int): Общее количество созданных категорий
        product_count(int): Общее количество созданных продукта
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
        Category.product_count = len(self.__products) if self.__products else 0

    @property
    def products(self) -> List[Product]:
        """Возвращает список продуктов в категории"""
        return self.__products

    def add_product(self, product: Product) -> None:
        """
        Метод добавляет в категорию продукт и обновляет счетчик
        :param product: Продукт который нужно добавить
        """
        self.__products.append(product)
        Category.product_count += 1
