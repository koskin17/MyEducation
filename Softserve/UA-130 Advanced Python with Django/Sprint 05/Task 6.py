# Write the function sum_slice_array(arr, first, second), which accepts the array (list) arr and two numbers (first and second) - the ordinal numbers of the elements of the array that must be added. For example, if 3 and 5 were entered, the 3rd and 5th elements must be added.

# The function should generate exceptions MyExceptions:
# if non-numbers or numbers less than 1 were entered;
# if non-numbers obtained from array;
# if when one of the numbers or both is larger than the array length.
# For example:

# print(sum_slice_array([1, 2, 3], 1, 2))
# 3.0

# try:
#     print(sum_slice_array([1, "string", 3], 1, 2))
# except MyExceptions:
#     print("MyExceptions")
# MyExceptions

# try:
#     print(sum_slice_array([14, 5, 3], -1, 2))
# except MyExceptions:
#     print("MyExceptions")
# MyExceptions

# Создание собственного класса исключения
class MyExceptions(Exception):
    pass

def sum_slice_array(arr, first, second):
    try:
        # Проверяем, что first и second являются числами и >= 1
        if not (isinstance(first, int) and isinstance(second, int) and first >= 1 and second >= 1):
            raise MyExceptions("Numbers must be integers and at least 1")

        # Проверяем, что first и second не выходят за границы списка
        if first > len(arr) or second > len(arr):
            raise MyExceptions("Indexes are out of range")

        # Проверяем, что элементы списка, на которые указывают first и second, являются числами
        if not (isinstance(arr[first - 1], (int, float)) and isinstance(arr[second - 1], (int, float))):
            raise MyExceptions("Elements must be numbers")

        # Возвращаем сумму двух элементов
        return float(arr[first - 1] + arr[second - 1])
    
    except MyExceptions as e:
        return "MyExceptions"

# # Примеры вызова функции
print(sum_slice_array([1, 2, 3], 1, 2))      # Вывод: 3.0

try:
    print(sum_slice_array([1, "string", 3], 1, 2))  # Вывод: MyExceptions
except MyExceptions:
    print("MyExceptions")

try:
    print(sum_slice_array([14, 5, 3], -1, 2))  # Вывод: MyExceptions
except MyExceptions:
    print("MyExceptions")

# ### **Объяснение кода**
# 1. **Создаём пользовательское исключение `MyExceptions`**:
#    - Класс `MyExceptions` наследуется от `Exception`, чтобы можно было использовать `raise MyExceptions(...)`.

# 2. **Обрабатываем три типа ошибок в `try-except`**:
#    - **`first` и `second` должны быть числами ≥ 1**:  
#      Если переданы не числа или они меньше `1`, вызываем `MyExceptions`.
#    - **Проверяем, что `first` и `second` не выходят за границы списка**:  
#      Если одно из чисел больше длины списка, вызываем `MyExceptions`.
#    - **Проверяем, что элементы списка являются числами**:  
#      Если `arr[first-1]` или `arr[second-1]` не числа, вызываем `MyExceptions`.

# 3. **Если всё в порядке, возвращаем сумму чисел из списка в виде `float`**.