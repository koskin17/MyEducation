class Cat():
    def __init__(self, name):
        self.name = name

furball = Cat('Grumpy')
print('Our latest addition: ', furball.name)
a_cat = Cat("Mr. Fuzzybuttons")
print(a_cat.name)

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):        # так обозначается наследование класса
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)
print()
print(person.name)
print(doctor.name)
print(lawyer.name)

class Animal:
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass


''' Родительский класс - примесь'''
class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()
