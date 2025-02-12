import pytest

from src.classes import Product


@pytest.fixture
def product_1():
    return Product("Samsung", "4К экран", 90000.0, 5)


@pytest.fixture
def product_2():
    return Product("Sony", "FullHD", 800000.0, 2)


@pytest.fixture
def product_3():
    return Product("LG", "IPS-матрица", 20000.0, 3)
