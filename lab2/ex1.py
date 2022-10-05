class Rectangle:
    length = None
    width = None

    def setter(self, length=1.0, width=1.0):
        if isinstance(length, float) and isinstance(width, float):
            if 0.0 < length < 20.0 and 0.0 < width < 20.0:
                self.length = length
                self.width = width
                return True
            else:
                return False
        else:
            return False

    def getter(self):
        return self.length, self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


rec1 = Rectangle()
if rec1.setter(16.0):
    print("length and width", rec1.getter())
    print("perimeter", rec1.perimeter())
    print("area", rec1.area())
else:
    print("Incorrect input")
