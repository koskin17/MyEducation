# Магические методы __len__ и __abs__

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)    # В этом случае автоматически вызывается магический метод abs,
                            # который описан ниже и выполнится его Return

    def __abs__(self):
        return abs(self.x2 - self.x1)


a = Person("Name", "Surname")
print(len(a))
b = Person("1", "23")
print(len(b))

ot1 = Otrezok(3, 9)
print(len(ot1))
ot2 = Otrezok(10, 2)
print(len(ot2))
