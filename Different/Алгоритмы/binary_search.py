def binary_search(lst, item):
    # в low и high хранятся границы части списка, где выполняется поиск
    low = 0
    high = len(lst) - 1
    i = 0
    # Пока не останется один элемент
    while low <= high:
        # Проверяем средний элемент
        mid = (low + high) // 2
        guess = lst[mid]
        # Значение найдено
        if guess == item:
            return mid
        # Значение велико
        if guess > item:
            high = mid - 1
        # Значение мало
        else:
            low = mid + 1
        i = i + 1

    # Значение не найдено
    return None


my_lst = [1, 3, 5, 7, 9]
print(binary_search(my_lst, 5))  # => 2 (позиция элемента в списке)

# 'None' в Python означает "ничто". Элемент не найден.
print(binary_search(my_lst, 9))  # => 4 позиция элемента
