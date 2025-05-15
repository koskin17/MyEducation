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
    # try:
        # Проверяем, что first и second являются числами и >= 1
    if not (isinstance(first, int) and isinstance(second, int) and first >= 1 and second >= 1):
        raise MyExceptions("Numbers must be integers and at least 1")

    # Проверяем, что first и second не выходят за границы списка
    if first > len(arr) or second > len(arr):
        raise MyExceptions("Indexes are out of range")

    # Проверяем, что элементы списка, на которые указывают first и second, являются числами
    if not (isinstance(arr[first - 1], (int, float)) and isinstance(arr[second - 1], (int, float))):
        raise MyExceptions("Elements must be numbers")
    # except MyExceptions as e:
    #     return "MyExceptions"
    
    # Возвращаем сумму двух элементов
    return float(arr[first - 1] + arr[second - 1])
    
    

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

# 1. ✅ Створено **власний клас виключення `MyExceptions`**.
# 2. ✅ Усі умови задачі покриті:
#    * Перевірка, що індекси — цілі та ≥ 1.
#    * Перевірка, що індекси не виходять за межі списку.
#    * Перевірка, що обрані елементи — числа (`int` або `float`).
# 3. ✅ Повертається сума у форматі `float`.
# 4. ✅ Повертає `"MyExceptions"` при помилці, що відповідає прикладу.

# ## ⚠️ **Що можна покращити:**
# ### 1. ❗️ Погане використання `try-except`:
# * Виняток `MyExceptions` викликається в `try`, і потім у цьому ж `except` він перехоплюється та перетворюється на строку `"MyExceptions"`.
# * Це **порушує принцип**: якщо виняток кидається — його повинен обробити **викликаючий код**, а не глушити сам `sum_slice_array`.

# 📌 **Згідно задачі**, **виклик** повинен виглядати так:
# try:
#     print(sum_slice_array([...], ..., ...))
# except MyExceptions:
#     print("MyExceptions")

# А не щоб функція повертала рядок `"MyExceptions"`.

# ## 🛠️ **Поліпшене рішення (правильне з точки зору Python-практики):**
# # Власний клас винятку
# class MyExceptions(Exception):
#     pass

# def sum_slice_array(arr, first, second):
#     # Перевірка: цілі числа ≥ 1
#     if not (isinstance(first, int) and isinstance(second, int) and first >= 1 and second >= 1):
#         raise MyExceptions("Indexes must be integers ≥ 1")

#     # Перевірка: індекси не виходять за межі масиву
#     if first > len(arr) or second > len(arr):
#         raise MyExceptions("Indexes out of range")

#     # Перевірка: елементи — числа
#     elem1 = arr[first - 1]
#     elem2 = arr[second - 1]
#     if not (isinstance(elem1, (int, float)) and isinstance(elem2, (int, float))):
#         raise MyExceptions("Elements must be numeric")

#     # Обчислення та повернення
#     return float(elem1 + elem2)

# ## ✅ **Як правильно викликати функцію:**
# print(sum_slice_array([1, 2, 3], 1, 2))
# # ➞ 3.0

# try:
#     print(sum_slice_array([1, "string", 3], 1, 2))
# except MyExceptions:
#     print("MyExceptions")
# # ➞ MyExceptions

# try:
#     print(sum_slice_array([14, 5, 3], -1, 2))
# except MyExceptions:
#     print("MyExceptions")
# # ➞ MyExceptions

# ## 🔍 **Чому так краще:**

# | Оригінал                    | Покращено                                     |
# | --------------------------- | --------------------------------------------- |
# | Виняток глушиться у функції | Виняток піднімається і правильно обробляється |
# | Повертається рядок          | Повертається значення або виникає виняток     |
# | Суперечить принципу SRP     | Дотримано принципів чистого коду              |

# * 🛠️ Уточнений варіант дозволяє:

#   * **відокремити логіку обробки помилок**;
#   * забезпечити **гнучкість** у використанні;
#   * **використовувати `try-except` там, де треба**, а не в середині самої функції.

# Логування — це важливий інструмент для **відлагодження** та **моніторингу** роботи програм.
# Давай покажу, як додати **логування в `sum_slice_array`**, щоб воно:
# * фіксувало всі перевірки;
# * записувало винятки;
# * повідомляло, що функція відпрацювала успішно.

# ## ✅ **1. Базове логування через модуль `logging`**
# import logging

# # Налаштування логування
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename='sum_slice_array.log',  # лог-файл
#     filemode='w'  # перезапис при кожному запуску
# )

# # Власний виняток
# class MyExceptions(Exception):
#     pass

# def sum_slice_array(arr, first, second):
#     logging.info(f"Function called with arr={arr}, first={first}, second={second}")

#     if not (isinstance(first, int) and isinstance(second, int) and first >= 1 and second >= 1):
#         logging.error("Invalid indexes: must be integers ≥ 1")
#         raise MyExceptions("Indexes must be integers ≥ 1")

#     if first > len(arr) or second > len(arr):
#         logging.error("Indexes out of range")
#         raise MyExceptions("Indexes out of range")

#     elem1 = arr[first - 1]
#     elem2 = arr[second - 1]
#     if not (isinstance(elem1, (int, float)) and isinstance(elem2, (int, float))):
#         logging.error(f"Invalid elements: {elem1} or {elem2} are not numeric")
#         raise MyExceptions("Elements must be numeric")

#     result = float(elem1 + elem2)
#     logging.info(f"Sum calculated successfully: {result}")
#     return result

# ## 🔍 **Як працює:**
# * 📦 `logging.basicConfig(...)` — налаштовує журналювання:
#   * рівень — `INFO` (можна змінити на `DEBUG`, `ERROR`, тощо),
#   * запис у файл `sum_slice_array.log`.

# * 📄 Кожен виклик і перевірка логуються:
#   * `logging.info(...)` — звичайна інформація,
#   * `logging.error(...)` — у випадку помилок.

# ## 🚀 **Приклад використання:**
# try:
#     print(sum_slice_array([1, 2, 3], 1, 2))
# except MyExceptions:
#     print("MyExceptions")

# try:
#     print(sum_slice_array([1, "oops", 3], 1, 2))
# except MyExceptions:
#     print("MyExceptions")

# try:
#     print(sum_slice_array([1, 2], 5, 1))
# except MyExceptions:
#     print("MyExceptions")

# ## 📁 **Вміст файлу `sum_slice_array.log` після запуску:**

# 2025-05-14 14:30:15,001 - INFO - Function called with arr=[1, 2, 3], first=1, second=2
# 2025-05-14 14:30:15,002 - INFO - Sum calculated successfully: 3.0
# 2025-05-14 14:30:15,003 - INFO - Function called with arr=[1, 'oops', 3], first=1, second=2
# 2025-05-14 14:30:15,004 - ERROR - Invalid elements: 1 or oops are not numeric
# 2025-05-14 14:30:15,005 - INFO - Function called with arr=[1, 2], first=5, second=1
# 2025-05-14 14:30:15,006 - ERROR - Indexes out of range

# ## ✅ Переваги логування:

# * Можна **відстежити історію викликів**, параметри, помилки;
# * Зручно для **налагодження** або **моніторингу в продакшні**;
# * Легко розширити для логування в **консоль + файл**.

# Хочеш, я покажу ще як **логувати в консоль і файл одночасно**, або **налаштувати рівень логування через аргумент/налаштування**? 😊

