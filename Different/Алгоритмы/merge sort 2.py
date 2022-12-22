"""Merge Sort - сортировка слиянием

Алгоритм
Сортировка слиянием - элегантный пример использования подхода «Разделяй и властвуй».
Он состоит из двух этапов:

1. Несортированный список последовательно делится на N списков,\
    где каждый включает один «несортированный» элемент, а N — это число элементов в оригинальном
    массиве.
2. Списки последовательно сливаются группами по два, создавая новые отсортированные списки
до тех пор, пока не появится один финальный отсортированный список."""


def merge_sort(my_arr):
    # Последнее разделение массива
    if len(my_arr) <= 1:
        return my_arr
    mid = len(my_arr) // 2
    # Выполняем merge_sort рекурсивно с двух сторон
    left, right = merge_sort(my_arr[:mid]), merge_sort(my_arr[mid:])

    # Объединяем стороны вместе
    return merge(left, right, my_arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Сортируем каждый и помещаем в результат
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


print("Список перед сортировкой:")
my_arr = [9, 3, 41, 67, 2, 19, 0, 84]
print(my_arr)
print("Список после сортировки:")
print(merge_sort(my_arr))
