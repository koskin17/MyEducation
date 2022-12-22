lst, n_largest_elements = [-17,-8,-102,-309],2

def max_product(lst, n_largest_elements):
    maxlst = []
    for number in range(0, n_largest_elements):
        maxlst.append(lst.pop(lst.index(max(lst))))

    n_largest_elements = 1
    for number in maxlst:
        n_largest_elements *= number

    return n_largest_elements

print(max_product(lst, n_largest_elements))

''' Второй вариант.
В нёмЖ
- функцией nlargest выбирается n максимальных элементов из последовательности;
- функция reduse применяет функцию mul (умножение) ко всем
элементам последовательности nlargest,
т.е. перемножает их и возвращает результат'''
from functools import reduce
from operator import mul
from heapq import nlargest

def maxProduct (lst, n):
    return reduce(mul, nlargest(n, lst))

''' Третий вариант.
Формируется список из необходимого числа чисел из
отсортированного списка и потом эти числа перемножаются'''
def max_product(lst, n_largest_elements):
    lst_largest = sorted(lst)[-n_largest_elements:]
    prod = 1
    for number in lst_largest:
        prod *= number
    return prod
