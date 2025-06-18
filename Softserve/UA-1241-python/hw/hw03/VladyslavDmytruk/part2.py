number = 12345678

number_digits = 1
for digit in str(number):
    number_digits *= int(digit)

reversed_number = int(str(number)[::-1])

print("Product of digits of the number:", number_digits)
print("Reversed number:", reversed_number)

