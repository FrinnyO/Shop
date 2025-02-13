import pytest

from src.classes import Product


@pytest.fixture
def product_1():
    return Product("Samsung", "4К экран", 90000.0, 5)


@pytest.fixture
def product_2():
    return Product("Sony", "FullHD", 80000.0, 2)


@pytest.fixture
def product_3():
    return Product("LG", "IPS-матрица", 20000.0, 3)


@pytest.fixture
def product_4():
    return Product("Test_Prod_1", "Test_desc", 20000.0, 3)


@pytest.fixture
def product_5():
    return Product("Test_Prod_2", "Test_desc", 20000.0, 3)
