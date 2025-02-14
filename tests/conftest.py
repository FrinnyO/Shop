import pytest

from src.classes import Product
from src.subclasses import LawnGrass, Smartphone


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


@pytest.fixture
def product_smartphone():
    return Smartphone("Samsung", "Безрамочный экран", 90000.0, 3, 10000, "S24", 128, "Black")


@pytest.fixture
def product_smartphone_2():
    return Smartphone("Xiaomi Redmi Note 15", "256GB, Синий", 30000.0, 2, 900, "Note 15", 256, "Синий")


@pytest.fixture
def product_lawn_grass():
    return LawnGrass("Газонная трава", "Премиум вариант", 1000.0, 10, "Шотландия", "5 дней", "Изумрудный")


@pytest.fixture
def product_lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Бюджетный вариант", 100.0, 20, "США", "5 дней", "Темно-зеленый")