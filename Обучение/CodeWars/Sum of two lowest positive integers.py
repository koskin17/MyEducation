'''
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''

numbers = [19, 5, 42, 2, 77]

def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.pop(numbers.index(min1))
    min2 = min(numbers)
    return min1+min2

print(sum_two_smallest_numbers(numbers))


''' Второй вариант.
В нём список сортируется по возрастанию и ссумируются первые два
элемента в начале, которые и есть самые маленькие '''

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
