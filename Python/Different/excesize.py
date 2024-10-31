# a = 0
# def func():
#     global a
#     for num in [2, 4, 8]:
#         a += 1
#         yield num * 0.5
        
# array = []
# for val in func():
#     array.append(int(a == val))
# print(sum(array))

# a = 1; b = 2
# print(eval('print(a + b, end=" ") or 0'))

# class A:
#     def __iter__(self):
#         yield from range(10)
# a = A()
# print(5 in a, 20 in a)

# import re
# sent = 'Hello, Ben! How are you doing?'
# """split разбивает на 4 части строку.
#     Filter, если первый параметр None, просто оставит те элементы, которые возвращают true.
#     Пустая строка возвращает False"""
# lister = filter(None, re.split("[,!?]+", sent))
# print(re.split("[,!?]+", sent))
# print(len(list(lister)))

from itertools import product
a = [1, 2]
b = [3, 4]
"""Product создаёт кортежи всевозможных пар, беря по очереди:
    первый из а и первый из b,
    потом первый из а, второй из b.
    Потом второй из а, первый из b и т.д.
    
    При этом создаётся объект в памяти.
    Для его получения нужно его преобразовать в список, кортеж и т.д.
    """
# print(f"Список кортежей: {list(product(a, b))}")
# print(f"Кортеж кортежей: {tuple(product(a, b))}")
# print(f"Множество кортежей: {set(product(a, b))}")
# cort = tuple(product(a, b))
# print(sum(sum(cort, (0,))))

