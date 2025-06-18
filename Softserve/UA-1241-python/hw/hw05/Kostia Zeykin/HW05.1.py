"""Task 1"""

start_list = []
for number in range(20):
    start_list.append(number)

end_list = []
for element in start_list:
    end_list.append(float(element))

print(end_list)

"""Task 2"""
number = int(input("Укажите число, до которого Вы хотите рассчитать число Фибоначчи: "))
list_fibonacci = [0, 1]

for i in range(2, number+1):
    list_fibonacci.append(list_fibonacci[i-2] + list_fibonacci[i-1])

print(list_fibonacci)

"""Task 3"""
number = int(input("Укажите число для расчёта его факториала: "))

if number == 0 or number == 1:
    print(f"Факториал числа {number} равен: 1")
elif number == 2:
    print(f"Факториал числа {number} равен: 2")
else:
    factorial = 1
    for i in range(1, number+1):
        factorial *= i

    print(f"Факториал числа {number} равен: {factorial}")
