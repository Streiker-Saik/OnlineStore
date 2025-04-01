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

    def __add__(self, other: "Product") -> float:
        """
        Суммирование двух 'смартфонов' общей стоимости
        :param other: экземпляр класса Smartphone, который будет добавлен
        :return: общая стоимость 'смартфонов', как сумма стоимости 'смартфонов' умноженная на их количество
        :raises TypeError: Если переданный аргумент не является экземпляром класса Smartphone.
        """
        if type(other) is not Smartphone:
            raise TypeError("Переданный аргумент, не является классом Smartphone")
        return self.price * self.quantity + other.price * other.quantity
