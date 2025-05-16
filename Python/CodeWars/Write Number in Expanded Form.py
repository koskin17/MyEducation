# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
# NOTE: All numbers will be whole numbers greater than 0.

# Ця задача — класична задача на **перетворення числа в розгорнуту (expanded) форму**, тобто представлення кожної цифри з урахуванням її позиції в числі.
# ## 🎯 Приклад:
# Число `70304` ми перетворюємо на:
# ```
# 70000 + 300 + 4
# ```

# Бо:
# * 7 — стоїть у десятках тисяч → 70000
# * 0 — пропускаємо
# * 3 — сотні → 300
# * 0 — пропускаємо
# * 4 — одиниці → 4

## ✅ Простий та ефективний спосіб:
def expanded_form(num):
    num_str = str(num)               # Перетворимо число в рядок
    length = len(num_str)           # Довжина числа
    parts = []

    for i, digit in enumerate(num_str):
        if digit != '0':
            zeros = length - i - 1   # Кількість нулів після цифри
            parts.append(digit + '0' * zeros)

    return ' + '.join(parts)

## 🧪 Приклади використання:
print(expanded_form(12))      # "10 + 2"
print(expanded_form(45))      # "40 + 5"
print(expanded_form(70304))   # "70000 + 300 + 4"

# ## 📦 Як працює:
# * `enumerate(num_str)` — перебирає всі цифри
# * Якщо цифра **не нуль**:
#   * Додаємо до неї **стільки нулів**, скільки цифр після неї
# * Потім об'єднуємо частини через `" + "` → це і є розгорнута форма

## 🧠 Якщо хочеш ще простіший однорядковий варіант:

def expanded_form(num):
    return ' + '.join(
        digit + '0' * (len(str(num)) - i - 1)
        for i, digit in enumerate(str(num)) if digit != '0'
    )