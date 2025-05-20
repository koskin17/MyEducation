# Есть задача:
# Follow the link: https://classroom.github.com/a/1a2Fc0jK

# After the repository is created, clone it locally:

# git clone <your repository URL>
 
# Implement the following task in the university.py file:

#           You are given two JSON files:

# users.json — contains information about users in the following format:
#                  [ { "id": 1, "name": "userName", "department_id": 1 }, ... ]
# departments.json — contains information about departments in the following format:

# [ { "id": 1, "name": "departmentName" }, ... ]          
#           Create appropriate JSON Schemas to validate the structure of users.json and  departments.json.

#            Implement the functions:

# user_with_department(csv_file, user_json, department_json):
#                     This function should:

# Read data from the provided JSON files.

# Create a CSV file with the following format:

#           header line - name, department
#           next lines :  <userName>, <departmentName>
# If a user refers to a department_id that doesn't exist in departments.json, raise a DepartmentName exception.

# If the data does not match the schema, raise an InvalidInstanceError exception.
 
# validate_json(data, schema):
# which validates a JSON instance against a schema.

# Commit and push your solution to the GitHub repository.

# import json
# import jsonschema
# from jsonschema import validate
# import csv

# student_schema = {
#     #type schema here
#     }

# department_schema = {
#     #type schema here
#     }

# # type your code here

# ОБЪЯСНЕНИЕ Akademy GPT
## 📌 Цель задачи:
# Ты должен:
# 1. ✅ Создать **JSON-схемы** для валидации `users.json` и `departments.json`.
# 2. ✅ Написать функцию `validate_json(data, schema)` для проверки данных по схеме.
# 3. ✅ Написать функцию `user_with_department(csv_file, user_json, department_json)`, которая:
#    * Загружает пользователей и департаменты из JSON-файлов
#    * Валидирует их по схемам
#    * Создаёт CSV-файл с колонками `name, department`
#    * Если `department_id` у пользователя не существует в департаментах — выбрасывает исключение `DepartmentName`
#    * Если JSON невалидный — выбрасывает `InvalidInstanceError`

## 🔨 Шаг 1. Напишем схемы `student_schema` и `department_schema`
# student_schema = {
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             "id": {"type": "integer"},
#             "name": {"type": "string"},
#             "department_id": {"type": "integer"}
#         },
#         "required": ["id", "name", "department_id"]
#     }
# }

# department_schema = {
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             "id": {"type": "integer"},
#             "name": {"type": "string"}
#         },
#         "required": ["id", "name"]
#     }
# }

# # Эти схемы говорят, что:
# # * данные — это список (`"type": "array"`),
# # * каждый элемент — объект (`"type": "object"`),
# # * у объекта есть нужные поля и правильные типы.

# ## 🧠 Шаг 2. Функция `validate_json(data, schema)`
# class InvalidInstanceError(Exception):
#     pass

# def validate_json(data, schema):
#     try:
#         validate(instance=data, schema=schema) # функция python, которая валидирует полученные данные с указанной схемой
#     except jsonschema.exceptions.ValidationError as e:
#         raise InvalidInstanceError(f"Invalid JSON structure: {e.message}")

# ## 💥 Шаг 3. Ошибка `DepartmentName`
# class DepartmentName(Exception):
#     pass

# ## ✍️ Шаг 4. Функция `user_with_department(...)`
# def user_with_department(csv_file, user_json, department_json):
#     # 1. Загрузка данных
#     with open(user_json, encoding='utf-8') as f:
#         users = json.load(f)

#     with open(department_json, encoding='utf-8') as f:
#         departments = json.load(f)

#     # 2. Валидация
#     validate_json(users, student_schema)
#     validate_json(departments, department_schema)

#     # 3. Преобразуем список департаментов в словарь для быстрого доступа
#     department_dict = {dept['id']: dept['name'] for dept in departments}

#     # 4. Готовим CSV-файл
#     with open(csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['name', 'department'])  # первой строкой в файл записываем заголовки

#         for user in users:
#             dept_id = user['department_id']
#             if dept_id not in department_dict:
#                 raise DepartmentName(f"Department with ID {dept_id} not found.")
#             dept_name = department_dict[dept_id]
#             writer.writerow([user['name'], dept_name])

# ## 🧪 Пример структуры JSON:
# ### `users.json`
# [
#     { "id": 1, "name": "Alice", "department_id": 2 },
#     { "id": 2, "name": "Bob", "department_id": 3 }
# ]

# ### `departments.json`
# [
#     { "id": 2, "name": "Math" },
#     { "id": 3, "name": "Physics" }
# ]

## 📂 Структура `university.py` в итоге:
import json
import jsonschema
from jsonschema import validate
import csv
import os
from pathlib import Path


# JSON Schemas
student_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "department_id": {"type": "integer"}
        },
        "required": ["id", "name", "department_id"]
    }
}

department_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
    }
}

# Custom Exceptions
class InvalidInstanceError(Exception):
    pass

class DepartmentName(Exception):
    pass

# Validator
def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise InvalidInstanceError(f"Invalid JSON structure: {e.message}")

# Main function
def user_with_department(csv_file, user_json, department_json):
    
    with open(user_json, encoding='utf-8') as f:
        users = json.load(f)

    with open(department_json, encoding='utf-8') as f:
        departments = json.load(f)

    validate_json(users, student_schema)
    validate_json(departments, department_schema)

    department_dict = {dept['id']: dept['name'] for dept in departments}

    with open(csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'department'])

        for user in users:
            dept_id = user['department_id']
            if dept_id not in department_dict:
                raise DepartmentName(f"Department with ID {dept_id} not found.")
            dept_name = department_dict[dept_id]
            writer.writerow([user['name'], dept_name])

## ✅ Что делать дальше:
# 1. 🔁 Проверь, что `users.json` и `departments.json` лежат в твоей папке с репозиторием.
# 2. 🧪 Можешь запустить функцию вручную:

script_path = Path(__file__).resolve()  # Полный путь к файлу
print(script_path)

user_with_department("out.csv", "users.json", "departments.json")

# 3. ✅ Убедись, что `out.csv` содержит нужные строки.
# 4. 💾 Закоммить и пуш на GitHub:






# ОБЪЯСНЕНИЕ ОТ COPILOT
# Ниже приведён подробный план решения задачи вместе с примером кода и объяснениями на каждом шаге. Мы реализуем следующие моменты:
# 1. **JSON-схемы для проверки данных**  
#    Мы должны убедиться, что входные JSON-файлы соответствуют ожидаемой структуре.
# 2. **Функцию `validate_json(data, schema)`**  
#    Эта функция будет принимать данные и схему, а затем проверять данные с помощью библиотеки `jsonschema`. Если данные не удовлетворяют схеме, мы перехватываем исключение и выдаём (или переопределяем) свое исключение `InvalidInstanceError`.
# 3. **Функцию `user_with_department(csv_file, user_json, department_json)`**  
#    В этой функции мы:
#    - Откроем и загрузим JSON-файлы с пользователями и департаментами.
#    - Проверим, что данные удовлетворяют нашим схемам, вызвав `validate_json`.
#    - Сформируем словарь из департаментов, чтобы по `id` быстро найти имя департамента.
#    - Пройдём по записям пользователей. Если какой-либо пользователь ссылается на несуществующий `department_id` в словаре, выбросим исключение `DepartmentName`.
#    - Создадим CSV-файл, куда запишем строки в формате: `имя пользователя, имя департамента`.
# 4. **Определение кастомных исключений**  
#    Нам нужно определить два исключения:
#    - `DepartmentName` – выбрасывается, если у пользователя указан несуществующий `department_id`.
#    - `InvalidInstanceError` – выбрасывается, если данные не удовлетворяют схеме (это можно делать на уровне `validate_json`).

# Ниже приведён пример полного содержимого файла `university.py` с комментариями:
# import json
# import jsonschema
# from jsonschema import validate
# import csv

# Определяем кастомные исключения
class DepartmentName(Exception):
    """Выбрасываем, если у пользователя указан несуществующий department_id."""
    pass

class InvalidInstanceError(Exception):
    """Выбрасываем, если данные не удовлетворяют JSON-схеме."""
    pass

# JSON-схема для файла users.json
# Ожидается, что users.json — это массив объектов, где каждый объект имеет поля:
# 'id' (целое число), 'name' (строка), 'department_id' (целое число)
student_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "department_id": {"type": "integer"}
        },
        "required": ["id", "name", "department_id"]
    }
}

# JSON-схема для файла departments.json
# Ожидается, что departments.json — это массив объектов, где каждый объект имеет поля:
# 'id' (целое число), 'name' (строка)
department_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
    }
}

# def validate_json(data, schema):
#     """
#     Функция для валидации JSON-данных по заданной схеме.
    
#     Если данные не удовлетворяют схеме, выбрасывает InvalidInstanceError.
#     """
#     try:
#         validate(instance=data, schema=schema)
#     except jsonschema.exceptions.ValidationError as e:
#         raise InvalidInstanceError(f"Данные не удовлетворяют схеме: {e}")

# def user_with_department(csv_file, user_json, department_json):
#     """
#     Функция, которая читает пользователей и департаменты из JSON-файлов,
#     проверяет их на соответствие схемам и создаёт CSV-файл, где для каждого пользователя
#     указано его имя и название департамента.
    
#     Если для пользователя не находится department_id в departments.json, выбрасывается исключение DepartmentName.
#     Если данные не соответствуют схеме, выбрасывается InvalidInstanceError.
#     """

#     # 1. Открываем и загружаем данные из JSON-файлов
#     with open(user_json, 'r', encoding='utf-8') as f:
#         users = json.load(f)
        
#     with open(department_json, 'r', encoding='utf-8') as f:
#         departments = json.load(f)
    
#     # 2. Валидация загруженных данных по JSON-схемам
#     validate_json(users, student_schema)
#     validate_json(departments, department_schema)
    
#     # 3. Создаём словарь для быстрого поиска названия департамента по id
#     dept_dict = {dept['id']: dept['name'] for dept in departments}
    
#     # 4. Создаём CSV-файл и записываем данные
#     with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         # Записываем заголовок
#         writer.writerow(['name', 'department'])
        
#         # Обрабатываем каждого пользователя
#         for user in users:
#             dept_id = user.get('department_id')
#             # Если department_id не найден в словаре departments – выбрасываем исключение
#             if dept_id not in dept_dict:
#                 raise DepartmentName(f"У пользователя '{user.get('name')}' указан несуществующий department_id: {dept_id}")
#             writer.writerow([user.get('name'), dept_dict[dept_id]])

# Пример вызова функций:
# user_with_department("output.csv", "users.json", "departments.json")

### Пошаговое объяснение:
# 1. **JSON-схемы:**  
#    - В `student_schema` мы описываем, что данные должны быть массивом объектов, где каждый объект имеет обязательные поля:
#      - `"id": {"type": "integer"}`
#      - `"name": {"type": "string"}`
#      - `"department_id": {"type": "integer"}`
#    - В `department_schema` задаём, что в каждом объекте обязательно должны быть поля:
#      - `"id": {"type": "integer"}`
#      - `"name": {"type": "string"}`

# 2. **Функция `validate_json`:**  
#    - Эта функция использует метод `validate` из библиотеки `jsonschema` и проверяет, соответствует ли переданный JSON заданной схеме.
#    - В случае ошибки валидации перехватываем её и выбрасываем своё исключение `InvalidInstanceError`.

# 3. **Функция `user_with_department`:**  
#    - Сначала данные загружаются из файлов с помощью `json.load()`.
#    - Затем для пользователей и департаментов вызывается `validate_json`, чтобы убедиться, что структура данных корректна. Если данные не проходят валидацию, функция завершится с исключением.
#    - Создаётся словарь `dept_dict`, где ключ – это `id` департамента, а значение – его имя. Это необходимо для быстрого поиска.
#    - Функция переходит к записи CSV-файла:
#      - Записывается строка-заголовок.
#      - Для каждого пользователя проверяется, существует ли его `department_id` в словаре департаментов. Если нет – выбрасывается `DepartmentName` с соответствующим сообщением.
#      - Если всё в порядке, в CSV записываются имя пользователя и имя департамента.
     
# 4. **Коммит и push:**  
#    - Как только решение реализовано и протестировано, нужно закоммитить и запушить изменения в GitHub-репозиторий.
#    - Например:
#      ```bash
#      git add university.py
#      git commit -m "Реализована функция user_with_department и валидация JSON"
#      git push origin master  # или main, если ветка main

# Таким образом, ты создаёшь решение, которое:
# - Проверяет входные JSON-файлы на корректность структуры с помощью JSON-схем;
# - Если данные не удовлетворяют схеме, выбрасывает исключение `InvalidInstanceError`;
# - Если пользователь ссылается на несуществующий департамент, выбрасывает исключение `DepartmentName`;
# - Успешно генерирует CSV-файл, связывающий имена пользователей с именами департаментов.
 