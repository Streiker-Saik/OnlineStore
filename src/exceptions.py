from typing import Optional


class ZeroQuantityError(Exception):
    """Исключение, добавление продукта с нулевым количеством"""

    def __init__(self, message: Optional[str] = None) -> None:
        """
        Метод для инициализации исключения
        :param message: Сообщение, описывающее причину исключения (по умолчанию None)
        """
        self.message = message
        super().__init__(message)
