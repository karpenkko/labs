class Product:
    def __init__(self, price, description=None, dimensions=None):
        if isinstance(price, int | float) and price > 0:
            self.price = price
        else:
            self.price = None
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.description}: {self.price}$ ({self.dimensions})"


class Customer:
    def __init__(self, surname=None, name=None, patronymic=None, phone_number=None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phoneNumber = phone_number

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic} {self.phoneNumber}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.number = 0
        self.total = 0

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            self.number += 1

    def del_product(self, product):
        if isinstance(product, Product):
            for item in self.products:
                if str(item) == str(product):
                    self.products.remove(item)
                    self.number -= 1

    def get_total(self):
        for item in self.products:
            self.total += item.price
        print(self.total)

    def __str__(self):
        return f"Order\n" \
               f"Customer: \n{self.customer.surname} {self.customer.name} {self.customer.patronymic} " \
               f"{self.customer.phoneNumber} \n" \
               f"Products:\n" + ("\n".join(map(str, self.products))) + f"\nTotal: {self.total}"


product1 = Product(45, "Sport pants", "xs")
product2 = Product(30, "Sweatshirt", "s")
product3 = Product(50, "Jacket", "m")
customer1 = Customer("Karpenko", "Yaroslava", "Yuriivna", "0972397041")
order1 = Order(customer1)
order1.add_product(product1)
order1.add_product(product2)
order1.add_product(product3)
order1.del_product(product3)
order1.get_total()
print(str(order1))
