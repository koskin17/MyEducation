"""
Chain можно использовать для перебора сразу нескольких последовательностей (итерируемых объектов)
и получения элемента из каждой последовательности по порядку.
Переход к следующей последовательности происходит при достижении конца предыдущей последовательности.
"""

from itertools import chain

lst_a = [1, 22]
lst_b = [3, 20, 30, 40, 55]
lst_c = [5]

for _ in chain(lst_a, lst_b, lst_c):
    print(_, end=" ")   # вывод элементов в одну строку благодаря наличию end=""

print()
print("Chain itself creates and returns the object - iterator")
sample = chain(lst_a, lst_b, lst_c)
print(sample)
print("For convert the object - iterator to the list is used list():")
print(list(sample))

# [1, 22, 3, 20, 30, 40, 55, 5]
