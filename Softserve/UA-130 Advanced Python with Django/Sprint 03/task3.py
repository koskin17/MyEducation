# Create function create_account(user_name: string, password: string, secret_words: list). This function should return inner function check.

# The function check compares the values of its arguments with password and secret_words: the password must match completely, secret_words may be misspelled (just one element).

# Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,  special character and one number.

# Otherwise function create_account raises ValueError. 

# For example: 

# tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error 

# If tom = create_account("Tom", "Qwerty1_", ["1", "word"])  

# then 

# tom("Qwerty1_",  ["1", "word"]) return True 

# tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]

# tom("Qwerty1_",  ["word", "12"]) return True

# tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"

# Решение 1

# Ниже приведён один из вариантов решения задачи:

# - Функция `create_account` сначала проверяет, соответствует ли пароль следующим требованиям:
#   - Не менее 6 символов.
#   - Содержит хотя бы одну заглавную букву.
#   - Содержит хотя бы одну строчную букву.
#   - Содержит хотя бы одну цифру.
#   - Содержит хотя бы один специальный символ (то есть символ, для которого `not c.isalnum()` возвращает True).

# - Если пароль не проходит валидацию, генерируется исключение `ValueError`.

# - Функция возвращает внутреннюю функцию `check`, которая сравнивает переданный пароль с сохранённым и проверяет список секретных слов.  
#   **Проверка списка секретных слов** устроена так:
#   - Если длины списков не совпадают, возвращается `False`.
#   - Списки сортируются (то есть игнорируется порядок) и затем производится поэлементное сравнение.
#   - Если количество несовпадений (то есть «опечаток») не более одного, проверка считается успешной и функция возвращает `True`. В противном случае – `False`.

# Вот само решение:

# def create_account(user_name: str, password: str, secret_words: list):
#     # Проверка валидности пароля:
#     if len(password) < 6:
#         raise ValueError("Password must be at least 6 characters long.")
#     if not any(c.isupper() for c in password):
#         raise ValueError("Password must contain at least one uppercase letter.")
#     if not any(c.islower() for c in password):
#         raise ValueError("Password must contain at least one lowercase letter.")
#     if not any(c.isdigit() for c in password):
#         raise ValueError("Password must contain at least one digit.")
#     if not any(not c.isalnum() for c in password):
#         raise ValueError("Password must contain at least one special character.")
    
#     # Сохраняем данные аккаунта
#     stored_password = password
#     stored_secret_words = secret_words[:]  # копия списка секретных слов

#     def check(provided_password, provided_secret_words: list):
#         # Пароль должен совпадать точно
#         if provided_password != stored_password:
#             return False
        
#         # Длины списков секретных слов должны совпадать
#         if len(provided_secret_words) != len(stored_secret_words):
#             return False

#         # Сравнение списков в порядке, не зависящем от порядка элементов
#         sorted_stored = sorted(stored_secret_words)
#         sorted_provided = sorted(provided_secret_words)

#         # Подсчёт несовпадающих элементов
#         mismatches = sum(1 for s, p in zip(sorted_stored, sorted_provided) if s != p)

#         # Разрешается не более одной опечатки (несовпадение)
#         return mismatches <= 1

#     return check


# # Примеры использования:

# # Пример 1: Пароль "Qwerty1" не подходит (нет спецсимвола), выбрасывается ValueError:
# try:
#     tom = create_account("Tom", "Qwerty1", ["1", "word"])
# except ValueError as e:
#     print(e)  # Password must contain at least one special character.

# # Пример 2:
# tom = create_account("Tom", "Qwerty1_", ["1", "word"])

# # Точный совпадение:
# print(tom("Qwerty1_", ["1", "word"]))  # True

# # Разная длина списка секретных слов → False
# print(tom("Qwerty1_", ["word"]))        # False

# # Допускается одна опечатка при сравнении (игнорируется порядок)
# print(tom("Qwerty1_", ["word", "12"]))    # True

# # Неверный пароль → False
# print(tom("Qwerty1!", ["word", "1"]))     # False
# ```

# ### Объяснение

# 1. **Проверка пароля:**  
#    Если пароль не соответствует требованиям (по длине, наличию символов разных категорий), выбрасывается исключение `ValueError`.

# 2. **Функция `check`:**  
#    - Сначала сравнивается пароль: должна быть полная эквивалентность.
#    - Затем проверяется, что длина списка секретных слов совпадает.
#    - Для сравнения списков сортируются и поэлементно сравниваются. Допускается ровно одна несовпадающая пара (то есть один неверно введённый элемент).

# 3. **Примеры использования:**  
#    Примеры демонстрируют:
#    - Неверный пароль (без спецсимвола) приводит к исключению.
#    - При корректном пароле функция `check` возвращает `True` только если все условия соблюдены, с допуском одной ошибки в списке секретных слов.

# Этот вариант решения удовлетворяет условиям задачи. Если останутся вопросы – спрашивай!

# Решение 2

# import re

# def create_account(user_name: str, password: str, secret_words: list):
#     """
#     Создает учетную запись с заданным именем пользователя, паролем и секретными словами.
#     Возвращает внутреннюю функцию 'check', которая проверяет введенные пароль и
#     секретные слова на соответствие.

#     Args:
#         user_name: Имя пользователя (строка).
#         password: Пароль (строка).
#         secret_words: Список секретных слов (список строк).

#     Returns:
#         Внутренняя функция 'check'.

#     Raises:
#         ValueError: Если пароль не соответствует требованиям.
#     """
#     if not isinstance(user_name, str):
#         raise ValueError("Имя пользователя должно быть строкой.")
#     if not isinstance(password, str):
#         raise ValueError("Пароль должен быть строкой.")
#     if not isinstance(secret_words, list) or not all(isinstance(word, str) for word in secret_words):
#         raise ValueError("Секретные слова должны быть списком строк.")

#     # Проверка сложности пароля
#     if len(password) < 6:
#         raise ValueError("Пароль должен содержать не менее 6 символов.")
#     if not re.search(r"[A-Z]", password):
#         raise ValueError("Пароль должен содержать хотя бы одну заглавную букву.")
#     if not re.search(r"[a-z]", password):
#         raise ValueError("Пароль должен содержать хотя бы одну строчную букву.")
#     if not re.search(r"[^a-zA-Z0-9]", password):
#         raise ValueError("Пароль должен содержать хотя бы один специальный символ.")
#     if not re.search(r"[0-9]", password):
#         raise ValueError("Пароль должен содержать хотя бы одну цифру.")

#     def check(input_password: str, input_secret_words: list):
#         """
#         Внутренняя функция для проверки введенных пароля и секретных слов.

#         Args:
#             input_password: Введенный пароль (строка).
#             input_secret_words: Введенные секретные слова (список строк).

#         Returns:
#             True, если пароль совпадает и хотя бы один элемент из введенных
#             секретных слов присутствует в оригинальных секретных словах (допускается
#             одна опечатка), False в противном случае.
#         """
#         if input_password == password:
#             if len(input_secret_words) == len(secret_words):
#                 for input_word in input_secret_words:
#                     if input_word in secret_words:
#                         return True
#                 return False
#             elif len(input_secret_words) == len(secret_words) - 1:
#                 count = 0
#                 for input_word in input_secret_words:
#                     if input_word in secret_words:
#                         count += 1
#                 return count == len(input_secret_words)
#             elif len(input_secret_words) == len(secret_words) + 1:
#                 count = 0
#                 for secret_word in secret_words:
#                     if secret_word in input_secret_words:
#                         count += 1
#                 return count == len(secret_words)
#             else:
#                 return False
#         else:
#             return False

#     return check

# # Примеры использования
# try:
#     tom_invalid = create_account("Tom", "Qwerty1", ["1", "word"])
# except ValueError as e:
#     print(f"Ошибка при создании аккаунта Tom: {e}")

# tom = create_account("Tom", "Qwerty1_", ["1", "word"])

# print(f"tom('Qwerty1_', ['1', 'word']): {tom('Qwerty1_', ['1', 'word'])}")
# print(f"tom('Qwerty1_', ['word']): {tom('Qwerty1_', ['word'])}")
# print(f"tom('Qwerty1_', ['word', '12']): {tom('Qwerty1_', ['word', '12'])}")
# print(f"tom('Qwerty1!', ['word', '1']): {tom('Qwerty1!', ['word', '1'])}")

# lisa = create_account("Lisa", "P@$$wOrd1", ["key", "lock", "secret"])
# print(f"lisa('P@$$wOrd1', ['key', 'lock', 'secret']): {lisa('P@$$wOrd1', ['key', 'lock', 'secret'])}")
# print(f"lisa('P@$$wOrd1', ['key', 'secret']): {lisa('P@$$wOrd1', ['key', 'secret'])}")
# print(f"lisa('P@$$wOrd1', ['key', 'lock', 'extra', 'secret']): {lisa('P@$$wOrd1', ['key', 'lock', 'extra', 'secret'])}")
# print(f"lisa('P@$$wOrd1', ['wrong', 'lock', 'secret']): {lisa('P@$$wOrd1', ['wrong', 'lock', 'secret'])}")
# ```

# **Объяснение:**

# 1.  **Функция `create_account(user_name, password, secret_words)`:**
#     * Принимает имя пользователя (`user_name`), пароль (`password`) и список секретных слов (`secret_words`) в качестве аргументов.
#     * Выполняет **валидацию типов** для входных аргументов и выбрасывает `ValueError`, если типы не соответствуют ожидаемым.
#     * Проверяет **сложность пароля** с использованием регулярных выражений (`re`):
#         * Длина не менее 6 символов.
#         * Содержит хотя бы одну заглавную букву (`[A-Z]`).
#         * Содержит хотя бы одну строчную букву (`[a-z]`).
#         * Содержит хотя бы один специальный символ (`[^a-zA-Z0-9]`).
#         * Содержит хотя бы одну цифру (`[0-9]`).
#     * Если пароль не соответствует хотя бы одному из требований, функция выбрасывает `ValueError` с соответствующим сообщением.
#     * Определяет **внутреннюю функцию `check(input_password, input_secret_words)`**. Эта функция будет возвращена функцией `create_account`.

# 2.  **Внутренняя функция `check(input_password, input_secret_words)`:**
#     * Принимает введенный пароль (`input_password`) и список введенных секретных слов (`input_secret_words`) в качестве аргументов.
#     * Сначала проверяет, **совпадает ли введенный пароль с оригинальным паролем** (`input_password == password`).
#     * Если пароль совпадает, проверяет **секретные слова**:
#         * **Полное совпадение длины:** Если длина введенных секретных слов совпадает с длиной оригинальных секретных слов, функция проверяет, присутствует ли *каждое* введенное секретное слово в оригинальных секретных словах. Если все введенные слова найдены, возвращается `True`, иначе `False`.
#         * **Одна опечатка (один элемент отличается):** Функция проверяет, отличается ли длина введенных секретных слов от длины оригинальных секретных слов ровно на 1.
#             * Если длина введенных слов на 1 меньше, проверяется, содержатся ли *все* введенные слова в оригинальных.
#             * Если длина введенных слов на 1 больше, проверяется, содержатся ли *все* оригинальные слова во введенных.
#         * Если разница в длине больше 1, считается, что более одной опечатки, и возвращается `False`.
#     * Если введенный пароль не совпадает с оригинальным, функция возвращает `False`.

# 3.  **Возвращение `check`:**
#     * Функция `create_account` возвращает ссылку на внутреннюю функцию `check`. Благодаря **замыканию (closure)**, функция `check` "помнит" значения `password` и `secret_words` из области видимости `create_account`, даже после того как `create_account` завершила свое выполнение.

# **Примеры использования демонстрируют:**

# * Генерацию `ValueError`, если пароль не соответствует требованиям.
# * Успешную проверку (`True`), когда пароль совпадает и секретные слова совпадают по длине и содержанию.
# * Неуспешную проверку (`False`), когда пароль совпадает, но длина секретных слов отличается более чем на 1.
# * Успешную проверку (`True`), когда пароль совпадает и длина секретных слов отличается на 1, при этом все слова из более короткого списка присутствуют в более длинном.
# * Неуспешную проверку (`False`), когда пароль не совпадает.