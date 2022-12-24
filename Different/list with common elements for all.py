"""
Условие:
Ваша задача — написать функцию, которая принимает неограниченное количество списков и возвращает только те элементы, что есть в каждом списке.

Пример:
find_values([11, 10, 3], [10, 3, 5, 11], [11, 10]) -> [11, 10]
find_values([8, 4, 7, "hi"], [8, "hi"], [4, "hi"]) -> ['hi']
find_values([1, 4, 3], [6, 2, 8], ["4", "hi"]) -> []
"""


def find_values(*args):
    set_tmp = set(args[0])
    for lst in args[1:len(args)]:
        set_tmp = set_tmp.intersection(set(lst))
    return list(set_tmp)


print(find_values([11, 10, 3], [10, 3, 5, 11], [11, 10]))
print(find_values([8, 4, 7, "hi"], [8, "hi"], [4, "hi"]))
print(find_values([1, 4, 3], [6, 2, 8], ["4", "hi"]))

# Второй вариант
from typing import Sequence


def find_values2(values: Sequence, *add_values: Sequence) -> list:
    return list(set(values).intersection(*add_values))


print(find_values2([11, 10, 3], [10, 3, 5, 11], [11, 10]))
print(find_values2([8, 4, 7, "hi"], [8, "hi"], [4, "hi"]))
print(find_values2([1, 4, 3], [6, 2, 8], ["4", "hi"]))
