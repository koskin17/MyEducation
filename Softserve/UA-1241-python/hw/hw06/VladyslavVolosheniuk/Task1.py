#Task1. In the range from 1 to 10 determine
#even numbers that are divisible by 2,
#odd numbers, which are divisible by 3,
#numbers that are not divisible by 2 and 3.

even = [x for x in range(11) if x % 2 == 0] 
print(f"Even numbers that are divisible by 2(from 1 to 10): {even}")

odd = [x for x in range(11) if x % 2 == 1 and x % 3 == 0] 
print(f"Odd number, witch are divisible 3(from 1 to 10): {odd}")

numbers = [x for x in range(11) if x % 2 != 0 and x % 3 != 0]
print(f"Numbers that are not divisible by 2 and 3(from 1 to 10): {numbers}")

