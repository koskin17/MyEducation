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

def pretty_message(text):
    # Регулярное выражение для удаления повторяющегося окончания слов
    pattern = r'\b(\w*?)(\w{1,3})\2+\b'
    
    # Заменяем повторяющиеся окончания на основную часть слова
    cleaned_text = re.sub(pattern, r'\1\2', text)
    
    return cleaned_text


# Тестовые примеры
data1 = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data1))  # "This is echo string. Replace repeated groups of symbols"

data2 = "Another input data string"
print(pretty_message(data2))  # "Another input data string" (изменений нет)

# ### 🔎 **Как работает регулярное выражение?**
# ```regex
# \b(\w+?)(\1+)\b
# ```
# 1. **`\b`** → граница слова (чтобы захватывать только слова целиком).  
# 2. **`(\w+?)`** → первая группа: ищет **основную часть слова** (минимальное количество символов, чтобы захватить корень).  
# 3. **`(\1+)`** → вторая группа: повторяет **перво найденное слово** (`\1`) **один или несколько раз**.  
# 4. **`\b`** → граница слова в конце.  
# 5. **`re.sub(pattern, r'\1', text)`** → заменяет слово с повтором на его **первоначальную форму** (`\1`).

# ---

# ### ✅ **Что делает этот код?**
# - Находит **повторяющиеся окончания слов** (`ssss`, `isisis`, `aceaceace`, `edededed` и т. д.).
# - **Удаляет повторы**, оставляя только исходные корни слов.
# - Обрабатывает **любой текст**, где встречается эта ошибка.