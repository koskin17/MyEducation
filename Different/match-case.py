"""
Конструкция позволяет избавиться от громоздких условий и цепочек if - else:
http_status = 400
if http_status == 400:
    print("Bad Request")
elif http_status == 403:
    print("Forbidden")
elif http_status == 404:
    print("Not Found")
else:
    print("Other")

Вместо можно использовать match-case:
http_status = 400
match http_status:
    case 400:
        print("Bad Request")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case _:
        print("Other")

"""
from datetime import datetime
from enum import Enum

"Проверка дня недели """

week = {0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"}

day = week.get(datetime.isoweekday(datetime.now()))
print(f"Сегодня {day}")
print()

print("Вариант через if - else:")
if day == "Sunday":
    print("Take it easy")
elif day == "Monday":
    print("Go to work")
elif day == "Tuesday":
    print("Work + Hobbies")
elif day == "Wednesday":
    print("Meetings")
elif day == "Thursday":
    print("Presentations")
elif day == "Friday":
    print("Interviews and party")
elif day == "Saturday":
    print("Time to do sports")
"""
В данном случае используется много проверок одного выражения (обращение к переменной) day == ...
Правильно использовать метод match-case"""
print()
print("Вариант через match - case:")
match day:
    case "Sunday":
        print("Take it easy")
    case "Monday":
        print("Go to work")
    case "Tuesday":
        print("Work + Hobbies")
    case "Wednesday":
        print("Meetings")
    case "Thursday":
        print("Presentations")
    case "Friday":
        print("Interviews and party")
    case "Saturday":
        print("Time to do sports")

"""Конструкцию match-case можно использовать с различными шаблонами.
Шаблон литерал (literal) - это пример показан в варианте с днём недели.
Шаблон захвата (capture) - использовать для сохранения (захвата) совпавшего значения в переменную.
Пример - приветствие человека, если совпало его имя:"""


def greet(name=None):
    match name:
        case None:
            return "Приветствую, неизвестный человек!"
        case "Kostia":
            return f"Приветствую, {name}"


print()
print(greet())
print(greet(name="Kostia"))

"""Шаблон подстановки (wildcard).
При использовании выражения match-case можно применять знак подстановки для сопоставления,
без привязки к конкретному значению. При этом подстановка соответствует всему,
что не включено в выражения case. В некотором смысле подстановка — это блок else выражения match-case.
Для знака подстановки используется символ подчеркивания _.
Пример - проверка результата подбрасывания монеты"""
print()
print("Проверка результата подбрасывания монеты:")
# conflip = int(input("Введите 0 - Решка или 1 - Орёл: "))
conflip = 0
match conflip:
    case 0:
        print("Tails")
    case 1:
        print("Heads")
    case _:
        print("Must be 0 or 1.")

"""Подстановка, пример 2: есть коллекция, в которое не важны сами элементы, а важно их кол-во и что они существуют.
Проверяется размер кортежа, не рассматривая его содержимое"""
print()
location = (0, 0)
match location:
    case (_, ):
        print("1D location found.")
    case (_, _, ):
        print("2D location found.")
    case (_, _, _, ):
        print("3D location found.")

"""Шаблон постоянных значений (constant value) и перечисления.
В качестве значений case можно использовать элементы перечислений (enumerations).
Чтобы это продемонстрировать, создаётся класс перечисления Direction (унаследованный от класса Enum),
представляющий четыре основных направления на компасе.
После этого создаётся функция handle_directions(), которая принимает элемент класса Direction в качестве аргумента.
Эта функция сопоставляет аргумент с одним из направлений из перечисления и реагирует."""


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


def handle_direction(direction):
    match direction:
        case Direction.NORTH:
            print("Heading North")
        case Direction.EAST:
            print("Heading East")
        case Direction.SOUTH:
            print("Heading South")
        case Direction.WEST:
            print("Heading West")


print()
handle_direction(Direction.WEST)
# Шаблон последовательностей (sequence).
# Для сопоставления с заданным шаблоном можно использовать распакованные элементы различных
# последовательностей (коллекций).
directions = ["North", "East", "South", "West"]

# Grab the values from a list and store them into variables
n, e, s, w = directions
print(n)  # prints North
print(e)  # prints East
print(s)  # prints South
print(w)  # prints West
# Распаковку можно использовать вместе с выражением match-case.
# Проверка, является ли местоположение (переменная location) точкой 1D, 2D или 3D.
# Также сохраняются координаты в отдельных переменных в зависимости от количества измерений.
location = (1, 3)


def handle_direction2(var=location):
    match var:
        case x,:
            print(f"1D location found: ({x})")
        case x, y:
            print(f"2D location found: ({x}, {y})")
        case x, y, z:
            print(f"3D location found: ({x}, {y}, {z})")


print()
handle_direction2(location)
# Если в кортеже будет больше значений, то можно использовать оператор *.
# К примеру, в кортеже есть посторонние элементы: (1, 3, 2, "a", "b", "c").
# Чтобы отловить «лишние» элементы используется оператор *:
location = (1, 3, 2, "a", "b", "c")

match location:
    case x,:
        print(f"1D location found: ({x})")
    case x, y:
        print(f"2D location found: ({x}, {y})")
    case x, y, z, *names:
        print(f"3D location found: ({x}, {y}, {z})")
        print(f"Also, there was some extra data: {names}")


# Комбинирование шаблонов или сравнение сразу по нескольким шаблонам с оператором |(или)
day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Work")
