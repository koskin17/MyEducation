# Special magic method __method_name__
# Специальный или магические метода обозначаются двумя знаками подчеркивания.
# К примеру, метод __init__

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    # Переопределение метода str для получения информации про объект.
    # Согласно документации, метод str должен возвращать сроку.
    # Т.е. создаётся новый метод str, но его действия переопределяются нами.
    # В результате при печати объекта класса print(Jack) мы получаем то, что возвращаем методом str

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    # Переопределяет метод len() для объекта класса
    # Согласно документации он должен возвращать челочисленное значение.
    # В нашем случае мы будем возвращать возвраст человека.
    def __len__(self):
        return self.age

    # Переопределение метода del для удаления объекта так, чтобы было явно видно, что объект удалён
    def __del__(self):
        print("Person object with name", self.first_name, self.last_name, "was deleted from memory")


Jack = Person('Jack', 'White', 45)
print(len([1, 2, 3, 4, 5]))
print(Jack)
print(len(Jack))
# Jack.__del__
# или так
del Jack
