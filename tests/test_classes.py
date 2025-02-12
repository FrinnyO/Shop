import pytest

from src.classes import Category, Product


def test_create_product(product_1):
    assert product_1.name == "Samsung"
    assert product_1.description == "4К экран"
    assert product_1.price == 90000.0
    assert product_1.quantity == 5


def test_create_categories(product_1, product_2, product_3):
    tv_products = Category("TV_Products", "Premium class", [product_1, product_2])
    assert tv_products.name == "TV_Products"
    assert tv_products.description == "Premium class"
    assert tv_products.product_count == 2
    assert Category.category_count == 1
    monitors = Category("Monitors", "Лучшие игровые мониторы", [product_3])
    assert monitors.name == "Monitors"
    assert monitors.description == "Лучшие игровые мониторы"
    assert monitors.product_count == 3
    assert Category.category_count == 2
