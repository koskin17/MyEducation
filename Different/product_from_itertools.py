# https://pythonworld.ru/moduli/modul-itertools.html

from itertools import product

# Модуль product in itertools позволяет заменить вложенные циклы
for x, y in product('ABCD', 'xy'):
    print(x, y)  # --> Ax Ay Bx By Cx Cy Dx Dy

# Также его можно использовать для проверки последовательностей на выполнение условия

list_a = [1, 2020, 7]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

# К примеру, нужно получить числа, сумма которых равна определенному числу
for a, b, c, in product(list_a, list_b, list_c):
    if a + b + c == 75:
        print(f"Сумма 75 складывается из чисел: {a, b, c}")

    if a + b + c == 8:
        print(f"Сумма 8 складывается из чисел: {a, b, c}")

    if a + b + c == 4090:
        print(f"Сумма 4094 складывается из чисел: {a, b, c}")

    if a + b + c == 2008:
        print(f"Сумма 2008 складывается из чисел: {a, b, c}")
