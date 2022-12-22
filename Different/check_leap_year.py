# Проверка года на высокосность

while True:
    year = int(input("Укажите год: "))

    if (year % 400 == 0) and (year % 100 == 0):
        print(f"{year} - высокосный год")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} - это высокосный год")
    else:
        print(f"{year} - это не высокосный год")
