from src.category import Category
from src.exceptions import ZeroQuantityError
from src.order import Order
from src.product import Product

if __name__ == "__main__":

    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(e)
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт "
            "с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())
    # 140333.33

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
    # 0

    invalid_product = Product("Nubia Z70 Ultra", "512GB, Синий", 70000.0, 1)
    invalid_product.quantity = 0
    print(invalid_product)
    category1.add_product(invalid_product)
    try:
        result = Order(invalid_product, 5)
    except ZeroQuantityError as exc_info:
        print(exc_info)
    else:
        print(result)
    finally:
        print("Обработка добавления товара завершена")
