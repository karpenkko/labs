import math
from decimal import Decimal

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

    def __gt__(self, other):
        return f'{self.__str__()} is greater' if Decimal(self.numerator/self.denominator) > Decimal(other.numerator/other.denominator) \
            else f'{other.__str__()} is greater'

    def __lt__(self, other):
        return f'{self.__str__()} is less' if Decimal(self.numerator/self.denominator) < Decimal(other.numerator/other.denominator) \
            else f'{other.__str__()} is less'

    def __ge__(self, other):
        return f'{self.__str__()} is greater/equal' if Decimal(self.numerator/self.denominator) >= Decimal(other.numerator/other.denominator) \
            else f'{other.__str__()} is greater/equal'

    def __le__(self, other):
        return f'{self.__str__()} is less/equal' if Decimal(self.numerator/self.denominator) <= Decimal(other.numerator/other.denominator) \
            else f'{other.__str__()} is less/equal'

    def __eq__(self, other):
        return f'Fractions are equal' if Decimal(self.numerator/self.denominator) == Decimal(other.numerator/other.denominator) \
            else f'Fractions are not equal'

    def __ne__(self, other):
        return f'Fractions are not equal' if Decimal(self.numerator/self.denominator) != Decimal(other.numerator/other.denominator) \
            else f'Fractions are equal'

    def __str__(self):
        k = math.gcd(self.numerator, self.denominator)
        a = self.numerator // k
        b = self.denominator // k
        return f'{a} / {b}'

    def print_rational(self):
        print(self.numerator / self.denominator)


ob1 = Rational(3, 4)
ob2 = Rational(5, 8)
ob3 = Rational(1, 5)
ob4 = Rational(2, 10)
print(ob1 + ob2)
print(ob1 - ob2)
print(ob1 * ob2)
print(ob1 / ob2)
print(ob1 > ob2)
print(ob3 == ob4)
