from random import randint


def binary_search(lst, item):
    item = int(item)
    # в low и high хранятся границы части списка, где выполняется поиск
    low = 0
    high = len(lst) - 1
    attempt = 1
    # Пока не останется один элемент
    while low <= high:
        print(f"Попытка №{attempt}")
        # Проверяем средний элемент
        mid = (low + high) // 2
        guess = lst[mid]
        # Значение найдено
        if guess == item:
            return f"Число найдено - {item}"
        # Значение велико
        if guess > item:
            high = mid - 1
        # Значение мало
        else:
            low = mid + 1
        attempt = attempt + 1

    # Значение не найдено
    return "Значение не найдено"


while True:

    my_list = []
    len_list = input("Укажите длину списка: ")
    for i in range(int(len_list)):
        my_list.append(randint(1, int(len_list)))

    number = my_list[randint(0, int(len_list))]
    print("Случайное число для поиска: ", number)
    print(binary_search(sorted(my_list), number))
