class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        if isinstance(length, float) and isinstance(width, float):
            if 0.0 < length < 20.0 and 0.0 < width < 20.0:
                self.__length = length
                self.__width = width

    def set_width(self, value=1.0):
        if isinstance(value, float):
            if 0.0 < value < 20.0:
                self.__width = value

    def set_length(self, value=1.0):
        if isinstance(value, float):
            if 0.0 < value < 20.0:
                self.__length = value

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width


try:
    rec1 = Rectangle(16.0)
    rec1.set_width(3.0)
    print("length and width", rec1.get_length(), rec1.get_width())
    print("perimeter", rec1.perimeter())
    print("area", rec1.area())
except AttributeError:
    print("Incorrect input")
