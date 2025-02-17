import pytest

from src.classes import BaseProduct, Category, Order, Product


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


def test_add_products(product_4, product_5):
    test_products = Category("Test_Prods", "Test_description", [product_4])
    test_products.add_product(product_5)
    assert test_products.product_count == 5


def test_set_price(product_1):
    product_1.price = 100000
    assert product_1.price == 100000


def test_set_price_negative(capsys, product_1):
    product_1.price = -100
    message = capsys.readouterr()
    assert (
        message.out.split("\n")[-2] == "Цена не должна быть нулевая или отрицательная"
    )


def test_new_product(product_1):
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_make_string_products(product_1, product_2):
    tv_products = Category("TV", "Premium class", [product_1, product_2])
    assert (
        tv_products.products
        == f"""{product_1.name}, {product_1.price} руб. Остаток: {product_1.quantity} шт.
{product_2.name}, {product_2.price} руб. Остаток: {product_2.quantity} шт.\n"""
    )


def test_add_method_products(product_1, product_2):
    assert product_1 + product_2 == 610000.0


def test_str_product(product_1):
    assert str(product_1) == "Samsung, 90000.0 руб. Остаток: 5 шт."


def test_str_category(product_1, product_2):
    tv_products = Category("TV", "Premium class", [product_1, product_2])
    assert str(tv_products) == "TV, количество продуктов: 7 шт."


def test_add_same_product(
    product_smartphone, product_smartphone_2, product_lawn_grass, product_lawn_grass_2
):
    assert product_smartphone + product_smartphone_2 == 330000.0
    assert product_lawn_grass + product_lawn_grass_2 == 12000.0


def test_add_different_products(product_smartphone_2, product_lawn_grass_2):
    with pytest.raises(TypeError):
        assert product_smartphone_2 + product_lawn_grass_2


def test_add_not_product(product_lawn_grass, product_lawn_grass_2):
    grass_products = Category(
        "Lawn Grass", "Для частных домов", [product_lawn_grass, product_lawn_grass_2]
    )
    with pytest.raises(TypeError):
        assert grass_products.add_product("Wrong Product")


def test_mixinprint(capsys):
    Product("test_name", "test_description", 100, 2)
    log_message = capsys.readouterr()
    assert log_message.out.strip() == "Product(test_name, test_description, 100, 2)"


def test_abstract_class_inheritance_error():
    class TestProduct(BaseProduct):

        def __init__(self):
            pass

    with pytest.raises(TypeError):
        TestProduct()


def test_create_order_object(product_1):
    test_order = Order(product_1, 1)
    assert test_order.product == product_1
    assert test_order.quantity == 1
    assert test_order.price == 90000.0
    assert product_1.quantity == 4


def test_create_order_failed(product_1):
    with pytest.raises(ValueError):
        Order(product_1, 8)


def test_print_order(product_1):
    test_order = Order(product_1, 1)
    assert str(test_order) == "В заказе: Samsung - количество: 1"


def test_add_product_to_order(product_1):
    test_order = Order(product_1, 4)
    test_order.add_product(product_1)
    assert test_order.quantity == 5
    assert test_order.price == 450000.0
    assert product_1.quantity == 0
    with pytest.raises(ValueError):
        test_order.add_product(product_1)


def test_add_product_to_order_failed(product_1, product_2):
    test_order = Order(product_1, 2)
    with pytest.raises(TypeError):
        test_order.add_product(product_2)
