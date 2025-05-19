# Class Student has attributes full_name:str, avg_rank: float, courses: list
# Class Group has attributes title: str, students: list.

# Make both classes JSON serializable. 

# Json-files represent information about student (students). 

# Create methods:  

# Student.from_json(json_file) that return Student instance from attributes from json-file;

# Student.serialize_to_json(filename)

# Group.serialize_to_json(list_of_groups, filename)

# Group.create_group_from_file(students_file)

# Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension).

import json
import os
from json import JSONEncoder

class Student:
    """The Student clas swith information about a student."""
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def serialize_to_json(self, filename: str):
        """Save the Student object to a JSON file."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self, f, cls=StudentEncoder, indent=4, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_file: str):
        """Create an instance of the Student class from a JSON file."""
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"File {json_file} not found!")
        
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return cls(**data)

    def __repr__(self):
        return f"Student({self.full_name}, {self.avg_rank}, {self.courses})"


class Group:
    """Group class for a group of students."""
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    @classmethod
    def create_group_from_file(cls, students_file: str):
        """Create a Group instance from a JSON file with a list of students."""
        if not os.path.exists(students_file):
            raise FileNotFoundError(f"File {students_file} not found")

        with open(students_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        students = [Student(**student_data) for student_data in data]  # Creating Student objects
        title = os.path.splitext(os.path.basename(students_file))[0]  # File name without extension is the group name

        return cls(title, students)

    @staticmethod
    def serialize_to_json(list_of_groups, filename: str):
        """Save the list of groups to a JSON file."""
        groups_data = [
            {"title": group.title, "students": [student.__dict__ for student in group.students]}
            for group in list_of_groups
        ]

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(groups_data, f, indent=4, ensure_ascii=False)

    def __repr__(self):
        return f"Group({self.title}, {len(self.students)} students)"


# Define a custom JSONEncoder for the Student class
class StudentEncoder(JSONEncoder):
    """Serialize Student objects to JSON."""
    def default(self, obj):
        if isinstance(obj, Student):
            return obj.__dict__  # Return the object attributes as a dictionary
        return super().default(obj)

# === 🔹 Пример использования ===
# Создание студентов вручную
student1 = Student("Alice Johnson", 4.5, ["Math", "Physics"])
student2 = Student("Bob Smith", 3.8, ["Biology", "Chemistry"])

# Сохранение студента в JSON-файл
student1.serialize_to_json("student1.json")

# Чтение студента из JSON-файла
loaded_student = Student.from_json("student1.json")
print(loaded_student)

# Создание группы из JSON-файла
group = Group.create_group_from_file("students.json")
print(group)

# Сохранение списка групп
Group.serialize_to_json([group], "groups.json")

### **Объяснение решения**
# ✅ **Класс `Student`**
# - **Сериализация** (`serialize_to_json`) → сохраняет объект в JSON-файл.
# - **Десериализация** (`from_json`) → загружает данные из JSON-файла и создаёт объект `Student`.
# - **`__dict__`** → конвертирует объект в словарь при сериализации.

# ✅ **Класс `Group`**
# - **Метод `create_group_from_file`** → загружает список студентов из JSON и создаёт объект `Group`.
# - **Метод `serialize_to_json`** → записывает список групп в JSON.
# - **Использование `os.path.splitext()`** → берёт **имя файла без расширения** как название группы.

# 📌 **Вывод:**  
# ✔ Поддерживается сериализация и десериализация.  
# ✔ Корректно создаются `Student` и `Group`.  
# ✔ Объекты можно сохранять и загружать из файлов.

# **Две звездочки (`**`) позволяют "распаковать" словарь** и передать его элементы как **именованные аргументы** (`key=value`) в функцию или метод.  

### 🔹 **Как это работает?**  
# Допустим, у нас есть словарь:
# data = {"name": "Alice", "age": 25}

# Если мы вызовем функцию так:  
# def greet(name, age):
#     print(f"Привет, {name}! Тебе {age} лет.")

# greet(**data)
# 🔹 Python **развернёт словарь** и передаст его как `greet(name="Alice", age=25)`.  
# 🔹 **Вывод:** `Привет, Alice! Тебе 25 лет.`  

### 🔹 **Где используется `**`?**
# ✅ **Передача аргументов в функцию**  
# ✅ **Создание объектов классов (`__init__(**data)`)**  
# ✅ **Объединение словарей** → `{**dict1, **dict2}`  
# ✅ **Динамическое изменение параметров (`kwargs`)**  

# 💡 **Вывод:**  
# 🚀 `**data` **распаковывает словарь** и делает код **гибким и удобным**.  
