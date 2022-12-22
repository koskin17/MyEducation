"""
Задача - сделать класс Точка.
"""
from math import sqrt


class Point:

    """Создание атрибута, распространяющегося на весь класс"""
    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f"Точка с координатами: {self.x}, {self.y}")

    "Метод работы с несколькими экземплярами"
    def calc_distance(self, another_point):

        """Сначала проверяем, что метод получил именно точку"""
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу \"Точка\"")
        else:
            print(sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2))


# p1 = Point()
# print(p1.__dict__)
# p1.move_to(4, 5)
# print(p1.__dict__)
# p1.go_home()
# print(p1.__dict__)
#
# p2 = Point()
# print(p2.__dict__)
# p2.print_point()
#
# p2.move_to(5, 5)
# p2.print_point()
#
p3 = Point(6, 0)
p4 = Point(0, 8)

"""Теперь можно вывести весь список точек в классе Points"""
p3.calc_distance(p4)
for point in Point.list_points:
    print(point.__dict__)
