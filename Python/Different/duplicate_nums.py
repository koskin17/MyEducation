"""Напишите функцию, которая будет принимать список nums,
содержащий числа в диапазоне от 1 до 100, и возвращать отсортированный список чисел,
которые в списке nums встречались дважды.

Примеры:
duplicate_nums([1, 2, 3, 4, 3, 5, 6])
➞ [3]

duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54])
➞ [72, 81, 99]

duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
➞ None

Примечания:
- никакое число не будет встречаться в nums трижды и более раз,
- если никакое число в nums не встречалось дважды, функция должна вернуть None.
"""
from collections import Counter

def duplicate_nums(list_with_number):
    duplicat_list = []
    duplicat = Counter(list_with_number)
    for number, amount in duplicat.items():
        if amount >= 2:
            duplicat_list.append(number)


    return sorted(duplicat_list)


print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Вариант 2
def duplicate_nums(list_with_number):
    duplicates = Counter(list_with_number)

    lst = sorted(num for num, amount in duplicates.items() if amount >= 2)
    return lst or []


print()
print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
