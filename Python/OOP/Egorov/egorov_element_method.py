class Cat:
    breed = 'pers'

    def hello(*args):
        print("Hello word from kitty", args)

    def show_breed(self):
        print(f'my breed is {self.breed}')

    def show_name(self):
        """Проверка наличия аттрибута"""
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print("Nothing")

        "Создание атрибутов класса при помощи метода"
    def set_value(self, value, age=0):
        self.name = value
        self.age = age


walt = Cat()
