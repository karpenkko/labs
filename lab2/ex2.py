import math


class Rational:
    def __init__(self, a=1, b=1):
        if not isinstance(a, int):
            raise TypeError("numerator is not an integer")
        if not isinstance(b, int):
            raise TypeError("denominator is not an integer")
        if not b:
            raise ZeroDivisionError("denominator = 0")
        self.a = a
        self.b = b

    def __str__(self):
        k = math.gcd(self.a, self.b)
        a = self.a // k
        b = self.b // k
        return f"{a} / {b}"

    def print2(self):
        print(self.a / self.b)


ob = Rational(15)
ob.b = 45
print(str(ob))
ob.print2()
