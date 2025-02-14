def test_smartphone_init(product_smartphone):
    assert product_smartphone.name == "Samsung"
    assert product_smartphone.description == "Безрамочный экран"
    assert product_smartphone.price == 90000.0
    assert product_smartphone.quantity == 3
    assert product_smartphone.efficiency == 10000
    assert product_smartphone.model == "S24"
    assert product_smartphone.memory == 128
    assert product_smartphone.color == "Black"


def test_lawn_grass_init(product_lawn_grass):
    assert product_lawn_grass.name == "Газонная трава"
    assert product_lawn_grass.description == "Премиум вариант"
    assert product_lawn_grass.price == 1000.0
    assert product_lawn_grass.quantity == 10
    assert product_lawn_grass.country == "Шотландия"
    assert product_lawn_grass.germination_period == "5 дней"
    assert product_lawn_grass.color == "Изумрудный"