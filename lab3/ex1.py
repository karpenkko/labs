import json


class RegularTicket:
    def __init__(self, name, date, time, number, price):
        self.name = name
        self.date = date
        self.time = time
        self.number = number
        self.price = price

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError
        if number <= 0:
            raise ValueError
        data = open('tickets.json')
        lis = json.load(data)
        for item in lis:
            if number == item:
                raise TypeError
        self.__number = number
        lis.append(number)
        with open('tickets.json', 'w') as tick:
            json.dump(lis, tick)

    def get_regular_price(self):
        return f'Regular ticket. Price:{self.price}'

    def get_regular_ticket(self):
        return f'Ticket №{self.number}\n' \
               f'Event "{self.name}"\n'\
               f'Date: {self.date}   Time: {self.time}\n' \
               f'Price: {self.price}'


class AdvanceTicket(RegularTicket):
    def __init__(self, name, date, time, number, price):
        super().__init__(name, date, time, number, price)
        self.advancePrice = self.price * 0.4

    def get_advance_price(self):
        return f'Advance ticket. Price:{self.advancePrice}'

    def get_advance_ticket(self):
        return f'Ticket №{self.number}\n' \
               f'Event "{self.name}"\n' \
               f'Date: {self.date}   Time: {self.time}\n' \
               f'Price: {self.advancePrice}'


class StudentTicket(RegularTicket):
    def __init__(self, name, date, time, number, price):
        super().__init__(name, date, time, number, price)
        self.studentPrice = self.price * 0.5

    def get_student_price(self):
        return f'Student ticket. Price:{self.studentPrice}'

    def get_student_ticket(self):
        return f'Ticket №{self.number}\n' \
               f'Event "{self.name}"\n' \
               f'Date: {self.date}   Time: {self.time}\n' \
               f'Price: {self.studentPrice}'


class LateTicket(RegularTicket):
    def __init__(self, name, date, time, number, price):
        super().__init__(name, date, time, number, price)
        self.latePrice = round((self.price * 1.1), 2)

    def get_late_price(self):
        return f'Late ticket. Price:{self.latePrice}'

    def get_late_ticket(self):
        return f'Ticket №{self.number}\n' \
               f'Event "{self.name}"\n' \
               f'Date: {self.date}   Time: {self.time}\n' \
               f'Price: {self.latePrice}'


ticket1 = StudentTicket("Pride and prejudice", "16.04.22", "18:00", 8, 100)
print(ticket1.get_student_price())
print(ticket1.get_student_ticket())






