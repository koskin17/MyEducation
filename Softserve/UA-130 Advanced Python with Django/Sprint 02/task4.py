# As input data, you have a string that consists of words that have duplicated characters at the end of it.

# All duplications may be in the next format:

# wordxxxx
# wordxyxyxy
# wordxyzxyzxyz
# , where x, xy or xyz repeated ending of the word

# Using re module write function pretty_message() that remove all duplications

# For example:

# Тест	Result
# data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
# print(pretty_message(data))
# This is echo string. Replace repeated groups of symbols
# data = "Another input data string"
# print(pretty_message(data))

# Для удаления повторяющихся окончаний слов мы можем использовать **регулярное выражение**.  
# В данном случае можно применить **группы захвата и обратные ссылки**, чтобы найти и убрать повторяющиеся фрагменты в конце слов.  

### **Решение на Python**

import re

def remove_duplicate_suffix(word):
    word_length = len(word)
    for size in range(1, word_length // 2 + 1):
        suffix = word[-size:]
        repeats = word.count(suffix, word_length - size * 2)
        if repeats >= 1 and word.endswith(suffix * (repeats + 1)):
            while word.endswith(suffix * 2):
                word = word[:-size]
            break
    return word

def pretty_message(data):
    return re.sub(r'\b\w+\b', lambda m: remove_duplicate_suffix(m.group()), data)

# Тестовые примеры
data1 = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data1))  # "This is echo string. Replace repeated groups of symbols"

data2 = "Another input data string"
print(pretty_message(data2))  # "Another input data string" (изменений нет)

Ого, супер! Дуже круто, що ти знайшов варіант, який **працює на всіх тестах** 👏
Звісно, ось **готовий код + докладне пояснення в одному повідомленні, яке можна зберегти:**

---

## ✅ **Готовий код:**

```python
import re

def remove_duplicate_suffix(word):
    word_length = len(word)
    for size in range(1, word_length // 2 + 1):
        suffix = word[-size:]
        repeats = word.count(suffix, word_length - size * 2)
        if repeats >= 1 and word.endswith(suffix * (repeats + 1)):
            while word.endswith(suffix * 2):
                word = word[:-size]
            break
    return word

def pretty_message(data):
    return re.sub(r'\b\w+\b', lambda m: remove_duplicate_suffix(m.group()), data)
```

---

# ## ✨ **Пояснення коду:**

# ### 🔍 **Завдання:**

# Потрібно видалити **повторювані суфікси** в кінці кожного слова. Повторюваний блок може бути **довільної довжини** (наприклад: `x`, `xy`, `xyz`), і повторюватися **декілька разів підряд.**

# ### 📌 **Як працює функція `remove_duplicate_suffix`:**

# 1. Беремо слово.
# 2. Перебираємо **усі можливі суфікси** розміром від 1 до `len(word)//2` (бо довший блок не зможе повторитися мінімум 2 рази).
# 3. Для кожного суфіксу:
#    * перевіряємо, **чи повторюється він мінімум 2 рази підряд в кінці слова.**
#    * якщо так:
#      * обрізаємо повтори, поки не залишиться **тільки один суфікс.**
#      * зупиняємося (виконується `break`, бо знайшли потрібний суфікс).
# 4. Якщо жодного повтору не знайдено — повертаємо слово без змін.
# ---
# ### 📌 **Функція `pretty_message`:**
# 1. Використовує `re.sub` для пошуку **усіх слів** у рядку (регулярний вираз `\b\w+\b` — слово між межами).
# 2. Для кожного слова:
#    * застосовує `remove_duplicate_suffix`.
#    * замінює слово на скорочену версію, якщо були повтори.
# ---
# ## 🎯 **Приклади роботи:**
# ```python
# data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
# print(pretty_message(data))
# ```
# ✅ Результат:
# ```
# This is echo string. Replace repeated groups of symbols

# data = "Another input data string"
# print(pretty_message(data))
# ```

# ✅ Результат:

# ```
# Another input data string
# ```

# ---

# ## 📝 **Ключові моменти:**

# * Підтримує **повторюваний суфікс будь-якої довжини**.
# * Працює тільки на **словах** (не чіпає знаки пунктуації, лапки, спецсимволи).
# * Заміна відбувається **лише якщо знайдено мінімум 2 підрядкових повтори суфікса.**

# ---

# 💾 **Можеш скопіювати цей код і пояснення собі у нотатки — він універсальний і проходить всі тест-кейси, включно з рядками, що містять лапки, код тощо!**

# Якщо захочеш додати підтримку ще складніших випадків (наприклад, текст із HTML, або спецсимволами) — завжди можна адаптувати.
# Вітаю з таким ретельним підходом! 🚀👏
