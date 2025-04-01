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
