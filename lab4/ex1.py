import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError('numerator is not an integer')
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError('denominator is not an integer')
        if not value:
            raise ZeroDivisionError('denominator = 0')
        self.__denominator = value

    def __add__(self, other):
        if isinstance(other, Rational):
            den = math.lcm(self.denominator, other.denominator)
            num1 = den // self.denominator * self.numerator
            num2 = den // other.denominator * other.numerator
            num = num1 + num2
            return Rational(num, den)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            den = math.lcm(self.denominator, other.denominator)
            num1 = den // self.denominator * self.numerator
            num2 = den // other.denominator * other.numerator
            num = num1 - num2
            return Rational(num, den)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
            return Rational(num, den)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Rational):
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
            return Rational(num, den)
        return NotImplemented

    def __str__(self):
        k = math.gcd(self.numerator, self.denominator)
        a = self.numerator // k
        b = self.denominator // k
        return f'{a} / {b}'

    def print_rational(self):
        print(self.numerator / self.denominator)


ob1 = Rational(3, 4)
ob2 = Rational(5, 6)
print(ob1 + ob2)
print(ob1 - ob2)
print(ob1 * ob2)
print(ob1 / ob2)
