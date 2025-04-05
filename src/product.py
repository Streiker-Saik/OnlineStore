from typing import Any, Dict, List, Optional

from src.interfaces import BaseProduct
from src.mixins import PrintMixin


class Product(BaseProduct, PrintMixin):
    """
    Класс для предоставления продукта

    Атрибуты:
        name(str): Название продукта
        description(str): Описание продукта
        price(float): Цена продукта (private)
        quantity(int): Количество продукта

    Методы:
        __init__(self, name: str, description: str, price: float, quantity: int) -> None:
            Инициализирует экземпляр класса Product с заданными атрибутам
        new_product(cls, product: Dict[str, Any], existing_products: Optional[List['Product']] -> 'Product':
            Создает новый экземпляр класса Product на основе данных из словаря.
            Если такой продукт с name существует в списке, обновляет количество и цену
        price(self) -> float:
            Getter: возвращает значение цены
        price(self, new_price: float) -> None:
            Setter: заменяет значение цены.
            При меньше или равное 0 выводит сообщение предупреждения.
            При уменьшении цены запрашивает у пользователя подтверждение
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Метод для инициализации экземпляра продукта
        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество продукта
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """
        Магический метод, строковое отображение класса.
        :return: Строка отображения класса. Формат:
        <name>, <price> руб. Остаток: <quantity> шт.
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Суммирование двух продуктов общей стоимости товаров
        :param other: экземпляр класса Product, который будет добавлен
        :return: общая стоимость товаров, как сумма стоимости товаров умноженная на их количество
        :raises TypeError: Если переданный аргумент не является тем же классы/подклассы.
        """
        if type(other) is not self.__class__:
            raise TypeError("Не возможно сложить разные классы/подклассы")
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def created_product(cls, product_date: Dict[str, Any]) -> "Product":
        """
        Классовый метод создания экземпляра класса из словаря
        :param product_date: Словарь с параметрами продукта
            Ожидаемые ключи: name, description, price, quantity
        :return: Экземпляр класса Product
        """
        return cls(
            name=product_date.get("name", ""),
            description=product_date.get("description", ""),
            price=product_date.get("price", 0.0),
            quantity=product_date.get("quantity", 0),
        )

    @classmethod
    def new_product(
        cls, product_date: Dict[str, Any], existing_products: Optional[List["Product"]] = None
    ) -> "Product":
        """
        Классовый метод преобразования из словаря в объект класса
        :param product_date: Словарь с параметрами продукта
            Ожидаемые ключи: name, description, price, quantity
        :param existing_products: Список существующих продуктов(по умолчанию пустой)
        :return: Экземпляр класса Product
            Если продукт с таким именем уже существует, обновляет его количество и цену.
            В противном случае создает новый продукт.
        """
        if existing_products is None:
            existing_products = []

        for existing_product in existing_products:
            if existing_product.name == product_date.get("name"):
                existing_product.quantity += product_date.get("quantity", 0)
                existing_product.price = max(existing_product.price, product_date.get("price", existing_product.price))
                return existing_product

        new_product = cls.created_product(product_date)
        existing_products.append(new_product)
        return new_product

    @property
    def price(self) -> float:
        """
        Getter выводит цену
        :return: Цена
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Setter сравнивает цену, если она меньше/равна 0, выводит сообщение
        :param new_price: Новое значение цены
        :return: "Цена не должна быть нулевая или отрицательная"
        При понижении цены запрашивает у пользователя понижать ли ее.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif self.__price > new_price:
            user_out = input("Понизить цену? введите Y/N (yes/no): ")
            if user_out.lower() in ("y", "yes"):
                self.__price = new_price
        else:
            self.__price = new_price
