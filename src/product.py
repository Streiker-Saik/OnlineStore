
class Product:
    """
    Класс для предоставления продукта
    Атрибуты:
        name(str): Название продукта
        description(str): Описание продукта
        price(float): Цена продукта
        quantity(int): Количество продукта
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        Метод для инициализации экземпляра продукта
        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество продукта
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
