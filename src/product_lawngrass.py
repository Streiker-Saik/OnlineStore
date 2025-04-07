from typing import Any, Dict

from src.product import Product


class LawnGrass(Product):
    """
    Класс, представления "Трава газонная"

    Атрибуты:
        country(str): Страна-производитель
        germination_period(str): Срок прорастания
        color(str): Цвет

    Методы:
        __init__(self, name: str, description: str, price: float, quantity: int,
            country: str, germination_period: str, color: str) -> None:
            Инициализирует экземпляр, наследуемого от Product класса LawnGrass, с заданными атрибутам
    """

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Метод для инициализации экземпляра травы газонной
        :param name: Название
        :param description: Описание
        :param price: Цена
        :param quantity: Количество
        :param country: Страна-производитель
        :param germination_period: Срок прорастания
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @classmethod
    def created_product(cls, product_date: Dict[str, Any]) -> "LawnGrass":
        """
        Классовый метод создания экземпляра класса из словаря
        :param product_date: Словарь с параметрами продукта
            Ожидаемые ключи: name, description, price, quantity, country, germination_period, color
        :return: Экземпляр класса Smartphone
        """
        return cls(
            name=product_date.get("name", ""),
            description=product_date.get("description", ""),
            price=product_date.get("price", 0.0),
            quantity=product_date.get("quantity", 0),
            country=product_date.get("country", ""),
            germination_period=product_date.get("germination_period", ""),
            color=product_date.get("color", ""),
        )
