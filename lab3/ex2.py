from datetime import datetime

addition_ingredients = {'pineapple': 14, 'bacon': 25, 'mushrooms': 9, 'sausages': 20,
                        'chicken': 20, 'corn': 5, 'olives': 10, 'paprika': 10, 'tomato': 10,
                        'pepper': 10, 'salami': 20, 'extra cheese': 20}


class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.components = ingredients
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__price = value

    def agg_ingredients(self, *args):
        for item in args:
            if addition_ingredients[item]:
                self.components.append(item)
                self.price += addition_ingredients[item]

    def __str__(self):
        return f'{self.name}\nIngredients: {self.components}\nTotal price: {self.price}'


class FourMeats(Pizza):
    def __init__(self):
        self.title = 'Monday: four meats'
        self.ingredients = ['sauce', 'cheese', 'salami', 'chicken', 'sausages', 'bacon', 'onion']
        self.price = 109
        super().__init__(self.title, self.ingredients, self.price)


class FourCheeses(Pizza):
    def __init__(self):
        self.title = 'Tuesday: four cheeses'
        self.ingredients = ['sauce', 'dutch cheese', 'mozzarella cheese', 'dor bleu cheese', 'parmesan cheese']
        self.price = 105
        super().__init__(self.title, self.ingredients, self.price)


class WhiteChicken(Pizza):
    def __init__(self):
        self.title = 'Wednesday: white chicken'
        self.ingredients = ['sauce', 'cheese', 'onion', 'tomato', 'chicken', 'bacon']
        self.price = 99
        super().__init__(self.title, self.ingredients, self.price)


class Hawaiian(Pizza):
    def __init__(self):
        self.title = 'Thursday: hawaiian'
        self.ingredients = ['sauce', 'cheese', 'onion', 'pineapple', 'chicken']
        self.price = 95
        super().__init__(self.title, self.ingredients, self.price)


class ChickenMushrooms(Pizza):
    def __init__(self):
        self.title = 'Friday: chicken mushrooms'
        self.ingredients = ['sauce', 'cheese', 'onion', 'mushrooms', 'chicken', 'bacon']
        self.price = 89
        super().__init__(self.title, self.ingredients, self.price)


class Margarita(Pizza):
    def __init__(self):
        self.title = 'Saturday: margarita'
        self.ingredients = ['sauce', 'cheese', 'tomato']
        self.price = 69
        super().__init__(self.title, self.ingredients, self.price)


class Pepperoni(Pizza):
    def __init__(self):
        self.title = 'Sunday: pepperoni'
        self.ingredients = ['sauce', 'cheese', 'salami', 'pepper']
        self.price = 135
        super().__init__(self.title, self.ingredients, self.price)


pizzas = {1: FourMeats, 2: FourCheeses, 3: WhiteChicken, 4: Hawaiian, 5: ChickenMushrooms, 6: Margarita, 7: Pepperoni}


def return_pizza(day):
    for item in pizzas:
        if item == day:
            return pizzas[item]


now = datetime.now()
week_day = datetime.isoweekday(now)

pizza_of_the_day = return_pizza(week_day)
pizza1 = pizza_of_the_day()
pizza1.agg_ingredients('chicken')
print(pizza1)
