# Магические методы __eq__ и __hash__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """
    Метод __hash__ есть у неизменяемых объектов,
    но его нет у изменяемых объектов.
    Если переопределяется метод __eq__, то теряется метод __hash__ у объекта.
    В этом случае объект нельзя сохранить в качестве ключа словаря.
    Для этого метод __hash__ нужно переопределить."""
    def __eq__(self, other):
        return isinstance(other, Point) and \
               self.x == other.x and \
               self.y == other.y

    def __hash__(self):
        """Возвращается hash функции от нашего кортежа, который состоит из координат."""
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
print("У точек разные id: ")
print(id(p1))
print(id(p2))
print("Однако точки между собою равны: p1 == p2? \n", "Ответ: ", p1 == p2)
p3 = Point(3, 4)
p4 = Point(3, 4)
p5 = Point(30, 40)
print("Проверка равенства точек / объектов.")
print("Равно ли p3 и p4? ", p3 == p4)
print("Равно ли p3 и p5? ", p3 == p5)
print("Hash-значения точек:")
print("- точка p3: hash - ", hash(p3))
print("- точка p4: hash - ", hash(p4))
print("У этих точек равны координаты, т.е. они равны по функции hash,\
которую мы переопределили и она сравнивает по координатам.")
print("- точка p5 имеет другие координаты и её hash равен: hash - ", hash(p5))
# Теперь можно создать словарь и его ключами могут быть наши экземпляры
example_dict = dict()
example_dict[p3] = 100
example_dict[p5] = 200
for key, value in example_dict.items():
    print("Ключами словаря стали объекты:")
    print(str(key) + ":" + str(value))
