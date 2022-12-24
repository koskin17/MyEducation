# Полиморфизм - многоформенность
# Это говорит о том, что методы, одинаковые по названиям, ведут себя различным способом.

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, " is saying woof")


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, " is saying meow")


class Mouse:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, " is saying pee-pee-pee")


Spike = Dog("Spike")
Tom = Cat("Tom")
Jerry = Mouse("Jerry")

pet_list = [Spike, Tom, Jerry]

for pet in pet_list:
    pet.speak()

# Животное можно передать в виде параметра функции
# А в самой функции уже вызвать метод, но с указанием скобок ()


def pet_voice(pet):
    pet.speak()


pet_voice(Spike)
pet_voice(Tom)
pet_voice(Jerry)
