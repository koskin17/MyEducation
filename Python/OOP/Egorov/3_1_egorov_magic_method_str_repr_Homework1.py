class Person:

    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value == "female":
            self.__gender = value
        else:
            print("Я не понимаю, что Вы имеете в виду. \n Пусть это будет мальчик.")
            self.__gender = "male"

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.gender}"


p1 = Person("Chuck", "Norris")
print(p1)
p2 = Person("Mila", "Kunis", "female")
print(p2)
p3 = Person("Оби-Ван", "Кеноби", "True")
print(p3)
