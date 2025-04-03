class PrintMixin:
    """Класс-миксин, печати в консоль"""

    def __repr__(self) -> str:
        """
        Магический метод, вывода в консоль класса с параметрами
        :return: Строка класса с параметрами
            Формат: "<class_name>(<attribute1>, ...)"
        """
        attributes = ", ".join(f"{value!r}" for value in self.__dict__.values())
        return f"{self.__class__.__name__}({attributes})"
