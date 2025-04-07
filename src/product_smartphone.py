from typing import Any, Dict

from src.product import Product


class Smartphone(Product):
    """
    Класс, представления "Смартфон"

    Атрибуты:
        efficiency(float): Производительность
        model(str): Модель
        memory(int): Объем встроенной памяти
        color(str): Цвет

    Методы:
        __init__(self, name: str, description: str, price: float, quantity: int,
            efficiency: float, model: str, memory: int, color: str) -> None:
            Инициализирует экземпляр, наследуемого от Product класса Smartphone, с заданными атрибутам
    """

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Метод для инициализации экземпляра смартфона
        :param name: Название
        :param description: Описание
        :param price: Цена
        :param quantity: Количество
        :param efficiency: Производительность
        :param model: Модель
        :param memory: Объем встроенной памяти
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def created_product(cls, product_date: Dict[str, Any]) -> "Smartphone":
        """
        Классовый метод создания экземпляра класса из словаря
        :param product_date: Словарь с параметрами продукта
            Ожидаемые ключи: name, description, price, quantity, efficiency, model, memory, color
        :return: Экземпляр класса Smartphone
        """
        return cls(
            name=product_date.get("name", ""),
            description=product_date.get("description", ""),
            price=product_date.get("price", 0.0),
            quantity=product_date.get("quantity", 0),
            efficiency=product_date.get("efficiency", 0.0),
            model=product_date.get("model", ""),
            memory=product_date.get("memory", 0),
            color=product_date.get("color", ""),
        )
