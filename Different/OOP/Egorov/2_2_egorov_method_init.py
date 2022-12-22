class Cat:

    def __init__(self, name='Just cat', breed='pers', age=1, color='white'):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        print(self.__dict__)
        print("Cat is made!")


tom = Cat('Tom', 'siam', 30, 'black')
jerry = Cat('Jerry')
kelly = Cat('Kelly', 'siam', 5, 'blue')
misha = Cat()
