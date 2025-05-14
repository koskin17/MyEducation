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
