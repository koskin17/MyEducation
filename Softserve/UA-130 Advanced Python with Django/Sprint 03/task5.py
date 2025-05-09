# Create decorator logger. The decorator should print to the console information about function's name and all its arguments separated with ',' for the function decorated with logger.

# Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function.

# Необходимо создать декоратор с именем logger. Этот декоратор должен выводить в консоль информацию об имени декорируемой функции и всех её аргументах, разделенных запятой. Также нужно создать функцию concat, которая принимает любое количество любых аргументов, конкатенирует их и применить к этой функции декоратор logger.

# For example

# print(concat(2, 3)) display
# Executing of function concat with arguments 2, 3...
# 23

# print(concat('hello', 2)) display
# Executing of function concat with arguments hello, 2...
# hello2

# print(concat (first = 'one', second = 'two')) display
# Executing of function concat with arguments one, two...
# onetwo

type your code here

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)


# Решение 1

# ```python
# def logger(func):
#     def wrapper(*args, **kwargs):
#         # Собираем все аргументы в виде строк:
#         arguments = []
#         if args:
#             arguments.extend(map(str, args))
#         if kwargs:
#             # Для keyword-аргументов — берём только их значения
#             arguments.extend(map(str, kwargs.values()))
#         # Выводим сообщение с именем функции и аргументами, разделёнными запятыми
#         print(f"Executing of function {func.__name__} with arguments " + ", ".join(arguments) + "...")
#         # Вызываем оригинальную функцию и возвращаем её результат
#         return func(*args, **kwargs)
#     return wrapper


# @logger
# def concat(*args, **kwargs):
#     result = ""
#     # Объединяем позиционные аргументы, преобразуя их в строки
#     for arg in args:
#         result += str(arg)
#     # Объединяем значения keyword-аргументов
#     for value in kwargs.values():
#         result += str(value)
#     return result

# # Пример использования:

# print(concat(2, 3))
# # Вывод:
# # Executing of function concat with arguments 2, 3...
# # 23

# print(concat('hello', 2))
# # Вывод:
# # Executing of function concat with arguments hello, 2...
# # hello2

# print(concat(first='one', second='two'))
# # Вывод:
# # Executing of function concat with arguments one, two...
# # onetwo
# ```

# ### Объяснение:
# 1. **Декоратор `logger`**  
#    - Функция-обертка `wrapper` принимает произвольное количество позиционных (*args) и именованных (**kwargs) аргументов.
#    - Аргументы преобразуются в строки и объединяются через запятую.
#    - Перед вызовом оригинальной функции выводится сообщение вида:  
#      `Executing of function <имя функции> with arguments <arg1>, <arg2>, ......`
# 2. **Функция `concat`**  
#    - Принимает любое количество аргументов и просто конкатенирует их в одну строку после преобразования в str.
# 3. **Использование декоратора**  
#    - Благодаря декоратору при вызове `concat` сначала срабатывает вывод сообщения, затем функция выполняется и возвращает результат.

# Таким образом решение удовлетворяет условию задачи. Если возникнут дополнительные вопросы – пожалуйста, дай знать!

# Решение 2

# def logger(func):
#     def wrapper(*args, **kwargs):
#         func_name = func.__name__
#         all_args = ", ".join(map(str, args))
#         if kwargs:
#             all_kwargs = ", ".join(f"{k}={v}" for k, v in kwargs.items())
#             if all_args:
#                 print(f"Executing of function {func_name} with arguments {all_args}, {all_kwargs}...", end=" ")
#             else:
#                 print(f"Executing of function {func_name} with arguments {all_kwargs}...", end=" ")
#         else:
#             print(f"Executing of function {func_name} with arguments {all_args}...", end=" ")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper

# @logger
# def concat(*args, **kwargs):
#     result = ""
#     for arg in args:
#         result += str(arg)
#     for value in kwargs.values():
#         result += str(value)
#     return result

# # Examples
# print(concat(2, 3))
# print(concat('hello', 2))
# print(concat(first='one', second='two'))
# print(concat(1, 'b', third=3.0))

# **Объяснение:**

# 1.  **Декоратор `logger(func)`:**
#     * Эта функция принимает другую функцию (`func`) в качестве аргумента. Это стандартная структура декоратора в Python.
#     * Внутри `logger` определяется внутренняя функция `wrapper(*args, **kwargs)`. Именно эта функция заменит исходную декорированную функцию.
#     * `*args` и `**kwargs` позволяют `wrapper` принимать любое количество как позиционных, так и именованных аргументов, точно так же, как и декорируемая функция.
#     * `func_name = func.__name__` извлекает имя декорируемой функции (например, `"concat"`).
#     * `аргументы_позиционные = ", ".join(map(str, args))` преобразует все позиционные аргументы из кортежа `args` в строки с помощью `map(str, args)` и затем объединяет их в одну строку, разделяя запятой и пробелом.
#     * `аргументы_ключевые = ", ".join(f"{ключ}={значение}" for ключ, значение in kwargs.items())` аналогично обрабатывает именованные аргументы из словаря `kwargs`, формируя строку вида `"ключ=значение"` для каждого аргумента и объединяя их.
#     * Блок `if-elif-else` отвечает за вывод в консоль информации о выполняемой функции и её аргументах. Он корректно обрабатывает случаи, когда есть только позиционные, только именованные или и те, и другие аргументы, а также случай отсутствия аргументов. `end=" "` используется для того, чтобы вывод информации об аргументах и результата функции `concat` оказались на одной строке.
#     * `результат = func(*args, **kwargs)` вызывает исходную декорированную функцию (`concat`) с переданными ей аргументами.
#     * `return результат` возвращает результат работы исходной функции.
#     * Функция `logger` возвращает функцию `wrapper`.

# 2.  **Применение декоратора `@logger`:**
#     * Строка `@logger` перед определением функции `concat` применяет к ней декоратор `logger`. Это синтаксический сахар, эквивалентный `concat = logger(concat)`.

# 3.  **Функция `concat(*args, **kwargs)`:**
#     * Эта функция принимает любое количество позиционных (`*args`) и именованных (`**kwargs`) аргументов.
#     * Она инициализирует пустую строку `результат`.
#     * Затем она последовательно добавляет строковое представление каждого позиционного аргумента в `результат`.
#     * После этого она проходит по значениям словаря `kwargs` и также добавляет их строковое представление в `результат`.
#     * В конце функция возвращает объединенную строку `результат`.

# **Как это работает на примерах:**

# * `print(concat(2, 3))`
#     * Декоратор `logger` перехватывает вызов `concat`.
#     * Выводится: `Выполнение функции concat с аргументами 2, 3...`
#     * Функция `concat` объединяет `2` и `3` в строку `"23"`.
#     * Выводится: `23` (на той же строке благодаря `end=" "`).

# * `print(concat('hello', 2))`
#     * Выводится: `Выполнение функции concat с аргументами hello, 2...`
#     * Выводится: `hello2`.

# * `print(concat(first='one', second='two'))`
#     * Выводится: `Выполнение функции concat с аргументами first=one, second=two...`
#     * Выводится: `onetwo`.

# * `print(concat(1, 'b', third=3.0))`
#     * Выводится: `Выполнение функции concat с аргументами 1, b, third=3.0...`
#     * Выводится: `1b3.0`.

# * `print(concat())`
#     * Выводится: `Выполнение функции concat без аргументов...`
#     * Выводится: `` (пустая строка).