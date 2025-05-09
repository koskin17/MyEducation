## 1. Assignment (in English)

# Create a function `create_account(user_name: string, password: string, secret_words: list)`. This function should return an inner function `check`.

# The function `check` compares the values of its arguments with the saved `password` and `secret_words`: the password must match exactly, and the `secret_words` list is considered correct if it may contain exactly one mispelled element (i.e. at most one element differs when compared regardless of order).

# Additionally, the password must contain at least 6 symbols, including **one uppercase letter**, **one lowercase letter**, **one special character** (non-alphanumeric), and **one number**.  
# If the password does not meet these criteria, the function `create_account` should raise a `ValueError`.

# For example:
#   tom = create_account("Tom", "Qwerty1", ["1", "word"])

#   should raise a `ValueError` (because the password is missing a special character).

#   If  
#   tom = create_account("Tom", "Qwerty1_", ["1", "word"])
#   then:
#   - `tom("Qwerty1_", ["1", "word"])` returns `True`
#   - `tom("Qwerty1_", ["word"])` returns `False` due to different lengths of the secret words lists.
#   - `tom("Qwerty1_", ["word", "12"])` returns `True`
#   - `tom("Qwerty1!", ["word", "1"])` returns `False` because the password does not match exactly.

## 2. Перевод задания на русский язык

# Создайте функцию  

# create_account(user_name: string, password: string, secret_words: list)

# Эта функция должна возвращать внутреннюю функцию `check`.

# Функция `check` сравнивает значения переданных ей аргументов с сохранёнными `password` и `secret_words`: пароль должен совпадать полностью, а список секретных слов считается правильным, если допускается ровно одна ошибка (то есть, не более одного элемента отличается при сравнении вне зависимости от порядка).

# Кроме того, пароль должен содержать не менее 6 символов, включая **одну заглавную букву**, **одну строчную букву**, **один спецсимвол** (не букву и не цифру) и **одну цифру**.  
# Если пароль не соответствует этим критериям, функция `create_account` должна выбрасывать исключение `ValueError`.

# Например:
# -  
#   ```python
#   tom = create_account("Tom", "Qwerty1", ["1", "word"])

#   должно вызвать исключение `ValueError` (так как в пароле отсутствует спецсимвол).

# -  
#   Если  

#   tom = create_account("Tom", "Qwerty1_", ["1", "word"])

#   тогда:
#   - `tom("Qwerty1_", ["1", "word"])` возвращает `True`
#   - `tom("Qwerty1_", ["word"])` возвращает `False` из-за разной длины списков секретных слов.
#   - `tom("Qwerty1_", ["word", "12"])` возвращает `True`
#   - `tom("Qwerty1!", ["word", "1"])` возвращает `False`, так как пароль не совпадает полностью.

## 3. Final Working Code

def create_account(user_name: str, password: str, secret_words: list):
    # Validate the password based on the criteria:
    def validate_password(pw: str) -> bool:
        if len(pw) < 6:
            return False
        if not any(c.isupper() for c in pw):   # must contain at least one uppercase
            return False
        if not any(c.islower() for c in pw):   # must contain at least one lowercase
            return False
        if not any(c.isdigit() for c in pw):     # must contain at least one digit
            return False
        # must contain at least one special character (non-alphanumeric)
        if not any(not c.isalnum() for c in pw):
            return False
        return True

    if not validate_password(password):
        raise ValueError("Invalid password")
    
    # Save the provided password and a copy of secret_words
    stored_password = password
    stored_secret_words = secret_words[:]

    # Define the inner function 'check'
    def check(provided_password, provided_secret_words: list):
        # The provided password must match exactly
        if provided_password != stored_password:
            return False
        # The lists of secret words must have the same length
        if len(provided_secret_words) != len(stored_secret_words):
            return False

        # Compare the saved secret_words with provided ones regardless of order.
        # We allow at most one mismatch.
        copy_list = stored_secret_words.copy()
        match_count = 0
        for word in provided_secret_words:
            if word in copy_list:
                copy_list.remove(word)
                match_count += 1
        mismatches = len(stored_secret_words) - match_count
        return mismatches <= 1

    # Ensure the inner function name is "check"
    check.__name__ = "check"
    return check


# ----- Example tests -----

# Test arrays for secret words:
initial_arr = ["one", "two", "three"]

# Test 1: Exact match with same list
checked_arr_1_true = ["one", "two", "three"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_1_true))  # Expected: True

# Test 2: One secret word is slightly different (allowed mispelling)
checked_arr_2_true = ["one", "tw0", "three"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_2_true))  # Expected: True

# Test 3: Another variation with one mismatch
checked_arr_3_true = ["one", "two", "thre3"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_3_true))  # Expected: True

# Test 4: Different order but matching elements (allowed)
checked_arr_4_true = ["two", "one", "three"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_4_true))  # Expected: True

# Test 5: Exact matching (again)
checked_arr_5_true = ["one", "two", "three"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_5_true))  # Expected: True

# Test 6: Different order
checked_arr_6_true = ["three", "two", "one"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_6_true))  # Expected: True

# Test 7: More than one mismatch → should return False
checked_arr_7_false = ["one", "tw0", "thr0e"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_7_false))  # Expected: False

# Test 8: Completely different secret words list → should return False
checked_arr_8_false = ["1", "2", "3"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_8_false))  # Expected: False

# Test 9: Different lengths of secret words lists → should return False
checked_arr_9_false = ["one", "two"]
val1 = create_account("123", "qQ1!45", initial_arr)
print(val1("qQ1!45", checked_arr_9_false))  # Expected: False

# Test for password validation:
try:
    create_account("123", "qQ1345", initial_arr)
except ValueError:
    print("Raises ValueError")  # Expected output

# Testing that the inner function name is "check"
check_func = create_account("test", "qQ1!45", ["a", "b"])
print("check" in [check_func.__name__])  # Expected: True

# Tests for another account (user2)
user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5", ["abc3", "word1", "list"]))    # Expected: True
print(user2("yu6r*Tt5", ["abc3", "word1", "zzzzzz"]))     # Expected: True
print(user2("yu6r*Tt5", ["abc3", "abc3", "abc3"]))        # Expected: False
print(user2("yu6r*Tt5", ["word1", "zzzz", "z"]))          # Expected: False

# Test for user3:
# Note: Using 'initial_arr' as secret_words for this test, which in this context are ["one", "two", "three"]
user3 = create_account("User", "MmKk*9kj", ["1", "2", "1"])
print(user3("MmKk*9kj", ["1", "2", "1"]))  # Expected: True

# Test for simple user:
try:
    simple_user = create_account("A", "Aa!1", ["word"])
except ValueError:
    print("Raises ValueError")  # Expected: Raises ValueError due to password not meeting criteria

simple_user = create_account("A", "Aa!190", ["word"])
print(simple_user("Aa!190", ["word"]))  # Expected: True

# ## 4. Detailed Explanation of the Code

# ### **Password Validation**

# 1. **Function `validate_password`:**  
#    - Проверяет, что длина пароля не меньше 6 символов.
#    - Проверяет наличие хотя бы одной заглавной буквы с помощью `any(c.isupper() for c in pw)`.
#    - Проверяет наличие хотя бы одной строчной буквы через `any(c.islower() for c in pw)`.
#    - Проверяет наличие хотя бы одной цифры с помощью `any(c.isdigit() for c in pw)`.
#    - Проверяет наличие хотя бы одного спецсимвола, используя условие `any(not c.isalnum() for c in pw)`, где спецсимвол – это символ, который не является ни буквой, ни цифрой.
#    - Если хотя бы одно из условий нарушается, функция возвращает `False`.

# 2. Если функция `validate_password` возвращает `False`, происходит выброс исключения `ValueError`. Это гарантирует, что аккаунт создаётся только с корректным паролем.

### **Сохранение Данных**

# - Сохранён пароль и копия списка секретных слов (`stored_secret_words = secret_words[:]`) для дальнейшего сравнения.

### **Внутренняя Функция `check`**

# 1. **Проверка пароля:**  
#    - Сначала функция сравнивает предоставленный пароль с сохранённым. Если они не совпадают (точное сравнение), возвращается `False`.

# 2. **Проверка длины списков секретных слов:**  
#    - Функция проверяет, совпадает ли длина переданного списка секретных слов с длиной сохранённого. Если длины различаются, функция сразу возвращает `False`.

# 3. **Сравнение секретных слов:**  
#    - Для сравнения списков независимо от порядка создаётся копия сохранённого списка (`copy_list`).
#    - Для каждого слова из переданного списка, если слово находится в копии, оно удаляется из копии, а счётчик совпадений (`match_count`) увеличивается.
#    - Подсчитывается число несовпадений как разница между исходной длиной списка секретных слов и количеством совпадений.
#    - Функция возвращает `True`, если число несовпадений не превышает 1 (то есть допускается ровно одна ошибка), иначе – `False`.

# 4. **Установка имени функции:**  
#    - Перед возвратом `check` ей присваивается имя `"check"` через `check.__name__ = "check"`, что удовлетворяет требованию тестов, проверяющим имя внутренней функции.

### **Примеры Тестирования**

# - Приведены примеры тестов для различных вариантов ввода секретных слов, проверки корректности пароля, а также дополнительные тесты, демонстрирующие выброс исключения `ValueError` для неверно заданного пароля.
# - Даны тесты для разных пользователей (например, `user2` и `user3`) и проверка того, что список секретных слов сравнивается корректно (без учета порядка, с допуском одной ошибки).