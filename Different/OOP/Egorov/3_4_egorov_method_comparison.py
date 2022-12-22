# Магические методы сравнения:
# __eq__ - (сокращение от equal) отвечает за ==
# __ne__ - (сокращение от not equal)отвечает за !=
# __lt__ - (сокращение от less than) отвечает за <
# __le__ - отвечает за <=
# __qt__ - отвечает за >
# __qe__ - отвечает за >=

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print("Вызвался метод __eq__")
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print("Вызвался метод __lt__")
        """В данном случае сравниваются по площади.
        Для этого создаём свойство property - area, которое возвращает площадь треугольника.
        Теперь вызываем property area у self и спрашиваем, меньше ли оно, чем у other"""
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):  # проверка, является ли other числом, т.е. int или float
            return self.area < other

    def __le__(self, other):
        print("Сработал метод __le__")
        """
        В данном случае при сравнении self = other сработает магический метод __eq__, гд подхватывается
        сравнение Rectangle.
        Если они не равны, т.е. self == other вернёт False, то выполнится проверка на знак меньше,
        т.е. вызовется метод __lt__
        """
        return self == other or self < other


r1 = Rectangle(1, 2)
r2 = Rectangle(1, 2)
print(r1 == r2)

r3 = Rectangle(10, 2)
print(r3 == r1)

print(r1 < r3)
print(r1 > r3)
# Проверка методом __le__
r4 = Rectangle(4, 5)
r5 = Rectangle(4, 5)
print(r4 <= r5)

r6 = Rectangle(1, 2)
print(r6 <= r5)
