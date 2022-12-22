'''
Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

'''
array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]

def flatten_and_sort(array):
    new_array = []
    for x in range(len(array)):
         if array[x] == None:
               continue
         for y in range(len(array[x])):
                new_array.append(array[x][y])
    return sorted(new_array)

print(flatten_and_sort(array))


''' Второй вариант
Функция chain перебирает все итерируемые элементы в последовательности,
независимо от их количества и вложенности, пока последовательность и элементы не закончатся'''
from itertools import chain
def flatten_and_sort(array):
    return sorted((chain(*array)))
