# Please specify a regular expression for matching publication formats such as "Head First. Python: PROSystem, 2021 and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022

# For example:

# Тест	Result
# if 're' in sys.modules:
#     print(True)
# True
# data = '"Head First. Python: PROSystem, 2021"# and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"'

# for item in pretty_message(data):
#     print(item)
# ('Head First. Python', 'PROSystem', '2021')
# ('Coding for Kids Python & Blockchain Programming', 'Elliot Davis', '2022')

# Ты можешь использовать регулярное выражение для извлечения названия книги, автора (или издателя) и года из строки.  

### **Готовое регулярное выражение**
import re

def pretty_message(data):
    pattern = r'"([^"]+?):\s*([^,]+),\s*(\d{4})"'  
    matches = re.findall(pattern, data)
    return matches

# Тестовые данные
data = '"Head First. Python: PROSystem, 2021"# and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"'

# Вывод результатов
for item in pretty_message(data):
    print(item)

### **Выходные данные (ожидаемый результат)**

# ('Head First. Python', 'PROSystem', '2021')
# ('Coding for Kids Python & Blockchain Programming', 'Elliot Davis', '2022')

### 🔎 **Разбор регулярного выражения:**
# ```regex
# "([^"]+?):\s*([^,]+),\s*(\d{4})"
# ```
# 1. **`"([^"]+?):`**  
#    - `"([^"]+?)"` → захватывает **название книги**, включая точки (`.`).  
#    - `:` → обязательный **разделитель** между названием и автором/издателем.  

# 2. **`\s*([^,]+),`**  
#    - `\s*` → допускает возможные пробелы после `:`.  
#    - `([^,]+)` → захватывает **автора или издателя** (не содержит запятую).  
#    - `,` → обязательный **разделитель** перед годом.  

# 3. **`\s*(\d{4})"`**  
#    - `\s*` → допускает пробелы перед годом.  
#    - `(\d{4})` → **четыре цифры**, указывающие **год публикации**.  
#    - `"` → закрывающая кавычка, чтобы строка была завершённой.