import random

number = random.randrange(1000, 9999)

print(f"Random number: {number}\n")

list_number = [int(i) for i in str(number)]
product = 1
for i in list_number:
    product *= i
print(f"The product of the digits of this number: {product}\n")

reversed_number = ''.join(str(i) for i in list_number[::-1])
print(f"The number in reverse order: {reversed_number}\n")

sorted_number = ''.join(str(i) for i in sorted(list_number))
print(f"The digits sorted in ascending order: {sorted_number}")




##