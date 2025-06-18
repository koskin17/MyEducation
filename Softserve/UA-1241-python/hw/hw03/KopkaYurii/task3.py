a = int(input("Enter value to a: "))
b = int(input("Enter value to b: "))

print(f"Original: a = {a}, b = {b}")

a, b = b, a

print(f"Swapped: a = {a}, b = {b}")
