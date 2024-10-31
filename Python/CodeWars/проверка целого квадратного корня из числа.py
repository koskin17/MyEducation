''' Надо проверить, является ли квадратный корень из числа
целым числом'''

n = int(input('Введите число: '))

from math import sqrt

def is_square(n):    
    if n < 0:
        return False
    elif n == 0:
        return True
    elif sqrt(n) / int(sqrt(n)) > 1:
        return False

    else:
        return True

is_square(n)
