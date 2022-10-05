import math


class Rational:
    def __init__(self, a=1, b=1):
        if b:
            k = math.gcd(a, b)
            self.a = int(a / k)
            self.b = int(b / k)
            self.c = float(a / b)

    def print1(self):
        print(self.a, "/", self.b)

    def print2(self):
        print(self.c)


try:
    ob = Rational(45, 51)
    ob.print1()
    ob.print2()
except:
    print("Error")