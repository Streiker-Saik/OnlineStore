from typing import Any, Dict, List, Optional

class Product:
    """
    Класс для предоставления продукта
    Атрибуты:
        name(str): Название продукта
        description(str): Описание продукта
        price(float): Цена продукта
        quantity(int): Количество продукта
    Методы:
        __init__(self, name: str, description: str, price: float, quantity: int) -> None:
            Инициализирует экземпляр класса Product с заданными атрибутам
        new_product(cls, product: Dict[str, Any], existing_products: List['Product']) -> 'Product':
            Создает новый экземпляр класса Product на основе данных из словаря.
            Если такой продукт с name существует в списке, обновляет количество и цену
    """
    name: str
    description: str
    price: float
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
        self.price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product: Dict[str, Any], existing_products: Optional[List['Product']] = None) -> 'Product':
        """
        Классовый метод преобразования из словаря в объект класса
        :param product: Словарь с параметрами продукта
            Ожидаемые ключи: name, description, price, quantity
        :param existing_products: Список существующих продуктов(по умолчанию пустой)
        :return: Экземпляр класса Product
            Если продукт с таким именем уже существует, обновляет его количество и цену.
            В противном случае создает новый продукт.
        """
        for existing_product in existing_products:
            if existing_product.name == product.get("name", ""):
                existing_product.quantity += product.get("quantity", 0)
                existing_product.price = max(existing_product.price, product.get("price", 0.0))
                return existing_product
        new_product = cls(
            name=product.get("name", ""),
            description=product.get("description", ""),
            price=product.get("price", 0.0),
            quantity=product.get("quantity", 0)
        )
        existing_products.append(new_product)
        return new_product