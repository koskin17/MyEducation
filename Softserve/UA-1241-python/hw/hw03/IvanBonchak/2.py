namber_4 = 7653
namber_str = str(namber_4)
sum_n = 0
#sum of numbers
print(int(namber_str[0]) + int(namber_str[1]) + int(namber_str[2]) + int(namber_str[3]))
#- write the number in reverse order
r_namber = int(namber_str[::-1])

print(r_namber)
#- in ascending order, you need to sort the numbers included in the given number
f_namber = ''.join(sorted(namber_str))
print(r_namber)
