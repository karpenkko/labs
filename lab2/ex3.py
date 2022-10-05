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
    def total(self, cus1, prod1, prod2):
        return f"{cus1.surname} {cus1.name}: {prod1.price+prod2.price}$ (total)"


product1 = Product(25, "Sport pants", "xs s m l xl")
product2 = Product(30, "Sweatshirt", " s m l xl")
customer1 = Customer("Karpenko", "Yaroslava", "Yuriivna", "0972397041")
order1 = Order()
print(order1.total(customer1, product1, product2))