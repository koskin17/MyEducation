class Vector:

    def __init__(self, *args):
        self.values = []
        for number in args:
            if isinstance(number, int):
                self.values.append(number)

    def __str__(self):
        if not self.values:
            return "Пустой вектор"
        else:
            return f"{', '.join(map(str, sorted(self.values)))}"


v1 = Vector(1, 7, 9, 4.5, 6.0, 2, 19, 3, 5.5)
print(v1)
v2 = Vector()
print(v2)
