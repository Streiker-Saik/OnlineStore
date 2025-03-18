def test_init_category(first_category) -> None:
    """Тестирование корректной инициализации класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, но и получение "
                                          "дополнительных функций для удобства жизни")
    assert len(first_category.products) == 2
    assert first_category.category_count == 1
    assert first_category.product_count == 2

