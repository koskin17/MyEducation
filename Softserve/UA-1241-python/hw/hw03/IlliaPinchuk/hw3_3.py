def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

a = input("Enter a: ")
while not is_number(a):
    print("Please enter a valid number.")
    a = input("Enter a: ")

b = input("Enter b: ")
while not is_number(b):
    print("Please enter a valid number.")
    b = input("Enter b: ")

a, b = b, a

print("a: ", a)
print("b: ", b)
