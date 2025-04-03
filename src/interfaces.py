from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс продуктов"""

    @abstractmethod
    def __init__(self) -> None:
        """Инициализация продукта"""
        pass


class BaseEntity(ABC):
    """Абстрактный класс сущностей"""
    pass
