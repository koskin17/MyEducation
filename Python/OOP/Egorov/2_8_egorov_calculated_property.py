class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        self.__side = new_side
        self.__area = None

    # В этом случае свойство property вычисляется каждый раз при вызове.
    # Для экономии ресурсов результат нужно запоминать в переменную, которая добавлена в метод __init__
    # и проверять, пустая ли это переменная или нет.
    # Если пустая, то выполянть действия. Если не пустая, то возвращать уже посчитанное значение
    @property
    def area(self):
        if self.__area is None:
            print("Calculated area:")
            self.__area = self.side ** 2

        return self.__area


a = Square(10)
print(a.area)
# В этом случае значение было передано, переменная self.__area была равна None и ответ поссчитан
# При повторном вызове метода area для объекта a выводится значение уже в переменной self.__area,
# т.е. без фразу Calculated area
print("Значение из кэша:", a.area)

b = Square(11)
print(b.area)
print("Значение из кэша:", b.area)
