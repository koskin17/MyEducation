# Множественное наследование

class Swimmable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello! My name is {self.name} and I can swim")


class Walkable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello! My name is {self.name} and I can walk")


class Flyable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello! My name is {self.name} and I can fly")


class GameCharacter(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

    def greeting(self):
        print(f"Hello! My name is {self.name}")


James = GameCharacter('James')
James.greeting()
# В этом случае срабатываем метод __init__ класса Swimmable потому-что этот класс стоит первым в параметрах наследования
# в строке 27
# Методы __init__ в методе __init__ класса GameCharacter срабатывают в том порядке, в котором они написаны


# проверка функций isinctance является ли James объектов класса Walkable
print(isinstance(James, Walkable))
print(isinstance(James, Walkable))
print(isinstance(James, Swimmable))
print(isinstance(James, Flyable))

# В Python существует общий класс Object и все типы данных в Python являются объектами этого общего класса
