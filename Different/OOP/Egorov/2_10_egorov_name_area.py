# Пространство имён класса

class DepartmentIT:
    # Имена атрибутов класса не видны внутри методов экземпляра
    python_dev = 4
    go_dev = 3
    react_dev = 2

    # Методам при создании недоступны имена в области класса
    # При этом методы экземпляров класса имеют доступ к глобальной области переменных,
    # т.е. видят их в основной программе
    # Но через self. можно получить доступ к атрибутам класса:
    # - self.python_dev;
    # - self.go_dev;
    # - self.react_dev.

    def info(self):
        return self.python_dev, self.go_dev, self.react_dev

    # Также можно получить доступ через класс Department.python_dev
    def info2(self):
        return DepartmentIT.python_dev, DepartmentIT.go_dev, DepartmentIT.react_dev

    # Можно создать свойство
    @property
    def info_properties(self):
        return self.python_dev, self.go_dev, self.react_dev

    # Можно создать classmethod
    @classmethod
    def class_info(cls):
        return cls.python_dev, cls.go_dev, cls.react_dev

    # Можно создать staticmethod. Он ничего не принимает (ни экземпляры, ни классы)
    # Обращение к атрибутам класса происходит через имя класса
    @staticmethod
    def static_info():
        return DepartmentIT.python_dev, DepartmentIT.go_dev, DepartmentIT.react_dev

    def make_backend(self):
        print("Python and Go")

    def make_frontend(self):
        print("React")

    def hiring_pyth_dev(self):
        DepartmentIT.python_dev += 1
        return DepartmentIT.python_dev


it1 = DepartmentIT()
print("Доступ через параметр self: ", it1.info())
print("Доступ через имя класса: ", it1.info2())
print("Доступ через свойство property: ", it1.info_properties)
print("Доступ через classmethod: ", it1.class_info())
print("Доступ через staticmethod: ", it1.static_info())
it1.hiring_pyth_dev()
print(DepartmentIT.python_dev)
