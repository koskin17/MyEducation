# Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records (unique by key "name") by merging information from all input_files argument (if we find user with already existing name from previous file we should ignore it). Use pretty printing for writing users to json-file.


# If the function cannot find input files we need to log information with error level  

# root - ERROR - File <file name> doesn't exist

# For example:
# user1.json : 
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# ]

# user2.json : 
# [{"name": "Bob1", "rate": 25, “languages": ["French"]},
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]

# If we execute parse_user(user3.json, user1.json, user2.json)
# then file user3.json should contain information:
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]

import json
import logging
import os

# Setting up logging
logging.basicConfig(level=logging.ERROR, format="root - %(levelname)s - %(message)s")

def parse_user(output_file, *input_files):
    """Collects unique records by key 'name' from JSON files and writes to output file."""
    unique_users = {}
    
    for file in input_files:
        if not os.path.exists(file):
            logging.error(f"File {file} doesn't exist")  # Log an error if the file does not exist
            continue
        
        with open(file, "r", encoding="utf-8") as f:
            try:
                users = json.load(f)  # Загружаем данные из JSON
            except json.JSONDecodeError:
                logging.error(f"File {file} contains invalid JSON format")
                continue
        
        # WorkWorking with downloaded data
        if isinstance(users, list):  # If the JSON contains a list of users
            for user in users:
                if "name" in user and user["name"] not in unique_users:
                    unique_users[user["name"]] = user
        elif isinstance(users, dict):  # If the JSON contains a single user as a dictionary
            if "name" in users and users["name"] not in unique_users:
                unique_users[users["name"]] = users

    # Write unique records to a JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(list(unique_users.values()), f, indent=4, ensure_ascii=False)  # Pretty-printing

# Пример использования
parse_user("user3.json", r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Task 06 Serialization\Task 2\user1.json", r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Task 06 Serialization\Task 2\user2.json")

### **Объяснение кода**
# ✅ **Настраиваем логирование** (`logging.ERROR`), чтобы логировать **ошибки** при отсутствии файлов или неверном формате JSON.  
# ✅ **Проходим по всем входным файлам** и загружаем данные из JSON, **пропуская несуществующие файлы** (`os.path.exists()`).  
# ✅ **Фильтруем уникальные записи по `name`** и сохраняем их в словарь `unique_users`.  
# ✅ **Обрабатываем JSON независимо от формата** (`list` пользователей или один `dict`).  
# ✅ **Записываем итоговые данные в `output_file`** в удобном формате (`indent=4` для читаемости).

# 💡 **Вывод:**  
# Этот код **правильно объединяет записи**, **игнорирует дубликаты**, **логирует ошибки** и **создаёт корректный JSON-файл**.  
# Попробуй запустить и скажи, если нужно что-то уточнить! 🚀
