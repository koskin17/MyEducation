class City:
    def __init__(self, city_name):
        self.name = city_name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in "aeiou"


p1 = City("new york")
print(p1)
print(bool(p1))
p2 = City("SaN frANCISco")
print(p2)
print(p2 == True)
