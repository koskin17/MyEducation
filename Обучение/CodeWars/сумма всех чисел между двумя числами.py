''' Нужно найти сумму всех чисел, расположенных между двумя числами.
Если числа равны, то вернуть одно из них '''
import time
start_time = time.time()
a = -236
b = 0

def get_sum(a,b):
    a1 = 0
    b1 = 0
    summ = 0
    if b < a:
        a1 = b
        b1 = a
        while a1 <= b1:
            summ += a1
            a1 +=1
    else:
        while a <= b:
            summ += a
            a += 1
    return summ

print(get_sum(a,b))
print("--- %s seconds ---" % (time.time() - start_time))
''' Второй вариант '''
start_time = time.time()
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(a,b))
print("--- %s seconds ---" % (time.time() - start_time))
