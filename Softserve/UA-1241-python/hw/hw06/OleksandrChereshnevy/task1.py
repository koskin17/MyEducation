# Task1. In the range from 1 to 10 determine 
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

l = list(range(1,10))
temp = list()

for i in l:
    if i % 2 == 0:
        temp.append(i)

print(f"Even numbers that are divisible by 2: {temp}")
temp.clear()

for i in l:
    if i % 2 != 0 and i % 3 == 0:
        temp.append(i)

print(f"Odd numbers, which are divisible by 3: {temp}")
temp.clear()

for i in l:
    if i % 2 != 0 and i % 3 != 0:
        temp.append(i)

print(f"Numbers that are not divisible by 2 and 3: {temp}")



