'''
Получено 2 числа.
Нужно певрое по очереди умножить на все цифры по порядку
в пределах от 1 от второго числа
'''

def count_by(x, n):
    sequence = []
    for i in range(1, n+1):
        sequence.append(x*i)
    return sequence

print(count_by(2, 5))

''' Второй вариант '''
def count_by2(x, n):
    return [i * x for i in range(1, n + 1)]

print(count_by2(2, 5))
