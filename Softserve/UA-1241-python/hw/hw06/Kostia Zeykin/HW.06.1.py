"""Task 1"""
odd_number = []
even_number = []
other_number = []

for i in range(1, 11):
    if i % 2 == 0:
        odd_number.append(str(i))
    elif i % 3 == 0:
        even_number.append(str(i))
    else:
        other_number.append(str(i))

print(f"Чётные числа в списке: {",".join(odd_number)}")
print(f"Нечётные числа в списке: {",".join(even_number)}")
print(f"Другие числа в списке: {",".join(other_number)}")

"""Task 2"""
login = input("Пожалуйста, введите ваш логин: ")

if login == "First":
    print(f"Приветствуем Вас, пользователь {login}")
else:
    print("Возникла ошибка - Вы указали неверный логин для входа.")
