import datetime


class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

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
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__year = value

    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 3:
            a, b, c = other
            return Calendar(self.__day+a, self.__month+b, self.__year+c)

    def __sub__(self, other):
        if isinstance(other, tuple) and len(other) == 3:
            a, b, c = other
            return Calendar(self.__day-a, self.__month-b, self.__year-c)

    def convert_date(self):
        return datetime.date(self.__year, self.__month, self.__day)

    def __gt__(self, other):
        return f'{self.convert_date()} is greater' if self.convert_date() > other.convert_date() \
            else f'{other.convert_date()} is greater'

    def __lt__(self, other):
        return f'{self.convert_date()} is less' if self.convert_date() < other.convert_date() \
            else f'{other.convert_date()} is less'

    def __ge__(self, other):
        return f'{self.convert_date()} is greater' if self.convert_date() > other.convert_date() \
            else f'{other.convert_date()} is greater/equal'

    def __le__(self, other):
        return f'{self.convert_date()} is less/equal' if self.convert_date() <= other.convert_date() \
            else f'{other.convert_date()} is less/equal'

    def __eq__(self, other):
        return f'Dates are equal' if self.convert_date() == other.convert_date() \
            else f'Dates are not equal'

    def __ne__(self, other):
        return f'Dates are not equal' if self.convert_date() != other.convert_date() \
            else f'Dates are equal'

    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'


d1 = Calendar(16, 4, 2020)
d2 = Calendar(16, 4, 2020)
d3 = Calendar(10, 5, 2018)
d4 = Calendar(12, 12, 2012)
d5 = Calendar(2, 4, 2022)
d6 = Calendar(11, 11, 2022)
print(d1 >= d2)
print(d3 <= d4)
print(d1 == d2)
print(d3 != d4)
print(d5 > d6)
print(d5 < d6)

