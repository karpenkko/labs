import json
import uuid
from datetime import datetime, date


class Event:
    def __init__(self, name, year, month, day, hour, minute):
        self.name = name
        now = datetime.now()
        str_d = f'{year}-{month}-{day} {hour}:{minute}'
        d = datetime.strptime(str_d, '%Y-%m-%d %H:%M')
        if d > now:
            self.year = year
            self.month = month
            self.day = day
            self.hour = hour
            self.minute = minute
        else:
            raise ValueError('Event has already passed')

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError
        self.__year = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not 0 < value <= 12:
            raise ValueError
        self.__month = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not 0 < value <= 31:
            raise ValueError
        self.__day = value

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not 0 <= value <= 24:
            raise ValueError
        self.__hour = value

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not 0 <= value <= 60:
            raise ValueError
        self.__minute = value

    def __str__(self):
        return f'Event: "{self.name}"\nDate: {self.day}.{self.month}\nTime: {self.hour}:{self.minute}\n'


class RegularTicket:

    def __init__(self, price, event, discount=1.0, title='Regular'):
        self.title = title
        self.number = uuid.uuid4()
        self.price = round(price * discount)
        self.event = event
        self.__json_serialize(event)

    def __json_serialize(self, event):
        with open('tickets.json', 'r') as tick:
            lis = json.load(tick)
        if 'tickets' not in lis:
            lis['tickets'] = {}
        if str(self.number) not in lis['tickets']:
            lis['tickets'][str(self.number)] = {}
            lis['tickets'][str(self.number)]['name'] = event.name
            lis['tickets'][str(self.number)]['date'] = f'{event.year}.{event.month}'
            lis['tickets'][str(self.number)]['time'] = f'{event.hour}:{event.minute}'
            lis['tickets'][str(self.number)]['title'] = self.title
            lis['tickets'][str(self.number)]['price'] = self.price
        with open('tickets.json', 'w') as tick:
            json.dump(lis, tick, indent=4)

    def get_price(self):
        return self.price

    @classmethod
    def get_ticket(cls, number):
        with open('tickets.json', 'r') as tick:
            lis = json.load(tick)
        if 'tickets' not in lis:
            raise KeyError('No tickets sold')
        if str(number) not in lis['tickets']:
            raise KeyError('No ticket with such number')

        name = lis['tickets'][str(number)]['name']
        day = lis['tickets'][str(number)]['date']
        time = lis['tickets'][str(number)]['time']
        title = lis['tickets'][str(number)]['title']
        price = lis['tickets'][str(number)]['price']

        return f'Event: "{name}"\nDate: {day}\nTime: {time}\n{title} ticket  Number: {number}  Price:{price}'

    def __str__(self):
        return str(self.event) + f'{self.title} ticket  Number: {self.number}  Price:{self.price}'


class AdvanceTicket(RegularTicket):
    def __init__(self, price, event, discount):
        self.title = 'Advance'
        super().__init__(price, event, discount, self.title)


class StudentTicket(RegularTicket):
    def __init__(self, price, event, discount):
        self.title = 'Student'
        super().__init__(price, event, discount, self.title)


class LateTicket(RegularTicket):
    def __init__(self, price, event, discount):
        self.title = 'Late'
        super().__init__(price, event, discount, self.title)


def order(event, early_term, late_term, student_status=False):
    today_date = date.today()
    event_dated = date(event.year, event.month, event.day)
    res = event_dated - today_date
    if student_status:
        return StudentTicket(100, event, 0.5)
    elif res.days >= early_term:
        return AdvanceTicket(100, event, 0.4)
    elif res.days <= late_term:
        return LateTicket(100, event, 1.1)
    else:
        return RegularTicket(100, event)


event1 = Event('Apple Event', 2022, 11, 20, 12, 30)
ticket1 = order(event1, 60, 10)
ticket2 = order(event1, 60, 10, True)
print(ticket2)
print(ticket2.get_price())
print(RegularTicket.get_ticket('a4b05234-3273-40d8-8803-b5c307b190c2'))
