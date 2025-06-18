num = input("Write 4 numbers:")
str = str(num)

# Sum 

print("Sum number:", int(str[0]) + int(str[1]) + int(str[2]) + int(str[3]))

# Write the number in reverse order

revers_num = int(str[::-1])
print("Revers number:", revers_num)

# Interchange the values of two variables without using the third variable.

sort_num = ''.join(sorted(str))
print("Sort number:",sort_num)

