'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
'''

number = int(input('Введите число: '))

def solution(number):
    summ = 0
    for figure in range(number):
        if figure < 0:
            return 0
        if figure %3 == 0 or figure %5 == 0:
            summ += figure
    return summ

print(solution(number))

''' Второй вариант
В этом варианте цикл из предыдещго вариант записан в одну строку,
а сумма считается сразу функцией sum'''
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
