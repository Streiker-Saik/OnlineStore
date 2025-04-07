from src.interfaces import BaseEntity
from src.product import Product


class Order(BaseEntity):
    """
    Класс заказа продукта

    Атрибуты:
       product(Product): Продукт, который был куплен
       quantity(int): Количество купленного продукта
       over_price(float): Общая стоимость

    Методы:
        __init__(self, product: Product, quantity: int) -> None:
            Инициализации экземпляра заказа
        __str__(self) -> str:
            Магический метод, строковое отображение класса. Формат:
            <product.name>, <quantity> шт: <total_price> руб
        update_quantity(self, new_quantity: int) -> None:
            Метод: обновление количество в заказе
    """

    product: Product
    quantity: int
    over_price: float

    def __init__(self, product: Product, quantity: int) -> None:
        """
        Метод для инициализации экземпляра заказа
        :param quantity: Количество продукта
        :param product: Продукт, который был куплен

        Высчитывает общую стоимость заказа продукта
        """
        self.product = product
        self.quantity = quantity
        self.total_price = quantity * product.price
        super().__init__()

    def __str__(self) -> str:
        """
        Магический метод, строковое отображение класса.
        :return: Строка отображения класса. Формат:
            <product.name>, <quantity> шт: <total_price> руб
        """
        return f"{self.product.name}, {self.quantity} шт: {self.total_price} руб"

    def update_quantity(self, new_quantity: int) -> None:
        """
        Обновление количество в заказе
        :param new_quantity: Новое количество
        :raise TypeError: Переданный аргумент не является целым числом
        :raise ValueError: Количество не может быть меньше 0
        """
        if not isinstance(new_quantity, int):
            raise TypeError("Переданный аргумент не является целым числом")
        elif new_quantity < 0:
            raise ValueError("Количество не может быть меньше 0")
        self.quantity = new_quantity
        self.total_price = self.quantity * self.product.price


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    Order(product1, 5)
