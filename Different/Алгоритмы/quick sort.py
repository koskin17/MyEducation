"""https://t.me/python2day/2534
Как и сортировка слиянием, быстрая сортировка использует подход «Разделяй и властвуй».
При правильной конфигурации он чрезвычайно эффективен и не требует дополнительной памяти,
в отличие от сортировки слиянием.
Массив разделяется на две части по разные стороны от опорного элемента.
В процессе сортировки элементы меньше опорного помещаются перед ним, а равные или большие - позади.

Алгоритм
Быстрая сортировка начинается с разбиения списка и выбора одного из элементов в качестве опорного.
А всё остальное передвигаем так, чтобы этот элемент встал на своё место.
Все элементы меньше него перемещаются влево, а равные и большие элементы перемещаются вправо."""


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


random_list_of_nums = [9, 3, 41, 67, 2, 19, 0, 84]
print(random_list_of_nums)
quick_sort(random_list_of_nums)
print("Список после сортировки:")
print(random_list_of_nums)

# [0, 2, 3, 9, 19, 41, 67, 84]
