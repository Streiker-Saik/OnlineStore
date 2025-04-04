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

## Модуль src.interfaces.py
class BaseProduct:
```
Абстрактный класс продуктов
    def new_product(cls, product_date: Dict[str, Any]) -> "BaseProduct":
        Классовый метод преобразования из словаря в объект класса
```
class BaseProduct:
```
Абстрактный класс сущностей
    __str__(self) -> str:
        Строковое отображение класса
```

## Модуль src.mixins.py
class PrintMixin:
```
Класс-миксин, печати в консоль
    __init__(self) -> None:
        Инициализация экземпляра класса с выводом в терминал
    __repr__(self) -> str:
        Строка класса с параметрами
            Формат: "<class_name>(<attribute1>, ...)"
```

## Модуль src.product.py
class Product(BaseProduct, PrintMixin):
```
Класс для предоставления продукта

Атрибуты:
    name(str): Название продукта
    description(str): Описание продукта
    price(float): Цена продукта (private)
    quantity(int): Количество продукта

Методы:
    __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        Инициализирует экземпляр класса Product с заданными атрибутам
    __str__(self) -> str:
        Возвращает строковое отображение класса Product. 
            Формат: <name>, <price> руб. Остаток: <quantity> шт.
    __add__(self, other: 'Product') -> float:
        Возвращает общую стоимость товаров, как сумма стоимости товаров умноженная на их количество
        TypeError: Если переданный аргумент не является тем же классоом/подклассом.
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

## Модуль src.product_smartphone.py
class Smartphone(Product):
```
Класс, представления "Смартфон"

Атрибуты:
    efficiency(float): Производительность
    model(str): Модель
    memory(int): Объем встроенной памяти
    color(str): Цвет
    
Методы:
    __init__(self, name: str, description: str, price: float, quantity: int,
        efficiency: float, model: str, memory: int, color: str) -> None:
        Инициализирует экземпляр, наследуемого от Product класса Smartphone, с заданными атрибутам
```

## Модуль src.product_lawngrass.py
class LawnGrass(Product):
```
Класс, представления "Трава газонная"
    
Атрибуты:
    country(str): Страна-производитель
    germination_period(str): Срок прорастания
    color(str): Цвет
    
Методы:
    __init__(self, name: str, description: str, price: float, quantity: int,
        country: str, germination_period: str, color: str) -> None:
        Инициализирует экземпляр, наследуемого от Product класса LawnGrass, с заданными атрибутам
```

## Модуль src.category.py
class Category(BaseEntity):
```
Класс категорий продукта

Атрибуты:
    name(str): Название категории
    description(str): Описание категории
    products(list): Список продукта (private)
    category_count(int): Общее количество созданных категорий
    product_count(int): Общее количество созданных продукта во всех категориях

Методы:
    __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        Инициализирует экземпляр класса Category с заданными атрибутам
    __str__(self) -> str:
        Возвращает строковое отображение класса Category. 
        Формат: <name>, количество продуктов: <sum(product.quantity)> шт.
    get_products(self) -> List[Product]:
        Getter: возвращает список продуктов в категории
    add_product(self, product: Product) -> None:
        Метод: добавляет в категорию продукт и обновляет счетчик, если его не было в списке
        TypeError: Если переданный аргумент не является экземпляром класса Product.
    products(self) -> str:
        Getter: возвращает строку с информацией о продуктах о продуктах в категории. Формат:
        <name>, <price> руб. Остаток: <quantity> шт.\n
```

## Модуль src.order.py
class Order(BaseEntity):
```
Класс категорий продукта

Атрибуты:
    product(Product): Продукт, который был куплен
    quantity(int): Количество купленного продукта
    over_price(float): Общая стоимость

Методы:
    __init__(self, product: Product, quantity: int) -> None:
        Инициализации экземпляра заказа
    __str__(self) -> str:
        Возвращает строковое отображение класса. Формат:
        <product.name>, <quantity> шт: <total_price> руб
    update_quantity(self, new_quantity: int) -> None:
        Метод: обновление количество в заказе
        TypeError: Если переданный аргумент не является целым числом
        ValueError: Если переданный аргумент отрицательный
```

## Модуль src.products_iterator.py
class ProductIterator:
```
Итератор класса Category, позволяющий перебирать продукты в категории

Атрибуты:
    category_obj(Category) - объект класса Category

Методы:
    __init__(self, category_obj: Category) -> None:
        Инициализирует объект класса Category
    __iter__(self) -> Iterator:
        Возвращает сам итератор
    __next__(self) -> Product:
        Возвращает следующий продукт в категории
```

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