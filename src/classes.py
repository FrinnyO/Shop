from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, params):
        pass


class ProductGroup(ABC):

    @abstractmethod
    def add_product(self, product):
        pass


class MixinPrint:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinPrint, BaseProduct):
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
        super().__init__()

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


class Category(ProductGroup):
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

    def __len__(self):
        return len(self.__products)

    def middle_price(self):
        try:
            return round(sum(x.price for x in self.__products) / len(self), 2)
        except ZeroDivisionError:
            return 0


class Order(ProductGroup):

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        if quantity > product.quantity:
            raise ValueError(
                f"Превышен лимит товара на складе. Текущее количество {product.name}: {product.quantity}"
            )
        self.product = product
        self.quantity = quantity
        self.price = product.price * self.quantity
        product.quantity -= self.quantity

    def __str__(self):
        return f"В заказе: {self.product.name} - количество: {self.quantity}"

    def add_product(self, add_product: Product):
        if add_product.quantity < 1:
            raise ValueError("Товар закончился")
        if (
            self.product.name == add_product.name
            and self.product.description == add_product.description
        ):
            self.quantity += 1
            self.price += add_product.price
            add_product.quantity -= 1
        else:
            raise TypeError("Нельзя складывать разные товары")
