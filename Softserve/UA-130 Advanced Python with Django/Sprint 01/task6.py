# Write a program that given an array of integers determines if it is sorted in "ascending" order, "descending" order or "not sorted" at all.

# Example

# For a = [10, 5, 4], the output should be
# order(a) = "descending";
# For a = [6, 20, 160, 420], the output should be
# order(a) = "ascending";
# For a = [1, 7, 0, 4, 8, 1], the output should be
# order(a) = "not sorted".
# [input] array.integer a

# 1 < a.length < 100, all of numbers are different

# [output] string

# "ascending", "descending" or "not sorted".

def order(a):
    if a == sorted(a):  # Проверяем, отсортирован ли массив по возрастанию
        return "ascending"
    elif a == sorted(a, reverse=True):  # Проверяем, отсортирован ли массив по убыванию
        return "descending"
    else:
        return "not sorted"

# Примеры:
print(order([10, 5, 4]))  # Выведет: "descending"
print(order([6, 20, 160, 420]))  # Выведет: "ascending"
print(order([1, 7, 0, 4, 8, 1]))  # Выведет: "not sorted"
