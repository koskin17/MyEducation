# We have a function calc(a, b, op) as shown on screenshot.

# Write your code insode run_calc with calling of function calc. Script must work with any arguments. Catch ValueError and print it, catch TypeError and print "TypeError", Catch error of division by zero and print "Division by zero". After call calc print "End of calculation" in all cases.

def calc(a, b, op):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b
    raise ValueError("Incorrect operation is obtained")

# For example:

# Тест	Result
# run_calc(1, 2, 0)
# 3
# End of calculation
# run_calc(-19, "String", 3)
# TypeError
# End of calculation
# run_calc(42, 0, 3)
# Division by zero
# End of calculation

def run_calc(a, b, op):
    try:
        result = calc(a, b, op)  # Вызов функции calc с аргументами
        print(result)
    except ValueError as e:  # Обработка ValueError
        print(e)
    except TypeError:  # Обработка TypeError
        print("TypeError")
    except ZeroDivisionError:  # Обработка деления на ноль
        print("Division by zero")
    finally:
        print("End of calculation")  # Вывод в любом случае

# # Примеры вызова:
run_calc(1, 2, 0)  # Вывод: 3, End of calculation
run_calc(-19, "String", 3)  # Вывод: TypeError, End of calculation
run_calc(42, 0, 3)  # Вывод: Division by zero, End of calculation

# ### **Объяснение кода**
# 1. **Используем `try-except-finally`**:
#    - `try`: пытаемся выполнить `calc(a, b, op)`.
#    - `except ValueError`: ловим исключение, если операция некорректна.
#    - `except TypeError`: ловим ошибки типа (например, строка вместо числа).
#    - `except ZeroDivisionError`: ловим деление на ноль.
#    - `finally`: выполняется **всегда** (печатает `"End of calculation"`).

# 🔹 Этот код **работает с любыми аргументами** и **корректно обрабатывает ошибки**.  
# Если есть вопросы, спрашивай! 🚀
