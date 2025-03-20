# Проект "Интернет-магазин"

## Описание:

Новые классы: Category, Product\
Реализованна функциональность конвертации из json в объекты класса

## Проверить версию Python:

Убедитесь, что у вас установлен Python (версия 3.x). Вы можете проверить установленную версию Python, выполнив команду:
```
python --version
```

## Установка Poetry:
Если у вас еще не установлен Poetry, вы можете установить его, выполнив следующую команду
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Проверить Poetry добавлен в ваш PATH.
```bash
poetry --version
```

## Установка:
- Клонируйте репозиторий:
```bash
git clone git@github.com:Streiker-Saik/OnlineStore.git
```
- Перейдите в директорию проекта:
```
cd "ваш-репозиторий"
```
- Установите необходимые зависимости:
```bash
poetry add pip
poetry add --group lint flake8 black isort mypy
poetry add --group dev pytest pytest-cov
```

# Примеры работы функций:

## Модуль src.product.py
class Product:
```
Атрибуты:
        name(str): Название продукта
        description(str): Описание продукта
        price(float): Цена продукта (private)
        quantity(int): Количество продукта
Методы:
        __init__(self, name: str, description: str, price: float, quantity: int) -> None:
            Инициализирует экземпляр класса Product с заданными атрибутам
        new_product(cls, product: Dict[str, Any], existing_products: List['Product']) -> 'Product':
            Создает новый экземпляр класса Product на основе данных из словаря.
            Если такой продукт с name существует в списке, обновляет количество и цену
        price(self) -> float:
            Getter: возвращает значение цены
        price(self, new_price: float) -> None:
            Setter: заменяет значение цены. 
            При меньше или равное 0 выводит сообщение предупреждения. 
            При уменьшении цены запрашивает у пользователя подтверждение
```

## Модуль src.category.py
class Category:
```
Атрибуты:
    name(str): Название категории
    description(str): Описание категории
    products(list): Список продукта (private)
    category_count(int): Общее количество созданных категорий
    product_count(int): Общее количество созданных продукта
Методы:
        __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
            Инициализирует экземпляр класса Category с заданными атрибутам
        get_products(self) -> List[Product]:
            Getter: возвращает список продуктов в категории
        add_product(self, product: Product) -> None:
            Метод: добавляет в категорию продукт и обновляет счетчик
        products(self) -> str:
            Getter: возвращает строку с информацией о продуктах о продуктах в категории. Формат:
            <name>, <price> руб. Остаток: <quantity> шт.
```
Увеличивает счетчик категорий(category_count) при создании нового экземпляра 
и устанавливает количество продуктов(product_count) в данной категории.

## Модуль src.utils.py
reader_json
- принимает путь к json файлу
- возвращает список словарей объект Python
```
reader_json(data/product.json)
>>>
[{...},...]
```

created_object_from_json (использует src.product и src.category)
- принимает список словарей, с содержанием категории и ее продуктов
- возвращает список объектов Category
```
date = [
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      ...
    ]
  },
  ...
]
category = created_object_from_json(date)
>>>
category = [<src.category.Category object at 0x000001D70DCA9550>, ...]
category[0].name = Смартфоны
category[0].get_products = [<src.product.Product object at 0x000001D70DCA9400>, ... ]
category[0].get_products[0].name = "Samsung Galaxy C23 Ultra"

```

## Тестирование:
Этот проект использует pytest для тестирования. Чтобы запустить тесты, выполните следующие шаги:

- Запустите тесты с помощью команды:
```bash
pytest
```
- Для получения подробного отчета о тестировании запустите:
```bash
pytest -v
```
- Запустите mypy для проверки типов:
```
mypy "ваш_скрипт".py
```