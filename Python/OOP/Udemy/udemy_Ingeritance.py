class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print("Car is created")

    def drive(self, city):
        print(f"{self.name} is driving to the {city} and has {Car.wheels_number} weels")

    def change_color(self, new_color):
        self.color = new_color


class Truck(Car):
    wheels_number = 6
    print("Truck is created")

    def drive(self, city):
        print("Truck", self.name, "is driving to", city)

    def load_cargo(self, weight):
        print("The cargo is loaded. Weight is", str(weight), "kg")


man_truck = Truck('Man', 'white', 2015, False)
print(man_truck.name)
print(man_truck.color)
man_truck.change_color('blue')
print("Цвет грузовика изменён на", man_truck.color)
man_truck.drive("Dnepr")
print(man_truck.wheels_number)
man_truck.load_cargo(200)