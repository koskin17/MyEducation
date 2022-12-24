class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода!")

    def destroy(self):
        Robot.population -= 1
        print(f"Robot {self.name} was destroyed")

    @classmethod
    def how_many(cls):
        print(f"Robots population equals: {Robot.population}")


r2 = Robot("R2-D2")
print(Robot.population)
r2.say_hello()
Robot.how_many()
r2.destroy()
Robot.how_many()
print(Robot.population)
