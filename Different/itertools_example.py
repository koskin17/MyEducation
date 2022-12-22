"""
Модуль itertools — это стандартная библиотека,
содержащая несколько функций, полезных в функциональном программировании.
Один из типов функций, которые он производит, — это бесконечные итераторы.
Функция count бесконечно увеличивает значение.
Цикл cycle бесконечно перебирает итерируемый объект (например, список или строку).
Функция repeat повторяет объект либо бесконечно, либо определенное количество раз.

takewhile - берет элементы из итерации, пока функция остается истинной;
chain - объединяет несколько итераций в одну длинную;
accumulate - возвращает промежуточную сумму значений в итерации.
"""
from itertools_example import accumulate, takewhile

nums = list(accumulate(range(10)))                   
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))
'''
============================================================================================
'''
from itertools_example import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))     # формирует все возможные комбинации букв и цифр в указанном пределе
print(list(permutations(letters)))          # формирует все возможные комбинации букв из списка

'''
============================================================================================
'''

from itertools_example import permutations

items = ['x', 'y']
print(list(permutations(items)))


def print_nums(x):
    for i in range(x):
        print(i)
    return


print_nums(10)
