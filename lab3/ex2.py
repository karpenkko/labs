class Pizza:
    def __init__(self, *args):
        self.basic = ['sauce', 'cheese']
        self.ingredients = {'pineapple': 14, 'bacon': 25, 'mushrooms': 9, 'sausages': 20, 'chicken': 20, 'corn': 5,
                            'olives': 10, 'paprika': 10, 'tomato': 10, 'pepper': 10, 'salami': 20, 'extra cheese': 20}
        self.extra = []
        self.price = 0
        for item in args:
            if self.ingredients[item]:
                self.extra.append(item)
                self.price += self.ingredients[item]


class Monday(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.m_name = '4 meats'
        self.m_basic = self.basic + ['salami', 'chicken', 'sausages', 'bacon', 'onion'] + self.extra
        self.m_price = 109 + self.price

    def __str__(self):
        return f'Monday pizza: {self.m_name}\n' \
               f'Ingredients: {self.m_basic}\n' \
               f'Total price: {self.m_price}'


class Tuesday(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.t_name = '4 cheeses'
        self.t_basic = self.basic + ['dutch cheese', 'mozzarella cheese', 'dor bleu cheese', 'parmesan cheese'] + self.extra
        self.t_basic.remove('cheese')
        self.t_price = 105 + self.price

    def __str__(self):
        return f'Tuesday pizza: {self.t_name}\n' \
               f'Ingredients: {self.t_basic}\n' \
               f'Total price: {self.t_price}'


class Wednesday(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.w_name = 'white chicken'
        self.w_basic = self.basic + ['onion', 'tomato', 'chicken', 'bacon'] + self.extra
        self.w_price = 99 + self.price

    def __str__(self):
        return f'Wednesday pizza: {self.w_name}\n' \
               f'Ingredients: {self.w_basic}\n' \
               f'Total price: {self.w_price}'


class Thursday(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.th_name = 'hawaiian'
        self.th_basic = self.basic + ['onion', 'pineapple', 'chicken'] + self.extra
        self.th_price = 95 + self.price

    def __str__(self):
        return f'Thursday pizza: {self.th_name}\n' \
               f'Ingredients: {self.th_basic}\n' \
               f'Total price: {self.th_price}'


class Friday(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.f_name = 'chicken mushrooms'
        self.f_basic = self.basic + ['onion', 'mushrooms', 'chicken', 'bacon'] + self.extra
        self.f_price = 89 + self.price

    def __str__(self):
        return f'Friday pizza: {self.f_name}\n' \
               f'Ingredients: {self.f_basic}\n' \
               f'Total price: {self.f_price}'


class Saturday(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.sat_name = 'margarita'
        self.sat_basic = self.basic + ['tomato'] + self.extra
        self.sat_price = 69 + self.price

    def __str__(self):
        return f'Saturday pizza: {self.sat_name}\n' \
               f'Ingredients: {self.sat_basic}\n' \
               f'Total price: {self.sat_price}'


class Sunday(Pizza):
    def __init__(self, *args):
        super().__init__(*args)
        self.s_name = 'pepperoni'
        self.s_basic = self.basic + ['salami', 'pepper'] + self.extra
        self.s_price = 135 + self.price

    def __str__(self):
        return f'Sunday pizza: {self.s_name}\n' \
               f'Ingredients: {self.s_basic}\n' \
               f'Total price: {self.s_price}'


pizza = Tuesday('paprika')
print(pizza)
