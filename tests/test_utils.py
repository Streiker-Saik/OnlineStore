import json
from pathlib import Path
from typing import Any, Dict, List

import pytest

from src.utils import created_object_from_json, reader_json

BASEDIR = Path(__file__).resolve().parent.parent


def test_reader_json_non_existent_file() -> None:
    """Тест, если файл JSON - не найден"""
    file_path = "non.json"
    assert reader_json(file_path) == []


def test_reader_json() -> None:
    """Тест работы функции"""
    try:
        file_path = "test.json"
        path: Path = BASEDIR / file_path
        date = [{"key": "value"}, {"key": "value"}]
        with open(path, "w", encoding="utf-8") as file_json:
            json.dump(date, file_json, indent=4, ensure_ascii=False)

        assert reader_json(file_path) == date
    finally:
        if path.exists():
            path.unlink()


def test_reader_json_empty_list() -> None:
    """Тест, если файл JSON - с пустым списком"""
    try:
        file_path = "test.json"
        path: Path = BASEDIR / file_path
        date: List = []
        with open(path, "w", encoding="utf-8") as file_json:
            json.dump(date, file_json, indent=4, ensure_ascii=False)

        assert reader_json(file_path) == date
    finally:
        if path.exists():
            path.unlink()


def test_reader_json_invalid() -> None:
    """Тест, если файл JSON - с некорректными данными"""
    try:
        file_path = "test.json"
        path: Path = BASEDIR / file_path
        data = "некорректные данные"
        with open(file_path, "w", encoding="utf-8") as file_json:
            file_json.write(data)

        assert reader_json(file_path) == []
    finally:
        if path.exists():
            path.unlink()


def test_reader_json_not_list() -> None:
    """Тест, если файл JSON - не со списком"""
    try:
        file_path = "test.json"
        path: Path = BASEDIR / file_path
        data: str = ""
        with open(file_path, "w", encoding="utf-8") as file_json:
            json.dump(data, file_json, indent=4, ensure_ascii=False)

        assert reader_json(file_path) == []
    finally:
        if path.exists():
            path.unlink()


def test_created_object_from_json(products_list: List[Dict[str, Any]]) -> None:
    """Тестирование проверяет конвертирование строки в объект класса"""
    result = created_object_from_json(products_list)
    assert result[0].name == "Смартфоны"
    assert result[0].description == (
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни"
    )
    assert len(result[0].products) == 3
    assert result[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert result[0].products[0].description == "256GB, Серый цвет, 200MP камера"
    assert result[0].products[0].price == 180000.0
    assert result[0].products[0].quantity == 5
    assert result[1].name == "Телевизоры"
    assert result[1].description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    assert len(result[1].products) == 1


def test_created_object_from_json_crash() -> None:
    """"""
    data = [
        {"name": "xxx", "description": "xxx", "products": ["xxx"]},
        {"name": "xxx", "description": "xxx", "products": ["xxx"]},
    ]
    with pytest.raises(TypeError) as exc_info:
        created_object_from_json(data)

    assert "Ошибка создания объекта из данных." in str(exc_info.value)
