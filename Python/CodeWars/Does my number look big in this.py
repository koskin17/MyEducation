"""
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits,
each raised to the power of the number of digits in a given base.
In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
"""


def narcissistic(value):
    summ = 0
    for i in str(value):
        summ += int(i) ** len(str(value))

    return True if summ == value else False


print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))


# Вариант 2
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
