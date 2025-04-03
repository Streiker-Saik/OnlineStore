from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация продукта"""
        pass


class BaseEntity(ABC):
    """Абстрактный класс сущностей"""

    @abstractmethod
    def __init__(self) -> None:
        """Инициализация сущности"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Магический метод, строковое отображение класса."""
        pass
