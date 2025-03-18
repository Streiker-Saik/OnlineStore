class Category:
    """
    Класс категорий продукта
    Атрибуты:
        name(str): Название категории
        description(str): Описание категории
        products(list): Список продукта
        category_count(int): Общее количество созданных категорий
        product_count(int): Общее количество созданных продукта
    """

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Метод для инициализации экземпляра категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов

        Увеличивает счетчик категорий при создании нового экземпляра
        и устанавливает количество продуктов в данной категории
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count = len(products) if products else 0
