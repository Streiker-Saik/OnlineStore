from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseProduct(ABC):
    """Абстрактный класс продуктов"""

    @classmethod
    @abstractmethod
    def created_product(cls, product_date: Dict[str, Any]) -> "BaseProduct":
        """Классовый метод создания экземпляра класса из словаря"""
        pass


class BaseEntity(ABC):
    """Абстрактный класс сущностей"""

    @abstractmethod
    def __str__(self) -> str:
        """Магический метод, строковое отображение класса."""
        pass
