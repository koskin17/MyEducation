# Description:
# Having two standards for a keypad layout is inconvenient!
# Computer keypad's layout:
# 7 8 9  \n
# 4 5 6  \n
# 1 2 3  \n
#   0 \n

# Cell phone keypad's layout:
# 1 2 3\n 
# 4 5 6\n  
# 7 8 9\n  
#   0\n

# Solve the horror of unstandardized keypads by providing a function that converts computer input to a number as if it was typed on a phone.

# Example:
# "789" -> "123"

# Notes:
# You get a string with numbers only

def computer_to_phone(numbers):
    # dictionary to map computer keypad numbers to phone keypad numbers
    keyboard_dictionary = {
        "7": "1",
        "8": "2",
        "9": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "1": "7",
        "2": "8",
        "3": "9",
        "0": "0"
    }
    
    phone_keyboard = []
    for i in range(len(numbers)):
        phone_keyboard.append(keyboard_dictionary[numbers[i]])
    
    return "".join(phone_keyboard)

computer_to_phone("0789456123") #"0123456789" #"Testing computer_to_phone('0789456123')")
computer_to_phone("000") #"000" #"Testing computer_to_phone('000')")
computer_to_phone("94561") #"34567" #"Testing computer_to_phone('94561')")


## ✅ Професійне рішення:
def computer_to_phone(numbers):
    mapping = {
        "7": "1", "8": "2", "9": "3",
        "4": "4", "5": "5", "6": "6",
        "1": "7", "2": "8", "3": "9",
        "0": "0"
    }
    return ''.join(mapping[d] for d in numbers)

## 🧪 Приклади:
# print(computer_to_phone("789"))     # "123"
# print(computer_to_phone("1234567890"))  # "7894561230"


## 💡 Чому це краще?

# | Що                            | Пояснення                                                     |
# | ----------------------------- | ------------------------------------------------------------- |
# | `mapping[d] for d in numbers` | Читається природно: *для кожної цифри — знайди відповідність* |
# | `''.join(...)`                | Швидко об'єднує список рядків в один рядок                    |
# | Меньше коду                   | Легше підтримувати і менше шансів помилитися                  |


## 📦 Рішення задачі:
def computer_to_phone(numbers):
    trans_table = str.maketrans("789123", "123789")
    return numbers.translate(trans_table)

# 📌 Пояснення:
# | Оригінал                                                     | Куди мапиться |
# | ------------------------------------------------------------ | ------------- |
# | `7 8 9`  → `1 2 3`                                           |               |
# | `1 2 3`  → `7 8 9`                                           |               |
# | `4 5 6` і `0` — не змінюються, тому їх не потрібно вказувати |               |

## 🧪 Приклад використання:
print(computer_to_phone("789"))         # "123"
print(computer_to_phone("123"))         # "789"
print(computer_to_phone("456"))         # "456"
print(computer_to_phone("7891234560"))  # "1237894560"

## 🧠 Переваги:
# * ✨ Суперкоротко
# * ⚡ Працює дуже швидко (перетворення на рівні C)
# * 💼 Професійно та читається добре


