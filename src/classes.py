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
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.quantity * self.__price + other.quantity * other.price
        raise TypeError

    @classmethod
    def new_product(cls, params):
        return cls(**params)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            choice = input(
                f'Введите "y" чтобы подтвердить снижение цены. Старая цена: {self.__price}->Новая цена: {new_price}\n'
            )
            if choice == "y":
                self.__price = float(new_price)
        else:
            self.__price = float(new_price)


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.__class__.category_count += 1
        self.__class__.product_count += len(products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum(x.quantity for x in self.__products)} шт."

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.__class__.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_list_string = ""
        for product in self.__products:
            product_list_string += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list_string
