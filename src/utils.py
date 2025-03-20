import json
import logging
from typing import Any, Dict, List

from src.category import Category
from src.product import Product
from src.settings import BASE_DIR, LOGS_DIR

name_file = "utils.log"
log_file = LOGS_DIR / name_file

utils_logger = logging.getLogger(name_file)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s: %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def reader_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Функцию открывания JSON-файла
    :param file_path: путь до JSON-файла
    :return: список словарей с данными
    """
    path = BASE_DIR / file_path

    if not path.exists():
        utils_logger.error(f"Файл '{file_path}' - не найден")
        return []

    try:
        utils_logger.info(f'Выполняем преобразование JSON-файла "{file_path}" в объект Python')
        with open(path, "r", encoding="utf-8") as file_json:
            data = json.load(file_json)

            if type(data) is not list:
                utils_logger.error("Файл содержит не список")
                return []

            utils_logger.info(f'Преобразование JSON-файла "{file_path}" в объект Python выполнено')
            return data

    except json.JSONDecodeError as exc_info:
        utils_logger.error(f"Невозможно преобразовать json дынные: {exc_info}")
        return []


def created_object_from_json(data: List[Dict[str, Any]]) -> List[Category]:
    """
    Функция создает объекты класса из словаря продуктов
    :param data: Список словарей, с содержанием категории и ее продуктов
        Структура данных:
            [
                {
                    "name": "xxx",
                    "description": "xxx",
                    "products": [
                        {
                            "name": "xxx",
                            "description":
                            "ххх",
                            "price": хх.х,
                            "quantity": Х
                        },
                        ...
                },
                ...
            ]
    :return: Список объектов Category

    :raises TypeError: Если данные не соответствуют ожидаемому формату при создании объектов Product или Category.
    """
    utils_logger.info("Конвертирование списка в объекты класса началось")
    categories = []
    for category in data:
        products = []
        try:
            for product in category["products"]:
                products.append(Product(**product))
            category["products"] = products
            categories.append(Category(**category))
            utils_logger.info(f"Конвертирование {category} в объекты класса законченно успешно")
        except TypeError as exc_info:
            error_message = f"Ошибка создания объекта из данных. {exc_info}"
            utils_logger.error(error_message)
            raise TypeError(error_message)

    return categories
