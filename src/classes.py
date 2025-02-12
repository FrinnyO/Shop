class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if quantity < 1:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products__ = products
        self.__class__.category_count += 1
        self.__class__.product_count += len(products)

    def __quan__(self):
        return f"{self.name}, количество продуктов: {sum(x.quantity for x in self.__products__)} шт."

    def __len__(self):
        return len(self.__products__)