""" Расчет площади треугольника"""

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__area = None

    @property
    def size(self):
        return self.__width, self.__height

    @size.setter
    def size(self, new_width, new_height):
        self.__width = new_width
        self.__height = new_height
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__width * self.__height

        return self.__area


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)
r3 = Rectangle(10, 5)

print(r1.area)
print(r2.area)
print(r3.area)

width_r4 = input("Введите ширину прямоугольника: ")
height_r4 = input("Введите высоту прямоугольника: ")

r4 = Rectangle(int(width_r4), int(height_r4))
print(r4.area)
