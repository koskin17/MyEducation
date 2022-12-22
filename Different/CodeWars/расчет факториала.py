n = 6
range(0, 5, -1)
def factorial(n):
    fact = 1
    if n < 0:
        return False
    if type(n) == type(1.2):
        return False
    for i in range(n, 0, -1):
        fact = fact * i
    return fact

print(factorial(n))

''' Второй вариант '''
from math import factorial

''' Третий вариант '''
def factorial(n):
    j = 1
    for i in range(1, n+1):
       j *= i
    return j   
