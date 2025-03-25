from typing import List, Optional

from src.product import Product


class Category:
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
        :raises TypeError: Если переданный аргумент не является экземпляром класса Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Не является классом Product")

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
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str.strip()
