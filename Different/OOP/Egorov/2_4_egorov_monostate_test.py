class Cat:
    __common_attr = {
        'breed': 'siam'
    }

    def __init__(self, color, name):
        self.__dict__ = Cat.__common_attr
        self.color = color
        self.name = name


a1 = Cat('black', 'Tom')
print(a1.__dict__)
a2 = Cat('yellow', 'Bob')
print(a2.__dict__)
