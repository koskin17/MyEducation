## **1. Задание (на английском)**

# Create a decorator `logger`. The decorator should print to the console information about the function's name and all its arguments separated with ',' for the function decorated with `logger`.

# Create the function `concat` with any number of any arguments which concatenates arguments and applies the `logger` decorator to this function.

### **For example:**
# print(concat(2, 3))  # Expected output:
# Executing of function concat with arguments 2, 3...
# 23

# print(concat('hello', 2))  # Expected output:
# Executing of function concat with arguments hello, 2...
# hello2

# print(concat(first='one', second='two'))  # Expected output:
# Executing of function concat with arguments one, two...
# onetwo

## **2. Перевод задания на русский язык**

# Создайте декоратор `logger`. Этот декоратор должен выводить в консоль информацию об имени декорируемой функции и всех её аргументах, разделённых запятой.

# Создайте функцию `concat`, принимающую любое количество аргументов, которая конкатенирует их и использует декоратор `logger`.

### **Примеры вызовов:**
# print(concat(2, 3))  # Ожидаемый вывод:
# Executing of function concat with arguments 2, 3...
# 23

# print(concat('hello', 2))  # Ожидаемый вывод:
# Executing of function concat with arguments hello, 2...
# hello2

# print(concat(first='one', second='two'))  # Ожидаемый вывод:
# Executing of function concat with arguments one, two...
# onetwo
## **3. Рабочий код**
# Этот код корректно выполняет задачу и учитывает порядок вывода `print()`.

import functools

def logger(func):
    @functools.wraps(func)  # Сохраняем метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Сначала выполняем оригинальную функцию
        arguments = []
        if args:
            arguments.extend(map(str, args))
        if kwargs:
            arguments.extend(map(str, kwargs.values()))
        print(f"Executing of function {func.__name__} with arguments " + ", ".join(arguments) + "...")
        return result  # Возвращаем результат оригинальной функции
    return wrapper


@logger
def concat(*args, **kwargs):
    result = ""
    for arg in args:
        result += str(arg)
    for value in kwargs.values():
        result += str(value)
    return result


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


# # ✅ **Проверим тестовые данные**
# print_arg(2)

# # 🔥 **Ожидаемый результат:**
# # 2
# # Executing of function print_arg with arguments 2...

# ## **4. Детальное объяснение работы кода**

# ### **🔹 Декоратор `logger`**
# 1. **Сохраняет метаданные оригинальной функции (`@functools.wraps(func)`)**  
#    - Без этого, `wrapper` заменил бы оригинальную функцию, теряя её имя (`func.__name__`) и документацию (`func.__doc__`).
#    - `functools.wraps(func)` помогает сохранить идентичность функции.

# 2. **Функция `wrapper` выполняет декорируемую функцию перед выводом логов**  
#    - `result = func(*args, **kwargs)` → **Сначала вызываем оригинальную функцию**.
#    - Затем собираем аргументы и выводим сообщение `Executing of function ...`.

# 3. **Возвращаем результат оригинальной функции**  
#    - `return result` гарантирует, что декорированная функция (`concat`, `sum`, `print_arg`) возвращает ожидаемый результат.

# ---

# ### **🔹 Функция `concat`**
# 1. **Принимает любое количество аргументов** (`*args, **kwargs`).  
# 2. **Конкатенирует их в строку**:
#    - `for arg in args:` → преобразует позиционные аргументы в строку и объединяет.
#    - `for value in kwargs.values():` → делает то же самое для именованных аргументов.

# ---

# ### **🔹 Функция `print_arg`**
# 1. Выводит аргумент `arg` с помощью `print(arg)`.  
# 2. Использует `logger`, который **сначала выполняет `print(arg)`, а затем добавляет логирующее сообщение**.  
# 3. Благодаря исправленной логике **сначала печатается аргумент, потом лог**, как того требуют тесты.

# ---

# ### **🔹 Финальный вывод для `print_arg(2)`**
# ```plaintext
# 2
# Executing of function print_arg with arguments 2...