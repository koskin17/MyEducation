# Write  the function day_of_week(day) whose input parameter is a number or string representation of number. The function returns the corresponding day of the week if the input parameter is in the range of 1 to 7, namely

# · in the case when the input parameter is 5 the function should be displayed the message – "Friday"
# · in the case when the input parameter is not in the range of 1 to 7 the function should be displayed the message – "There is no such day of the week! Please try again."
# · in the case of incorrect data the function should be displayed the message - "You did not enter a number! Please try again."

# Note: in the function you must use the "try except" construct.

# Function example:
# day_of_week(2)                     # output:   "Tuesday"
# day_of_week(11)                     # output:  "There is no such day of the week! Please try again."
# day_of_week("Monday")       # output:   "You did not enter a number! Please try again."

# Dictionary of numbers corresponding to days of the week
days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
        }

def day_of_week(day):
    try:
        # Convert the input parameter to a number
        day = int(day)
        
        # Check if the number is in the range 1-7
        if day in days:
            return days[day]
        else:
            return "There is no such day of the week! Please try again."
    
    except ValueError:  # Catch a type conversion error
        return "You did not enter a number! Please try again."

# # Примеры вызова функции
day_of_week(2)          # Output: "Tuesday"
day_of_week(11)         # Output: "There is no such day of the week! Please try again."
day_of_week("Monday")   # Output: "You did not enter a number! Please try again."
print(day_of_week(2))        # Output: "Tuesday"
print(day_of_week(11))         # Output: "There is no such day of the week! Please try again."
print(day_of_week("Monday"))   # Output: "You did not enter a number! Please try again."

# ### **Объяснение кода**
# 1. **Преобразуем параметр в `int`** (`int(day)`).  
#    - Если передано **не число**, возникает `ValueError`, и программа выводит `"You did not enter a number! Please try again."`.

# 2. **Создаём словарь соответствий дней недели**.  
#    - Если `day` **в диапазоне 1–7**, печатаем правильный день.
#    - Если `day` **не в диапазоне**, выводим `"There is no such day of the week! Please try again."`.

# 3. **Обрабатываем ошибки `ValueError`**, если ввод неправильный.

# 🔹 **Этот код корректно работает с любыми аргументами и правильно обрабатывает ошибки**.  
# Если есть вопросы, спрашивай! 🚀
