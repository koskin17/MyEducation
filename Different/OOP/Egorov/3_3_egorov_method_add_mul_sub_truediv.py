# Магические методы __add__ __mul__ __sub__ __truediv__

class Vector:
    def __init__(self, *args):
        self.values = []
        for number in args:
            if isinstance(number, int):
                self.values.append(number)

    def __str__(self):
        if self.values:
            tmp = [str(i) for i in self.values]  # преобразование значений списка в строку
            return f"Вектор ({', '.join(tmp)})"
        else:
            return "Пустой вектор."

    def __add__(self, other):
        if isinstance(other, int):
            tmp = [i + other for i in self.values]  # увеличение всех значений списка на число
            """
            После этого новый список возвращается в виде объекта класса Vector.
            Для того, чтобы передался каждый элемент списка отдельно
            используется оператор распаковки "*" (звёздочка).
            """
            return Vector(*tmp)  # возвращается новый объект класса Vector
        elif isinstance(other, Vector):  # проверка, если в other - объект класса Vector
            if len(other.values) == len(self.values):  # проверка, если значение по длине в other равны values
                tmp = [sum(i) for i in zip(self.values, other.values)]
                return Vector(*tmp)
            else:
                print("Сложение векторов разной длины недопустимо.")
        else:
            return f"Вектор нельзя сложить с {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            tmp = [i * other for i in self.values]  # умножение всех значений списка на число
            """
            После этого новый список возвращается в виде объекта класса Vector.
            Для того, чтобы передался каждый элемент списка отдельно
            используется оператор распаковки "*" (звёздочка).
            """
            return Vector(*tmp)  # возвращается новый объект класса Vector
        elif isinstance(other, Vector):  # проверка, если в other - объект класса Vector
            if len(other.values) == len(self.values):  # проверка, если значение по длине в other равны values
                tmp = [i[0] * i[1] for i in zip(self.values, other.values)]
                return Vector(*tmp)
            else:
                print("Умножение векторов разной длины недопустимо.")
        else:
            return f"Вектор нельзя умножить на {other}"


a = Vector(1, 2, 43)
print("Вектор a: ", a)
d = a + 5
print("Добавляем к вектору число 5 и получаем новый вектор: ", d)
b = Vector(1, 2, 43)
print("Новый вектор b: ", b)
print(a + b)
c = Vector()
print("Если пустой вектор: ", c)
print(a+5.0)
print(a * 3)
print(a * "я")

