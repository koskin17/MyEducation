import random

number = random.randrange(1000, 10000)

print(F"Your number is: {number}\n")

print("The product of the digits of this number:")
list_number = [int(i) for i in str(number)]
result = 0;
for i in list_number:
    result += i
print(f"Result: {result}\n")

print("The number in reverse order:")
for i in range(-1, -5, -1):
    print(list_number[i], end="")

print("\n\nThe sort numbers included in the number:")
i = -1
while i < len(list_number)-1:
    i += 1
    if (i < 3) and (list_number[i] > list_number[i + 1]):
        list_number[i], list_number[i+1] = list_number[i+1], list_number[i]
        i = -1
print(list_number)


