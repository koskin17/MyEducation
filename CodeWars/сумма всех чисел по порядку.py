'''
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
'''

num = int(input('Введите число: '))

def summation(num):
    summ = 0
    for i in range(num+1):
        summ += i
    return summ

print(summation(num))

''' Второй способ '''

def summation(num):
    return sum(range(num+1))

print(summation(num))
