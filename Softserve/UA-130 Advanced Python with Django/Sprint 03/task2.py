# Create function create with one string argument. This function should return anonymous function that checks if the argument of function is equals to the argument of outer function. 

# For example: 
#  tom = create("pass_for_Tom") 
#  tom("pass_for_Tom") returns true 
#  tom("pass_for_tom") returns false

def create(outer_arg):
    """
    Создает и возвращает анонимную функцию (lambda-функцию),
    которая проверяет, равен ли её аргумент аргументу внешней функции 'outer_arg'.

    Args:
        outer_arg: Строка, с которой будет сравниваться аргумент анонимной функции.

    Returns:
        Анонимная функция, выполняющая проверку на равенство.
    """
    return lambda inner_arg: inner_arg == outer_arg

# Пример использования:
tom = create("pass_for_Tom")
print(tom("pass_for_Tom"))  # Выводит: True
print(tom("pass_for_tom"))  # Выводит: False

lisa = create("secret_lisa")
print(lisa("secret_lisa")) # Выводит: True
print(lisa("wrong_password")) # Выводит: False

# **Подробное объяснение:**

# 1.  **`def create(outer_arg):`**:
#     * Мы определяем функцию с именем `create`, которая принимает один аргумент `outer_arg`. Это значение, с которым мы будем сравнивать аргумент анонимной функции.

# 2.  **`lambda inner_arg: inner_arg == outer_arg`**:
#     * Внутри функции `create` мы создаем анонимную функцию (lambda-функцию).
#     * `lambda` - это ключевое слово, используемое для создания анонимных функций в Python.
#     * `inner_arg` - это аргумент, который принимает анонимная функция.
#     * `inner_arg == outer_arg` - это выражение, которое вычисляется и возвращается анонимной функцией.  Оно сравнивает аргумент `inner_arg` с `outer_arg` (значением, переданным в `create`) и возвращает `True`, если они равны, и `False` в противном случае.
#     * Важно отметить, что lambda-функция имеет доступ к переменной `outer_arg` из области видимости функции `create`. Это снова пример **замыкания (closure)**.

# 3.  **`return lambda inner_arg: inner_arg == outer_arg`**:
#     * Функция `create` возвращает созданную lambda-функцию.

# **Как это работает на примере `tom = create("pass_for_Tom")`**:

# 1.  Вызывается функция `create` с аргументом `"pass_for_Tom"`.
# 2.  Внутри `create` создается lambda-функция: `lambda inner_arg: inner_arg == "pass_for_Tom"`.
# 3.  Функция `create` возвращает эту lambda-функцию.
# 4.  Возвращенная lambda-функция присваивается переменной `tom`.  Теперь `tom` - это функция, которая проверяет, равен ли её аргумент строке `"pass_for_Tom"`.

# **Как это работает на примере `tom("pass_for_Tom")` и `tom("pass_for_tom")`**:

# 1.  Вызывается функция, на которую ссылается переменная `tom`.  Это lambda-функция, созданная ранее.
# 2.  Аргумент `"pass_for_Tom"` передается в lambda-функцию.
# 3.  Вычисляется выражение `"pass_for_Tom" == "pass_for_Tom"`, которое равно `True`.
# 4.  Возвращается значение `True`.

# Во втором случае, аргумент `"pass_for_tom"` передается в ту же lambda-функцию. Вычисляется выражение `"pass_for_tom" == "pass_for_Tom"`, которое равно `False`, и возвращается `False`.

# Таким образом, функция `create` создает функцию-компаратор, которая "помнит" значение, с которым нужно сравнивать.