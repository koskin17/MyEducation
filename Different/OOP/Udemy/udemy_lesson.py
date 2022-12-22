# class Car:
#     """ Можно создать атрибут для каждого объекта класса вне метода
#     Для этого без метода __init__ прописывается атрибут.
#     И при создании объекта этот атрибут не нужно передавать.
#     Обращаться к атрибуту класса можно не через объект класса, а через сам класс
#     """
#     wheels_number = 4

#     def __init__(self, name, color, year, is_crashed):
#         """Создание атрибутов для каждого создаваемого объекта"""
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed

#     def drive(self, city):
#         print(f"{self.name} is driving to the {city} and has {Car.wheels_number} weels")

#     def change_color(self, new_color):
#         self.color = new_color


# mazda_car = Car(name="Mazda CX7", color="red", year=2017, is_crashed=True)
# bmw_car = Car(name="Bmw X7", color="black", year=2018, is_crashed=False)
# print(mazda_car.name, mazda_car.color, mazda_car.year, mazda_car.is_crashed, mazda_car.wheels_number)

# """"Обращаемся к атрибуту класса через сам класс
# Указываемся имя класса + точка (.) + имя атрибута"""

# numbers_of_wheels_of_3_cars = Car.wheels_number * 3
# print('Кол-во колёс у трёх машин - ', numbers_of_wheels_of_3_cars)

# print()
# print(bmw_car.name)
# print(bmw_car.color)
# print(bmw_car.year)
# print(bmw_car.is_crashed)
# print(bmw_car.wheels_number)

# """При создании объекта класса значения атрибутов можно записывать через запятую."""
# opel_car = Car('Opel Tigra', 'grey', 1999, True)
# opel_car.drive("London")
# bmw_car.drive("Dnepr")
# mazda_car.drive("Paris")
# """Также можно обратиться к методу класса и указать объект"""
# Car.drive(opel_car)

# изменение цвета объекта
# mazda_car.change_color('blue')
# print(f"Mazda изменила цвета на {mazda_car.color}")

# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def get_area(self):
#         return self.pi * (self.radius ** 2)
#
#     def get_circum_ference(self):
#         return 2 * self.pi * self.radius
#
#
# circle_1 = Circle()
# print(circle_1.get_area())
# print(circle_1.get_circum_ference())
# print()
#
# circle_1 = Circle(3)
# print(circle_1.get_area())
# print(circle_1.get_circum_ference())
# print()
#
# circle_1 = Circle(5)
# print(circle_1.get_area())
# print(circle_1.get_circum_ference())
# print()

def log_out():
    Gamer.active_gamers -= 1


class Gamer:
    """
    Для фиксации кол-во игроков в игре создаётся атрибут уровня класса
    """
    active_gamers = 0
    """
    Создание метода уровня класса. Он возвращает кол-во всех игроков.
    К нему обращаются через этот метод и делается это при помощи декораторов
    """
    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    """
    Создание игроков из строки через метод класса
    """
    @classmethod
    def gamers_from_string(cls, data_sring):
        nickname, age, level, points = data_sring.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        """
        При инициализации нового игрока атрибут класса active_gamers увеличивается на один 
        """
        Gamer.active_gamers += 1

    """
    При выходе из игры кол-во активных игроков уменьшается
    """

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    """
    Функция проверки возраста и, если >= 18, то выводится на печать, что можно перейти на более взрослый уровень
    """
    def get_adult_level_permisson(self):
        if self.is_adult():
            print("You can go to adult level")
        else:
            print("You cann't go to adult level")

# """
# Создаётся объект класса
# """
# print("Кол-во игроков вначале", Gamer.active_gamers)
# gamer_1 = Gamer('helloy_boy', 23, 5, 13)
# gamer_2 = Gamer('harry_potter', 13, 7, 34)
# """
# Получение атрибута при помощи геттера
# """
# print(gamer_1.get_age())
# gamer_1.get_adult_level_permisson()
#
# print(gamer_2.get_age())
# gamer_2.get_adult_level_permisson()
# print("Теперь кол-во игроков", Gamer.active_gamers)
#
# print("Для примера, gamer_1 вышел из игры и для него был вызван метод log_out")
# gamer_1.log_out()
#
# print("Теперь игроков", Gamer.active_gamers)
# print()
# Gamer.get_active_gamers()

# James = Gamer.gamers_from_string('James, 34, 2, 45')
# Jane = Gamer.gamers_from_string('Jane, 30, 5, 35')
# print(James.get_age())
# print(Jane.get_level())
# print(Gamer.get_active_gamers())

# my_dict = dict.fromkeys((1, 2, 3), ("apple", "orange", "banana"))
# print(my_dict)
