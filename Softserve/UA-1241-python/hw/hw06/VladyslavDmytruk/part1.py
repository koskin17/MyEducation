# Task 1: in the range from 1 to 10 determine
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.
numbers = range(1, 11)

div_1 = [num for num in numbers if num % 2 == 0]
div_2= [num for num in numbers if num % 3 == 0 and num % 2 != 0]
div_3_and_3 = [num for num in numbers if num % 2 != 0 and num % 3 != 0]

print("Even numbers divisible by 2:", div_1)
print("Odd numbers divisible by 3:", div_2)
print("Numbers not divisible by 2 and 3:", div_3_and_3)

