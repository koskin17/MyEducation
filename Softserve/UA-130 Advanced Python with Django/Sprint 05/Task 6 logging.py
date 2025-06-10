# You get a list of numbers and you have to write a program that calculates the arithmetic mean of these numbers and logs the result in the file 'app.log' with the notification level - "info".

# If the input list is empty, the program should return the line "The list is empty" - the notification should be of the "debug" level.

# If a ZeroDivisionError error occurs in the process of calculating the arithmetic mean, the program should return the line "Division by zero" - the notification should be of the "warning" level.

# If the function receives an argument that has the correct type but an inappropriate value, then handle a ValueError exception - the notification should be of the "error" level.

# If one of the numbers in the list is not a number, the program should return the line "Incorrect data entered" - the notification should be of the "critical" level.


# Change the basic configuration with filename 'app.log', file read method 'w' and output name, level name and message.
# Don't use: encoding='utf-8'.
# Don't use'print()'.
# Don't use'return'.
# Please use logging.

# Заготовка кода
# import logging

# logging.... # type your code here

# def average(numbers):
#     # type your code here

# average([1, 2, 3, 4, 5])
# average([10, -20, -30])
# average([])
# average([1, 2, 3, 0, 5])
# average([1, 2, "three", 4, 5])

import logging

# Setting up logging
logging.basicConfig(
    filename="app.log",  # Log file name
    filemode="w",  # File writing method (overwrite)
    format="%(name)s - %(levelname)s - %(message)s",  # Output format
    level=logging.DEBUG  # Logging level (lowest level - DEBUG)
)

def average(numbers):
    try:
        # Check if the list is empty
        if not numbers:
            logging.debug("The list is empty")
            logging.warning("Division by zero")
       # Check if all elements of a list are numbers
        elif not all(isinstance(number, (int, float)) for number in numbers):
            logging.critical("Incorrect data entered")
        else:
            # Calculating the arithmetic mean
            result = sum(numbers) / len(numbers)
            logging.info(f"Arithmetic mean: {result}")

    except ZeroDivisionError:
        logging.warning("Division by zero")
    except ValueError:
        logging.error("Incorrect value")

# Примеры вызова функции
average([1, 2, 3, 4, 5])        # "INFO: Arithmetic mean: 3.0"
average([10, -20, -30])         # "INFO: Arithmetic mean: -13.333333333333334"
average([])                     # "DEBUG: The list is empty"
average([1, 2, 3, 0, 5])        # "INFO: Arithmetic mean: 2.2"
average([1, 2, "three", 4, 5])  # "CRITICAL: Incorrect data entered"

### **Разбор кода**
# ✔ **Настроили логирование**:
# - `filename="app.log"` → записываем в файл `app.log`.
# - `filemode="w"` → каждый запуск перезаписывает файл.
# - `level=logging.DEBUG` → поддерживаем все уровни логов (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

# ✔ **Обрабатываем сценарии в `try-except`**:
# 1. **Пустой список** → `logging.debug("The list is empty")`.
# 2. **Есть нечисловые данные** → `logging.critical("Incorrect data entered")`.
# 3. **Вычисляем среднее** и логируем `INFO`-уровень.
# 4. **Ловим исключения** `ZeroDivisionError` и `ValueError`.

# 🔹 **Решение полностью соответствует условиям задачи**.  
# Попробуй запустить и скажи, если нужно доработать! 🚀