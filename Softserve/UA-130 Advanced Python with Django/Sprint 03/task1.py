# Create function with name outer(name). This function should return inner function with name inner.
# This inner function prints message Hello, <name>!
# For example 
# tom = outer("tom")
# tom() -> Hello, tom!

def outer(name):
    """
    Внешняя функция, которая принимает имя в качестве аргумента
    и возвращает внутреннюю функцию 'inner'.
    """
    def inner():
        """
        Внутренняя функция, которая выводит приветствие с использованием
        имени, переданного во внешнюю функцию.
        """
        print(f"Hello, {name}!")
    return inner

# Пример использования:
tom = outer("tom")
tom()  # Вывод: Hello, tom!

lisa = outer("lisa")
lisa() # Вывод: Hello, lisa!

# **Подробное объяснение:**

# 1.  **`def outer(name):`**:
#     * Мы определяем внешнюю функцию с именем `outer`.
#     * Эта функция принимает один аргумент, который мы назвали `name`. Ожидается, что этот аргумент будет строкой, представляющей чье-то имя.

# 2.  **`def inner():`**:
#     * Внутри функции `outer` мы определяем другую функцию с именем `inner`.
#     * Функция `inner` не принимает никаких аргументов.

# 3.  **`print(f"Hello, {name}!")`**:
#     * Внутри функции `inner` мы используем f-строку (formatted string literal) для создания приветственного сообщения.
#     * Переменная `name`, которая была передана в функцию `outer`, доступна внутри функции `inner`. Это называется **замыканием (closure)**. Внутренняя функция "замыкает" (помнит) переменные из лексического окружения внешней функции, даже после того, как внешняя функция завершила свое выполнение.

# 4.  **`return inner`**:
#     * Функция `outer` не вызывает функцию `inner`. Вместо этого она *возвращает саму функцию `inner` как объект*.

# **Как это работает на примере `tom = outer("tom")`:**

# 1.  Вы вызываете функцию `outer` с аргументом `"tom"`.
# 2.  Внутри `outer` определяется функция `inner`, которая "помнит", что переменная `name` имеет значение `"tom"`.
# 3.  Функция `outer` возвращает объект функции `inner`.
# 4.  Этот возвращенный объект функции присваивается переменной `tom`. Теперь `tom` является ссылкой на функцию `inner`, которая была создана с "запомненным" именем `"tom"`.

# **Как это работает на примере `tom()`:**

# 1.  Вы вызываете функцию, на которую ссылается переменная `tom`. Это та самая функция `inner`, которую вернула `outer` с именем `"tom"`.
# 2.  Внутри `inner` выполняется команда `print(f"Hello, {name}!")`. Поскольку `inner` "помнит", что `name` равно `"tom"`, на экран выводится "Hello, tom!".

# **Пример с `lisa = outer("lisa")` и `lisa()`:**

# Аналогично, когда вы вызываете `outer("lisa")`, создается новая внутренняя функция `inner`, которая теперь "помнит", что `name` равно `"lisa"`. При вызове `lisa()`, на экран выводится "Hello, lisa!".

# Таким образом, функция `outer` является фабрикой функций. Она создает "специализированные" внутренние функции `inner`, каждая из которых несет в себе имя, переданное при ее создании. Это мощный механизм в Python, который используется для создания более гибкого и структурированного кода.