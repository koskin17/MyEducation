# Given a string, check if its characters can be rearranged to form a palindrome. Where a palindrome is a string that reads the same left-to-right and right-to-left.

# Example

# "trueistrue" -> false;
# "abcab" -> true because "abcba" is a palindrome
# [input] string s (min 1 letters) 

# [output] boolean

# Мы можем решить эту задачу, используя подсчёт количества вхождений каждого символа. Идея следующая:
# - Для того, чтобы символы можно было переставить так, чтобы получилось палиндромом, почти все символы должны встречаться чётное число раз. Если длина строки нечётная, то может быть ровно один символ с нечётным числом вхождений (он будет центральным).
# - То есть, если количество символов с нечётной частотой больше одного, переставить символы в палиндром нельзя.
# Ниже приведён пример кода на Python:

from collections import Counter

def isPalindrome(str):
    # Подсчитываем частоту вхождений каждого символа
    freq = Counter(str)
    # Считаем, сколько символов встречаются нечетное число раз
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    # Палиндром возможен, если нечетных встречается не более 1
    return odd_count <= 1

# Примеры:
print(isPalindrome("trueistrue"))  # Выведет: False
print(isPalindrome("abcab"))       # Выведет: True