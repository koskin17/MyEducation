def productOfNumber(number):
    product = 1
    for i in number:
        product *= int(i)
    return product

def reverseOrderOfNumber(number):
    return str(number)[::-1]

def sortNumber(number):
    return ''.join(sorted(str(number)))

def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

number = input("Enter a number: ")
while not is_number(number):
    print("Please enter a valid number.")
    number = input("Enter number: ")

print("Product of the number: ", productOfNumber(number))
print("Reverse order of the number: ", reverseOrderOfNumber(number))
print("Sorted number: ", sortNumber(number))