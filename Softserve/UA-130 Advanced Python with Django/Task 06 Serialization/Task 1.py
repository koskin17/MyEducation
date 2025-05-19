# Create function find(file, key)

# This function parses json-file and returns all unique values of the key.

# 1.json:
# [{"name": "user_1”, "password": "pass_1”},
# {"name": "user_2”, "password": ["pass_1", "qwerty“]} ]

# find("1.json", "password") returns ["pass_1", "qwerty"]

# 2.json:
# [{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]

# find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]

# 3.json:
# {"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}

# find("3.json", "password") returns ["1234qweQWE"]

# Вот решение задачи:

import json

def find(file, key):
    """Function to find all unique values ​​of a key in a JSON file."""
    
    def extract_values(obj, key):
        """A recursive function to extract all values ​​of the key `key` from nested structures."""
        values = set()
        
        if isinstance(obj, dict):
            # If the object is a dictionary, check if the required key exists
            if key in obj:
                value = obj[key]
                if isinstance(value, list):
                    values.update(value)  # Add all the elements of the list
                else:
                    values.add(value)  # Add a single value
            
            # Recursively iterate through all nested dictionaries
            for v in obj.values():
                values.update(extract_values(v, key))
        
        elif isinstance(obj, list):
            # If the object is a list, iterate over the elements
            for item in obj:
                values.update(extract_values(item, key))
        
        return values

    # Reading the JSON file
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # print(list(extract_values(data, key)))
    # Extract unique key values
    return list(extract_values(data, key))

### **Подробное описание каждого этапа**
#### **1. Импорт модуля json**
# ✔ `import json` — загружаем модуль `json`, который позволяет работать с JSON-файлами.

#### **2. Определение функции `find(file, key)`**
# ✔ `find(file, key)` — принимает:
#     - `file` — имя JSON-файла.
#     - `key` — ключ, значения которого нужно извлечь.

#### **3. Вложенная функция `extract_values(obj, key)`**
# ✔ Эта рекурсивная функция нужна, чтобы **проходить вложенные структуры** (словари, списки) и находить значения указанного `key`.  
# ✔ **Почему рекурсия?** → JSON может быть **глубоко вложенным** (`credentials`, `password` внутри `credentials` и т. д.), поэтому простого перебора недостаточно.

##### 🔹 **Как `extract_values()` работает?**
# 1️⃣ **Если объект — `dict` (словарь)**  
#         - Проверяем, **есть ли нужный ключ (`key`)** в словаре.
#         - Если `key` содержит **список**, добавляем все его элементы (`values.update(value)`).
#         - Если `key` содержит **одно значение**, просто добавляем его (`values.add(value)`).
#         - Затем **проходимся по всем значениям словаря** и **рекурсивно вызываем `extract_values()`**.

# 2️⃣ **Если объект — `list` (список)**  
#    - Перебираем все элементы списка и **рекурсивно проверяем**, есть ли в них `key`.

# ✔ **Почему используем `set()`?**  
# **Чтобы исключить дубликаты!** Например, если `password` встречается дважды, `set()` оставит только уникальные значения.

#### **4. Чтение JSON-файла**
# with open(file, "r", encoding="utf-8") as f:
#     data = json.load(f)
#     ```
# ✔ **Открываем файл** в режиме чтения (`"r"`) и загружаем JSON-данные в переменную `data`.

#### **5. Извлечение уникальных значений ключа**
# return list(extract_values(data, key))

# ✔ **Вызываем `extract_values()`**, получаем **множество (`set`) значений**, затем **преобразуем в список (`list`)** для удобного вывода.

### **Примеры работы**
# 📌 **1.json**
# find("1.json", "password")  # Вывод: ["pass_1", "qwerty"]

# 📌 **2.json**
# find("2.json", "password")  # Вывод: ["1234qweQWE", "pass_1", "qwerty"]

# 📌 **3.json**
# find("3.json", "password")  # Вывод: ["1234qweQWE"]

# ### **Почему это решение правильное?**
# ✅ **Работает для любых JSON-структур** (списки, вложенные словари).  
# ✅ **Удаляет дубликаты** → `set()` хранит только **уникальные значения**.  
# ✅ **Рекурсивно проходит вложенные уровни** (`credentials`, `password` внутри `credentials`).  
# ✅ **Гибкое и универсальное** — можно искать **любой ключ** (не только `password`).

# 1.json:
# [{"name": "user_1", "password": "pass_1"}, {"name": "user_2", "password": ["pass_1", "qwerty"]}]
find(r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Task 06 Serialization\1.json", "password") #returns ["pass_1", "qwerty"]

# 2.json:
# [{"name": "user_1", "credentials": {"username": "user_user", "password": "1234qweQWE"}}, {"name": "user_2", "password": ["pass_1 ", "qwerty "]}]
find(r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Task 06 Serialization\2.json", "password") #returns ["1234qweQWE", "pass_1", "qwerty"]

# # 3.json:
# {"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
find(r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Task 06 Serialization\3.json", "password") #returns ["1234qweQWE"]