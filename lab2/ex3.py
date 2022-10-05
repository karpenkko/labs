class Product:
    def __init__(self, price=None, description=None, dimensions=None):
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:
    def __init__(self, surname=None, name=None, patronymic=None, phone_number=None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phoneNumber = phone_number


class Order:
    def __init__(self, customer, *args):
        self.customer = customer
        self.products = args
        self.price = 0
    def total(self):
        for item in self.products:
            self.price += item.price
        return f"{self.customer.surname} {self.customer.name}: {self.price}$ (total)"


product1 = Product(25, "Sport pants", "xs s m l xl")
product2 = Product(30, "Sweatshirt", " s m l xl")
customer1 = Customer("Karpenko", "Yaroslava", "Yuriivna", "0972397041")
order1 = Order(customer1, product1, product2)
print(order1.total())