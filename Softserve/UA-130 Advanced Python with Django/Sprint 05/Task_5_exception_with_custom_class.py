# Write  the function check_number_group(number) whose input parameter is a number. The function checks whether the  set number is more than number 10:

# in case the number is more than 10 the function should be displayed the corresponding message - "Number of your group input parameter of function is valid";
# in case the number is less than or equal to 10 the function should be raised the exception of your own class ToSmallNumberGroupError and displayed the corresponding message - "We obtain error: Number of your group can't be less than 10";
# in the case of incorrect data the function should be displayed the message - "You entered incorrect data. Please try again."


# Function example:
# check_number_group(number) (4)       #output:    "We obtain error: Number of your group can't be less than 10 "
# check_number_group(number) (59)    #output:     "Number of your group 59 is valid"
# check_number_group("25")                #output:    "Number of your group 25 is valid"
# check_number_group("abc")              #output:     "You entered incorrect data. Please try again."

# Создание собственного класса исключения
class ToSmallNumberGroupError(Exception):
    pass

def check_number_group(number):
    try:
        # Convert the input to a number
        number = int(number)

        # Check if the number is greater than 10
        if number > 10:
            return f"Number of your group {number} is valid"
        else:
            return ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10")
    
    except ToSmallNumberGroupError as e:
        return e
    except ValueError:
        return "You entered incorrect data. Please try again."

# # Примеры вызова функции
check_number_group(4)       # Output: "We obtain error: Number of your group can't be less than 10"
check_number_group(59)      # Output: "Number of your group 59 is valid"
check_number_group("25")    # Output: "Number of your group 25 is valid"
check_number_group("abc")   # Output: "You entered incorrect data. Please try again."
print(check_number_group(4))       # Output: "We obtain error: Number of your group can't be less than 10"
print(check_number_group(59))      # Output: "Number of your group 59 is valid"
print(check_number_group("25"))    # Output: "Number of your group 25 is valid"
print(check_number_group("abc"))   # Output: "You entered incorrect data. Please try again."

# Объяснение кода
# - Создаём пользовательский класс исключения ToSmallNumberGroupError, который наследуется от Exception.
# - Используем try-except:
# - int(number): преобразуем входной параметр в число. Если ввод не число, ValueError.
# - Если number > 10: печатаем "Number of your group … is valid".
# - Если number <= 10: вызываем ToSmallNumberGroupError с нужным сообщением.
# - except ToSmallNumberGroupError as e: ловим и выводим пользовательское исключение.
# - except ValueError: ловим неверный ввод ("abc" вместо числа).

# В первом случае класс ToSmallNumberGroupError написан как заглушка и это не очень хорошо.
# Пользовательский класс, даже заглушка, должен быть написан полностью и правильно - это best practices.
# По **best practices** (лучшим практикам Python) собственные классы исключений (`custom exceptions`) нужно **оформлять полноценно**, а не просто с `pass`.

## 🔹 Как правильно оформить свой класс исключения
# class ToSmallNumberGroupError(Exception):
#     """Custom exception raised when the group number is less than or equal to 10."""

#     def __init__(self, message="Number of your group can't be less than 10"):
#         self.message = message
#         super().__init__(self.message)  # Передаём сообщение базовому классу Exception

## 🔍 Объяснение по шагам:
# `class ToSmallNumberGroupError(Exception):` - создаёт свой собственный класс ошибки, который **унаследован от `Exception`** (базовый класс для всех исключений в Python)
# `"""..."""` - докстрока — полезно описать, **в каких случаях вызывается это сключение**.
# `def __init__(...)` - конструктор класса. Позволяет нам передавать кастомное сообщение.
# `self.message = message` - сохраняем сообщение как атрибут экземпляра.
# `super().__init__(self.message)` - вызываем родительский `__init__` и передаём туда сообщение, чтобы исключение **корректно работало как обычная ошибка** (с текстом, трассировкой и т.д.).

## Пример использования:
# try:
#     raise ToSmallNumberGroupError()
# except ToSmallNumberGroupError as e:
#     print(f"We obtain error: {e}")

# 🔸 Вывод:
# We obtain error: Number of your group can't be less than 10
# Можно передать и своё сообщение:
# raise ToSmallNumberGroupError("Custom message!")

## 💡 Зачем писать `__init__`, если можно просто `pass`?
# Если ты напишешь `pass`, ты не сможешь:
# * передать кастомное сообщение;
# * удобно использовать эту ошибку в логах, тестах и отладке;
# * сопровождать исключение дополнительной логикой (например, логированием).

# 🔹 Поэтому **в боевых проектах** всегда оформляют кастомные исключения **с `__init__` и сообщением**.

# Когда ты хочешь создать **один кастомный класс исключения для нескольких видов ошибок**, тебе нужно:

## ✅ **1. Правильно унаследовать класс**
# Ты всё ещё наследуешь его от `Exception` или от более узкого класса (например, `ValueError`, `TypeError`), если хочешь уточнить контекст.
## ✅ **2. Добавить параметр `code` или `error_type` (или что-то подобное)**

# Чтобы различать **типы ошибок внутри одного класса**, можно передавать дополнительную информацию: тип, код или даже словарь с деталями.

### 🔧 Пример: один класс для нескольких ошибок
# class GroupValidationError(Exception):
#     """Custom exception for group-related validation errors."""

#     def __init__(self, message, error_type=None):
#         self.message = message
#         self.error_type = error_type  # Например, "TooSmall", "NotANumber"
#         super().__init__(self.message)

#     def __str__(self):
#         return f"[{self.error_type}] {self.message}" if self.error_type else self.message

### 📌 Как использовать:
# ошибка из-за малого числа
# raise GroupValidationError("Number is too small", error_type="TooSmall")

# ошибка из-за некорректных данных
# raise GroupValidationError("Not a valid number", error_type="InvalidData")

### ✅ Обработка ошибок:
# try:
#     raise GroupValidationError("Invalid", error_type="BadFormat")
# except GroupValidationError as e:
#     if e.error_type == "TooSmall":
#         print("Handle too small group error")
#     elif e.error_type == "InvalidData":
#         print("Handle wrong input")
#     else:
#         print("Other group error:", e)

## 🧠 Best practices (итоги):
# Правило - Наследуй от `Exception` или от подходящего подтипа - Чёткая структура и читаемость
# Используй параметры `error_type`, `code`, `details` - Позволяет передавать контекст
# Переопредели `__str__()` - Для красивого вывода и логирования
# Добавь `docstring` - Для автодокументации и читаемости
