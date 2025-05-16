# Solve the problem of finding the tangent of the angle alpha given the sine of alpha and the cosine of alpha and add event logging to the "app.log" file.
# Catching the resulting sine and cosine values should be implemented using the "info" level.
# In the case of successful finding of the tangent of the alpha angle, logging should be with the "debug" level.
# In the event that cosine alpha = 0, logging should be with the "warning" level and the notification: "The cosine of the angle alpha = 0. The tangent is not defined.".
# In the event that the tangent is not defined, logging should be with the "critical" level and the notification: "The tangent of the angle alpha is not defined.".
# tan(α) = sin(α) / cos(α)
# Don't use: encoding='utf-8'.

# Don't use'print()'.

# Don't use'return'.

# Please use logging. ....



# For example:

# Test
# print_file("app.log")
# Input
# sin_alpha = 0.5
# cos_alpha = math.sqrt(3) / 2
# sin_alpha = 0.5
# cos_alpha = 'w'
# sin_alpha = 0.5
# cos_alpha = 0

# Result
# INFO:root:A value has been entered sin(alpha) = 0.5
# INFO:root:A value has been entered cos(alpha) = 0.8660254037844386
# DEBUG:root:The value of the tangent of the angle alpha is found = 0.5773502691896258
# INFO:root:A value has been entered sin(alpha) = 0.5
# INFO:root:A value has been entered cos(alpha) = w
# CRITICAL:root:The tangent of the angle alpha is not defined.
# INFO:root:A value has been entered sin(alpha) = 0.5
# INFO:root:A value has been entered cos(alpha) = 0
# WARNING:root:The cosine of the angle alpha = 0. The tangent is not defined.

import logging
import math

# Настроим логирование
logging.basicConfig(
    filename="app.log",  # Name of file for logging
    filemode="w",  # Overwrite file on every startup
    format="%(levelname)s:%(name)s:%(message)s",  # Log message format
    level=logging.DEBUG  # Logging level (from DEBUG to CRITICAL)
)

def findingTangent(sin_alpha, cos_alpha):
    try:
        # Logging input values
        logging.info(f"A value has been entered sin(alpha) = {sin_alpha}")
        logging.info(f"A value has been entered cos(alpha) = {cos_alpha}")

        # Check the correctness of the input data
        if not isinstance(sin_alpha, (int, float)) or not isinstance(cos_alpha, (int, float)):
            logging.critical("The tangent of the angle alpha is not defined.")
        # Check for division by zero
        elif cos_alpha == 0:
            logging.warning("The cosine of the angle alpha = 0. The tangent is not defined.")
        else:
            # Calculate the tangent
            tan_alpha = sin_alpha / cos_alpha
            logging.debug(f"The value of the tangent of the angle alpha is found = {tan_alpha}")

    except Exception as e:
        logging.critical(f"Unexpected error: {e}")

# Тестирование функции
findingTangent(0.5, math.sqrt(3) / 2)  # Ожидаемый DEBUG лог
findingTangent(0.5, "w")  # Ожидаемый CRITICAL лог
findingTangent(0.5, 0)  # Ожидаемый WARNING лог

### **Объяснение кода**
# 1️⃣ **Настроили логирование**:
#    - Запись в `app.log` (`filename="app.log"`).
#    - Файл перезаписывается при каждом запуске (`filemode="w"`).
#    - Логирование в формате `"Уровень: Сообщение"` (`format="%(levelname)s: %(message)s"`).
#    - Уровень `DEBUG`, чтобы поддерживать все уровни логов (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

# 2️⃣ **Обрабатываем сценарии**:
#    - **Логируем введённые данные** (`INFO`).
#    - **Если входные данные некорректны** (`CRITICAL` → `"The tangent of the angle alpha is not defined."`).
#    - **Если `cos_alpha == 0`** (`WARNING` → `"The cosine of the angle alpha = 0. The tangent is not defined."`).
#    - **Если вычисление прошло успешно** (`DEBUG` → `"The value of the tangent of the angle alpha is found"`).

# 3️⃣ **Ловим `Exception` на случай неожиданных ошибок** (`CRITICAL`).

# 🔹 **Этот код соответствует условиям задачи и правильно логирует все события**.  
# Попробуй запустить и скажи, если есть вопросы! 🚀
