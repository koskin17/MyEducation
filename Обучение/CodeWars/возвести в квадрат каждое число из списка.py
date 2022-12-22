numbers = list(input('Введите подряд несколько чисел: '))
def square_sum(numbers):
    summ = 0
    for number in numbers:
        summ += int(number)**2
    return summ

print(square_sum(numbers))

''' Второй вариант '''
def square_sum(numbers):
    return sum(int(n) ** 2 for n in numbers)

print(square_sum(numbers))
