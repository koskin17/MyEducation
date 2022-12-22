"""
Замена элемента на правый максимум
Сложность: Лёгкая
Условие задачи: дан массив, необходимо заменить каждый элемент на максимальный из тех,
что находятся справа. В случае отсутствия такого элемента, используется -1.
Пример:
Ввод: arr = [17,18,5,4,6,1]
Вывод: [18,6,6,6,1,-1]
"""


def rightmax(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            arr[i] = -1
        else:
            arr[i] = max(arr[i + 1:len(arr)])

    return arr

# straight-forwarded, non optimal solution, O(n*n)
def replace_elements01(arr):
    l = len(arr)
    return [(max(arr[i+1:]) if i+1 < l else -1) for i in range(l)]


# back-forwarded, optimal solution, O(n)
def replace_elements02(arr):
    right_max = -1
    for i in range(len(arr)-1, -1, -1):
        prev_num = arr[i]
        arr[i] = right_max
        if prev_num > right_max:
            right_max = prev_num
    return arr

arr = [400]
print(rightmax(arr))
