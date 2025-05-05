# Numbers in the Morse code have the following pattern:
# all digits consist of 5 characters;
# the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
# starting with the number 6, each dot is replaced by a dash and vise versa.
# Write the function morse_number() for encryption of a number in a three-digit format in Morse code.
# Attention!
# Do not use any collection data like lists, tuples, dictionaries for holding Morse codes

# For example:
# Тест	Result
# print(morse_number("295"))
# ..--- ----. .....
# print(morse_number("005"))
# ----- ----- .....
# print(morse_number("513"))
# ..... .---- ...--
# print(morse_number("784"))
# --... ---.. ....-

def morse_number(number):
    def convert_digit(digit):
        # Число до 5 -> n точек + (5 - n) дефисов
        if digit in "12345":
            return "." * int(digit) + "-" * (5 - int(digit))
        # Число от 6 до 9 -> инверсия точек и дефисов
        elif digit in "6789":
            return "-" * (int(digit) - 5) + "." * (5 - (int(digit) - 5))
        # Число 0 -> только дефисы
        else:
            return "-----"
    
    result = ""
    for char in number:
        result += convert_digit(char) + " "
    
    return result.strip()  # Убираем лишний пробел в конце

# Тестовые примеры
print(morse_number("295"))  # ..--- ----. .....
print(morse_number("005"))  # ----- ----- .....
print(morse_number("513"))  # ..... .---- ...--
print(morse_number("784"))  # --... ---.. ....-