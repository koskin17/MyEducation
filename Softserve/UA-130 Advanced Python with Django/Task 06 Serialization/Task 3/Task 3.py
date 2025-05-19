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
    """Student class with information about the student."""
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def serialize_to_json(self, filename: str):
        """Сохраняет объект Student в JSON-файл."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self, f, cls=StudentEncoder, ensure_ascii=False) # Здесь вызывается кастомный StudentEncoder, который переопределён ниже в коде

    @classmethod
    def from_json(cls, json_file: str):
        """Создаёт экземпляр Student из JSON-файла."""
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"File {json_file} not found!")
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Если загруженные данные оказались списком, берём первый (на всякий случай).
        if isinstance(data, list):
            if not data:
                raise ValueError("Empty student list in file")
            data = data[0]
        return cls(**data)

    def __str__(self):
        # Тесты ожидают вывод вида:
        # "Student2 from group2 (50.4): ['C++']"
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    def __repr__(self):
        return self.__str__()

        # ## 📌 РАЗНИЦА МЕЖДУ __str__ и __repr__?
        # | Метод      | Для чого використовується                                | Приклад виклику                          |
        # | ---------- | -------------------------------------------------------- | ---------------------------------------- |
        # | `__str__`  | Для **людей** – гарне, читабельне представлення          | `print(obj)`                             |
        # | `__repr__` | Для **розробників** – технічне, однозначне представлення | `obj` в `REPL`, списках, або `repr(obj)` |

        # ## 🧪 Приклад:
        # class Dog:
        #     def __init__(self, name):
        #         self.name = name

        #     def __str__(self):
        #         return f"Це песик {self.name}"

        #     def __repr__(self):
        #         return f"Dog('{self.name}')"

        # d = Dog("Барон")

        # print(d)           # Викликає __str__ → Це песик Барон
        # print([d])         # Викликає __repr__ → [Dog('Барон')]

        # ## ❓ А якщо визначити лише `__str__`, а `__repr__` не писати?
        # Python автоматично буде використовувати **базовий `__repr__`** типу:
        # ```
        # <__main__.Dog object at 0x000001234>
        # ```
        # 👎 Це технічне і неінформативне представлення.
        # ---
        # ## ✅ Тому ми часто пишемо:
        # ```python
        # def __repr__(self):
        #     return self.__str__()
        # ```
        # 🟢 Це означає: якщо Python хоче технічний вигляд, показуй той самий текст, що й для людей.
        # ---
        # ## 📌 Підсумок:
        # | Якщо ти...                                    | То роби так ✅                              |
        # | --------------------------------------------- | ------------------------------------------ |
        # | Хочеш гарний `print(obj)`                     | Реалізуй `__str__`                         |
        # | Хочеш гарне представлення в списках, логах    | Реалізуй `__repr__`, або скопіюй `__str__` |
        # | Хочеш окремі: технічне (repr) і красиве (str) | Реалізуй обидва по-різному                 |
        # ---
        # ## ✨ Висновок:
        # > 🔧 Якщо ти вже маєш `__str__` і не хочеш окремий технічний `__repr__`, просто:
        # ```python
        # def __repr__(self):
        #     return self.__str__()
        # ```
        # Це повністю правильно і зручно для читабельного коду.

class Group:
    """Класс Group для группы студентов."""
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    @classmethod
    def create_group_from_file(cls, students_file: str):
        """
        Создаёт экземпляр Group из JSON-файла содержащего информацию о студентах.
        Название группы берётся из имени файла (без расширения).
        
        Примечание:
         - Если файл содержит единственного студента (словарь), то оборачиваем его в список,
           чтобы работать с данными единообразно.
        """
        if not os.path.exists(students_file):
            raise FileNotFoundError(f"File {students_file} not found")
        with open(students_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            print()
            print(f"Содержимое data при разгрузке через json.load:{data}")
            print()
        # Если данные – это словарь (один студент), оборачиваем в список.
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            raise ValueError(f"Expected list or dict in {students_file}, got {type(data).__name__}")
        students = []
        for student_data in data:
            if not isinstance(student_data, dict):
                raise TypeError("Each student record must be a dictionary")
            students.append(Student(**student_data))
        # Название группы – имя файла без расширения.
        title = os.path.splitext(os.path.basename(students_file))[0]
        return cls(title, students)

    @staticmethod
    def serialize_to_json(list_of_groups, filename: str):
        """
        Сохраняет список групп в JSON-файл.
        **Важно:** JSON должен быть записан в компактном виде (без отступов), чтобы соответствовать тестам.
        """
        groups_data = [
            {"title": group.title, "students": [student.__dict__ for student in group.students]}
            for group in list_of_groups
        ]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(groups_data, f, ensure_ascii=False)

    def __str__(self):
        """
        Формирует строку в виде:
        2020_2: ["Student 1 from second Group (98): ['Python']", "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]
        """
        # Для каждого студента вызываем __str__ (который уже форматирован по требованиям)
        students_str = [str(student) for student in self.students]
        return f"{self.title}: {students_str}"

    def __repr__(self):
        return self.__str__()

class StudentEncoder(JSONEncoder):
    """Кастомный JSONEncoder для сериализации объектов Student."""
    def default(self, obj):
        if isinstance(obj, Student):
            return obj.__dict__
        return super().default(obj)

## 📦 Імпорт модулів
# ```python
# import json
# import os
# from json import JSONEncoder

# * `json` — стандартний модуль Python для роботи з JSON: серіалізація (перетворення об'єктів у JSON) та десеріалізація (з JSON у об'єкти).
# * `os` — модуль для взаємодії з операційною системою, зокрема для перевірки існування файлів та роботи з шляхами.
# * `JSONEncoder` — базовий клас для створення власних енкодерів, які дозволяють серіалізувати нестандартні об'єкти.

## 🎓 Клас `Student`
# class Student:
#     """Клас Student з інформацією про студента."""
#     def __init__(self, full_name: str, avg_rank: float, courses: list):
#         self.full_name = full_name
#         self.avg_rank = avg_rank
#         self.courses = courses
# * `__init__` — конструктор класу, який ініціалізує атрибути:
#   * `full_name` — повне ім'я студента.
#   * `avg_rank` — середній бал.
#   * `courses` — список курсів, які проходить студент.

### 💾 Метод `serialize_to_json`
#     def serialize_to_json(self, filename: str):
#         """
#         Зберігає об'єкт Student у JSON-файл.
#         **Важливо:** для проходження тесту JSON повинен бути записаний у компактному вигляді, без відступів.
#         """
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(self, f, cls=StudentEncoder, ensure_ascii=False)

# * Відкриває файл для запису з кодуванням UTF-8.
# * `json.dump` — серіалізує об'єкт `self` у JSON та записує у файл.

#   * `cls=StudentEncoder` — використовується власний енкодер для серіалізації об'єкта `Student`.
#   * `ensure_ascii=False` — дозволяє зберігати символи Unicode (наприклад, українські літери) без екранування.

### 📥 Метод `from_json`
    # @classmethod
    # def from_json(cls, json_file: str):
    #     """
    #     Створює екземпляр Student з JSON-файлу.
    #     Файл повинен містити JSON-об'єкт (словник), а не список.
    #     """
    #     if not os.path.exists(json_file):
    #         raise FileNotFoundError(f"Файл {json_file} не знайдено!")
    #     with open(json_file, "r", encoding="utf-8") as f:
    #         data = json.load(f)
    #     # Якщо завантажені дані є списком, беремо перший елемент.
    #     if isinstance(data, list):
    #         if not data:
    #             raise ValueError("Порожній список студентів у файлі")
    #         data = data[0]
    #     return cls(**data)

# * Перевіряє існування файлу.
# * Відкриває файл для читання з кодуванням UTF-8.
# * `json.load` — десеріалізує JSON у Python-об'єкт.
# * Якщо дані — список, бере перший елемент (припускаючи, що файл містить одного студента).
# * Повертає новий екземпляр `Student`, розпаковуючи словник `data` у параметри конструктора.

### 🖨️ Метод `__str__`
    # def __str__(self):
    #     # Тести очікують вивід у форматі:
    #     # "Student2 from group2 (50.4): ['C++']"
    #     return f"{self.full_name} ({self.avg_rank}): {self.courses}"
# * Повертає рядкове представлення об'єкта `Student` у заданому форматі.

### 🧾 Метод `__repr__`
    # def __repr__(self):
    #     return self.__str__()
# * Повертає те саме, що і `__str__`, для зручності відображення у списках та інших структурах.

## 👥 Клас `Group`
# class Group:
#     """Клас Group для групи студентів."""
#     def __init__(self, title: str, students: list):
#         self.title = title
#         self.students = students
# * `title` — назва групи.
# * `students` — список об'єктів `Student`.

### 🏗️ Метод `create_group_from_file`
    # @classmethod
    # def create_group_from_file(cls, students_file: str):
    #     """
    #     Створює екземпляр Group з JSON-файлу, що містить інформацію про студентів.
    #     Назва групи береться з імені файлу (без розширення).
    #     """
    #     if not os.path.exists(students_file):
    #         raise FileNotFoundError(f"Файл {students_file} не знайдено")
    #     with open(students_file, "r", encoding="utf-8") as f:
    #         data = json.load(f)
    #     # Якщо дані — словник (один студент), обгортаємо у список.
    #     if isinstance(data, dict):
    #         data = [data]
    #     elif not isinstance(data, list):
    #         raise ValueError(f"Очікувався список або словник у {students_file}, отримано {type(data).__name__}")
    #     students = []
    #     for student_data in data:
    #         if not isinstance(student_data, dict):
    #             raise TypeError("Кожен запис студента повинен бути словником")
    #         students.append(Student(**student_data))
    #     # Назва групи — ім'я файлу без розширення.
    #     title = os.path.splitext(os.path.basename(students_file))[0]
    #     return cls(title, students)

# * Перевіряє існування файлу.
# * Відкриває файл для читання з кодуванням UTF-8.
# * Десеріалізує JSON у Python-об'єкт.
# * Якщо дані — словник, обгортає у список.
# * Створює список об'єктів `Student`.
# * Визначає назву групи з імені файлу.
# * Повертає новий екземпляр `Group`.

### 💾 Метод `serialize_to_json`
    # @staticmethod
    # def serialize_to_json(list_of_groups, filename: str):
    #     """
    #     Зберігає список груп у JSON-файл.
    #     **Важливо:** JSON повинен бути записаний у компактному вигляді (без відступів), щоб відповідати тестам.
    #     """
    #     groups_data = [
    #         {"title": group.title, "students": [student.__dict__ for student in group.students]}
    #         for group in list_of_groups
    #     ]
    #     with open(filename, "w", encoding="utf-8") as f:
    #         json.dump(groups_data, f, ensure_ascii=False)
# * Створює список словників, що представляють групи та їх студентів.
# * Відкриває файл для запису з кодуванням UTF-8.
# * Серіалізує список груп у JSON та записує у файл.

# Может быть написан с использованием indent:
# def serialize_to_json(self, filename: str):
#         """Save the Student object to a JSON file."""
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(self, f, cls=StudentEncoder, indent=4, ensure_ascii=False)

#         # 🔹 **Параметр `indent=4`** в `json.dump()` отвечает за **форматирование JSON-данных** при записи в файл.
#         # ### **📌 Что делает `indent=4`?**
#         # - Указывает, что **каждый уровень вложенности** будет **сдвигаться на 4 пробела**.
#         # - Делает JSON-файл **читабельным**, добавляя отступы и переносы строк.
#         # ### **🛠 Пример использования**
#         # #### ❌ **Без `indent` (компактный JSON)**
#         # import json
#         # data = {"name": "Alice", "age": 25, "courses": ["Math", "Physics"]}
#         # with open("compact.json", "w", encoding="utf-8") as f:
#         #     json.dump(data, f)  # Без форматирования
#         # # Вывод compact.json:
#         # # {"name":"Alice","age":25,"courses":["Math","Physics"]}
#         # #### ✅ **С `indent=4` (отформатированный JSON)**
#         # with open("pretty.json", "w", encoding="utf-8") as f:
#         #     json.dump(data, f, indent=4)  # Форматирование с отступами
#         # ✔ **Теперь JSON выглядит так:**
#         # {
#         #     "name": "Alice",
#         #     "age": 25,
#         #     "courses": [
#         #         "Math",
#         #         "Physics"
#         #     ]
#         # }
#         # ### **💡 Итог**
#         # 🚀 `indent=4` делает JSON **красиво отформатированным** и удобным для чтения.  
#         # Если данные **не надо сжимать**, лучше включить этот параметр!

### 🖨️ Метод `__str__`
    # def __str__(self):
    #     """
    #     Формує рядок у вигляді:
    #     2020_2: ["Student 1 from second Group (98): ['Python']", "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]
    #     """
    #     students_str = [str(student) for student in self.students]
    #     return f"{self.title}: {students_str}"
# * Повертає рядкове представлення групи та її студентів у заданому форматі.

### 🧾 Метод `__repr__`
    # def __repr__(self):
    #     return self.__str__()
# * Повертає те саме, що і `__str__`, для зручності відображення у списках та інших структурах.

## 🛠️ Клас `StudentEncoder`
# class StudentEncoder(JSONEncoder):
#     """Кастомний JSONEncoder для серіалізації об'єктів Student."""
#     def default(self, obj):
#         if isinstance(obj, Student):
#             return obj.__dict__
#         return super().default(obj)
# * Наслідується від `JSONEncoder`.
# * Перевизначає метод `default`, щоб серіалізувати об'єкти `Student` у словники.
# * Якщо об'єкт не є `Student`, викликає метод `default` базового класу.

## ✅ Підсумок
# Цей код дозволяє:
# * Створювати об'єкти `Student` та `Group`.
# * Серіалізувати їх у JSON-файли.
# * Десеріалізувати з JSON-файлів.
# * Виводити об'єкти у зручному для читання форматі.

# ДАЛЬШЕ ИДУТ ВАРИНАТЫ КОДА С ОШИБКАМИ, КОТОРЫЕ ИСПРАВЛЯЛИСЬ, И ОБЪЯСНЕНИЕМ ИСПРАВЛЕНИЙ

# import json
# import os
# from json import JSONEncoder

# class Student:
#     """Student class with information about the student."""
#     def __init__(self, full_name: str, avg_rank: float, courses: list):
#         self.full_name = full_name
#         self.avg_rank = avg_rank
#         self.courses = courses

#     def serialize_to_json(self, filename: str):
#         """Save the Student object to a JSON file."""
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(self, f, cls=StudentEncoder, indent=4, ensure_ascii=False)

#         # 🔹 **Параметр `indent=4`** в `json.dump()` отвечает за **форматирование JSON-данных** при записи в файл.
#         # ### **📌 Что делает `indent=4`?**
#         # - Указывает, что **каждый уровень вложенности** будет **сдвигаться на 4 пробела**.
#         # - Делает JSON-файл **читабельным**, добавляя отступы и переносы строк.
#         # ### **🛠 Пример использования**
#         # #### ❌ **Без `indent` (компактный JSON)**
#         # import json
#         # data = {"name": "Alice", "age": 25, "courses": ["Math", "Physics"]}
#         # with open("compact.json", "w", encoding="utf-8") as f:
#         #     json.dump(data, f)  # Без форматирования
#         # # Вывод compact.json:
#         # # {"name":"Alice","age":25,"courses":["Math","Physics"]}
#         # #### ✅ **С `indent=4` (отформатированный JSON)**
#         # with open("pretty.json", "w", encoding="utf-8") as f:
#         #     json.dump(data, f, indent=4)  # Форматирование с отступами
#         # ✔ **Теперь JSON выглядит так:**
#         # {
#         #     "name": "Alice",
#         #     "age": 25,
#         #     "courses": [
#         #         "Math",
#         #         "Physics"
#         #     ]
#         # }
#         # ### **💡 Итог**
#         # 🚀 `indent=4` делает JSON **красиво отформатированным** и удобным для чтения.  
#         # Если данные **не надо сжимать**, лучше включить этот параметр!

#     @classmethod
#     def from_json(cls, json_file: str):
#         """Creating a Student instance from a JSON file."""
#         if not os.path.exists(json_file):
#             raise FileNotFoundError(f"File {json_file} not found!")
#         with open(json_file, "r", encoding="utf-8") as f:
#             data = json.load(f)
#         if not isinstance(data, dict):
#             raise ValueError(f"Expected JSON object in {json_file}, got {type(data).__name__}")
#         return cls(**data)

#     def __repr__(self):
#         return f"Student({self.full_name}, {self.avg_rank}, {self.courses})"

#     def __str__(self):
#         # Override __str__
#         return f"{self.full_name} ({self.avg_rank}): {self.courses}"

# class Group:
#     """Group class for a group of students."""
#     def __init__(self, title: str, students: list):
#         self.title = title
#         self.students = students

#     @classmethod
#     def create_group_from_file(cls, students_file: str):
#         """
#         Creates a Group instance from a JSON file containing student information.
#         If the file does not store a list, but a single student (dictionary),
#         then it is wrapped in a list. The group name is the file name without the extension.
#         """
#         if not os.path.exists(students_file):
#             raise FileNotFoundError(f"File {students_file} not found")
#         with open(students_file, "r", encoding="utf-8") as f:
#             data = json.load(f)
#         # If the data read is a dictionary (one student), wrap it in a list.
#         if isinstance(data, dict):
#             data = [data]
#         elif not isinstance(data, list):
#             raise ValueError(
#                 f"Expected list or dict in {students_file}, got {type(data).__name__}"
#             )
#         # Create Student objects from each dictionary.
#         students = []
#         for student_data in data:
#             if not isinstance(student_data, dict):
#                 # If by mistake we received something other than a dictionary, we throw a clear exception.
#                 raise TypeError("Each student data must be a dictionary")
#             students.append(Student(**student_data))
#         # Group name - file name without extension.
#         title = os.path.splitext(os.path.basename(students_file))[0]
#         return cls(title, students)

#     @staticmethod
#     def serialize_to_json(list_of_groups, filename: str):
#         """Save the list of groups to a JSON file."""
#         groups_data = [
#             {"title": group.title, "students": [student.__dict__ for student in group.students]}
#             for group in list_of_groups
#         ]
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(groups_data, f, indent=4, ensure_ascii=False)

#     def __repr__(self):
#         return f"Group({self.title}, {len(self.students)} students)"

# # Define a custom JSONEncoder for the Student class.
# class StudentEncoder(JSONEncoder):
#     """Сериализует объекты Student в JSON."""
#     def default(self, obj):
#         if isinstance(obj, Student):
#             return obj.__dict__  # Returns the object's attributes as a dictionary.
#         return super().default(obj)

### Объяснение причин ошибок и внесённых исправлений
# 1. **Формат вывода строки студента (__str__)**  
#    **Проблема:**  
#    - Тесты ожидали вывод вида  
#      `"Student2 from group2 (50.4): ['C++']"`
#      вместо  
#      `"Student(Student2 from group2, 50.4, ['C++'])"`.
     
#    **Решение:**  
#    - Был добавлен метод `__str__` (в дополнение к уже существующему `__repr__`), который возвращает строку в требуемом формате:
#      ```python
#      def __str__(self):
#          return f"{self.full_name} ({self.avg_rank}): {self.courses}"
#      ```
#    - Таким образом, функция `print(user1)` теперь использует `__str__` и вывод совпадает с ожидаемым.

# 2. **Проблема при создании группы из файла**  
#    **Ошибка:**  
#    - При вызове `Group.create_group_from_file("2020-01.json")` возникала ошибка:
#      ```
#      TypeError: __main__.Student() argument after ** must be a mapping, not str
#      ```
#    **Причина:**  
#    - Файл `"2020-01.json"` содержит информацию об одном студенте в виде словаря (например, `{"full_name": "Student2 from group2", ...}`), а не список словарей.
#    - Итерация по словарю приводит к получению ключей (строк), а не вложенных словарей. При попытке выполнить `Student(**student_data)` для строки возникает ошибка.
     
#    **Решение:**  
#    - В методе `Group.create_group_from_file` добавлена проверка: если считанные данные являются словарём, то они оборачиваются в список:
#      ```python
#      if isinstance(data, dict):
#          data = [data]
#      ```
#    - Теперь вне зависимости от формата файла (одиночный студент или список студентов) создаётся корректный список.

# 3. **Остальные моменты**  
#    - **Метод `Student.from_json`**  
#      Ожидает, что в файле содержится JSON-объект (словарь). Если файл содержит не словарь, генерируется ошибка с понятным сообщением.
#    - **Метод `serialize_to_json` для группы**  
#      Перебирает список групп и сериализует список студентов через получение их `__dict__`, что соответствует требуемому формату.
#    - **StudentEncoder**  
#      Если объект является экземпляром `Student`, метод `default` возвращает его атрибуты в виде словаря. Для всех остальных объектов вызывается родительский метод.

### Примеры использования (с тестовыми данными)
# Предположим, содержимое файла `"2020-01.json"`:
# ```json
# {
#     "full_name": "Student2 from group2",
#     "avg_rank": 50.4,
#     "courses": ["C++"]
# }
# ```
# Тогда вызовы:
# ```python
# user1 = Student.from_json("2020-01.json")
# print(user1)
# ```
# выведут:
# ```
# Student2 from group2 (50.4): ['C++']
# ```

# Если содержимое файла `"2020_2.json"` выглядит так:
# ```json
# [
#     {"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]},
#     {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": ["Ruby", "Python", "Frontend development"]}
# ]
# ```
# то использование
# ```python
# with open("2020_2.json") as read_file:
#     data = json.load(read_file)
# print([str(Student(**item)) for item in data])
# ```
# выведет:
# ```
# ["Student 1 from second Group (98): ['Python']", "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]
# ```

# И, наконец, для групп:
# ```python
# g1 = Group.create_group_from_file("2020_2.json")
# g2 = Group.create_group_from_file("2020-01.json")
# Group.serialize_to_json([g1, g2], "g1.json")
# ```
# содержимое файла `"g1.json"` будет следующим:
# ```json
# [
#     {
#         "title": "2020_2",
#         "students": [
#             {
#                 "full_name": "Student 1 from second Group",
#                 "avg_rank": 98,
#                 "courses": ["Python"]
#             },
#             {
#                 "full_name": "Student 2 from second Group",
#                 "avg_rank": 70.34,
#                 "courses": ["Ruby", "Python", "Frontend development"]
#             }
#         ]
#     },
#     {
#         "title": "2020-01",
#         "students": [
#             {
#                 "full_name": "Student2 from group2",
#                 "avg_rank": 50.4,
#                 "courses": ["C++"]
#             }
#         ]
#     }
# ]

### Итог

# - Добавление метода `__str__` помогает получить требуемый формат при выводе объектов Student.
# - Обработка случая, когда JSON-файл с информацией о студентах является не списком, а одиночным объектом (словарём), решает ошибку с распаковкой аргументов.
# - Остальные изменения обеспечивают универсальную работу методов сериализации и десериализации.

# Попробуй запустить исправленный код с тестовыми файлами. Если возникнут вопросы или понадобится дополнительное объяснение, обязательно дай знать!

# 📌 **Два случая работы `StudentEncoder`**  
### **✅ Случай 1: Сериализация объекта `Student` (он превращается в словарь)**
# import json
# from json import JSONEncoder

# class Student:
#     def __init__(self, full_name, avg_rank, courses):
#         self.full_name = full_name
#         self.avg_rank = avg_rank
#         self.courses = courses

# class StudentEncoder(JSONEncoder):
#     """Кастомный JSONEncoder для класса Student."""
#     def default(self, obj):
#         if isinstance(obj, Student):  # Если объект — Student
#             return obj.__dict__  # Преобразуем в словарь
#         return super().default(obj)  # Для остальных объектов стандартный метод

# Создаём объект Student
# student = Student("Alice Johnson", 4.5, ["Math", "Physics"])

# Сериализуем его с кастомным энкодером
# json_data = json.dumps(student, cls=StudentEncoder, indent=4)
# print(json_data)
# ```
# ✔ **Вывод JSON:**
# ```json
# {
#     "full_name": "Alice Johnson",
#     "avg_rank": 4.5,
#     "courses": ["Math", "Physics"]
# }
# ```
# 🔹 **Объект `Student` корректно превращается в словарь** благодаря `obj.__dict__`.  

### **❌ Случай 2: Передаём несериализуемый объект (используется `super().default(obj)`)**
# Допустим, мы передаём **несериализуемый объект** (например, `set()`):  
# data = {"name": "Alice", "skills": {"Python", "Django"}}

# Пытаемся сериализовать словарь с множеством
# json_data = json.dumps(data, cls=StudentEncoder, indent=4)
# print(json_data)
# ```
# ❌ **Ошибка:**  
# ```
# TypeError: Object of type set is not JSON serializable
# ```
# 📌 `super().default(obj)` **не знает, как сериализовать `set`**, поэтому выдаёт ошибку.  

### **✅ Исправленный вариант (обрабатываем `set`)**
# class CustomEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Student):
#             return obj.__dict__  # Преобразуем Student в словарь
#         if isinstance(obj, set):
#             return list(obj)  # Преобразуем set в список
#         return super().default(obj)  # Всё остальное обрабатываем стандартно

# data = {"name": "Alice", "skills": {"Python", "Django"}}

# json_data = json.dumps(data, cls=CustomEncoder, indent=4)
# print(json_data)
# ```
# ✔ **Вывод JSON (корректно обработан `set`)**:
# ```json
# {
#     "name": "Alice",
#     "skills": ["Django", "Python"]
# }
# 🔹 Теперь `set()` **автоматически превращается в список!**  

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

# Ты можешь создавать **собственные классы JSONEncoder**, чтобы **сериализовать нестандартные объекты**, такие как экземпляры классов.  
### 🔹 **Что делает этот код?**  
# - `StudentEncoder` наследует `JSONEncoder`, который используется в `json.dump()`.  
# - Переопределён метод `default(self, obj)`, который определяет **как сериализовать объекты**.  
# - Если `obj` — это объект `Student`, он **преобразуется в словарь** (`obj.__dict__`).  
# - Если `obj` — не `Student`, вызывается стандартный `super().default(obj)` (чтобы избежать ошибки).  

### 🔹 **Как это работает в практике?**  
#### ✅ **Пример использования `StudentEncoder`**
# import json
# from json import JSONEncoder

# class Student:
#     def __init__(self, full_name, avg_rank, courses):
#         self.full_name = full_name
#         self.avg_rank = avg_rank
#         self.courses = courses

# class StudentEncoder(JSONEncoder):
#     """Кастомный JSONEncoder для сериализации объектов Student."""
#     def default(self, obj):
#         if isinstance(obj, Student):
#             return obj.__dict__  # Преобразуем объект в словарь
#         return super().default(obj)  # Для остальных объектов стандартная сериализация

# Создание объекта Student
# student = Student("Alice Johnson", 4.5, ["Math", "Physics"])

# Сериализация с кастомным JSONEncoder
# json_data = json.dumps(student, cls=StudentEncoder, indent=4, ensure_ascii=False)
# print(json_data)

# 🔹 **Вывод JSON:**
# json
# {
#     "full_name": "Alice Johnson",
#     "avg_rank": 4.5,
#     "courses": ["Math", "Physics"]
# }

### 🔹 **Где это полезно?**
# ✅ **Когда стандартный `json.dumps()` не может обработать объект**  
# ✅ **Когда нужно кастомное поведение сериализации (например, исключить атрибуты)**  
# ✅ **Когда сериализуем сложные объекты, например, вложенные классы**  

### ✅ **Более сложный пример: вложенные объекты**  
# Если объект **содержит другой объект**, нам нужно обрабатывать оба:  

# class Group:
#     def __init__(self, title, students):
#         self.title = title
#         self.students = students

# class GroupEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Group):
#             return {
#                 "title": obj.title,
#                 "students": [StudentEncoder().default(student) for student in obj.students]  # Сериализуем студентов
#             }
#         return super().default(obj)

# Создаём группу
# group = Group("Physics Group", [Student("Alice", 4.5, ["Math"]), Student("Bob", 3.8, ["Physics"])])

# Сериализуем
# json_data = json.dumps(group, cls=GroupEncoder, indent=4, ensure_ascii=False)
# print(json_data)

# ✔ Теперь `GroupEncoder` сериализует и `Group`, и `Student` правильно.

### 💡 **Вывод:**  
# 🚀 **Ты можешь создавать собственные `JSONEncoder`, чтобы управлять сериализацией!**  
# 📌 Используй `default()`, чтобы **обрабатывать кастомные классы**.  
# 📌 Это позволяет **сохранять объекты в JSON без ручного преобразования**.  

# Ниже приведён исправлённый вариант кода, который удовлетворяет требованиям тестов, а также подробное объяснение причин ошибок и внесённых исправлений.

# import json
# import os
# from json import JSONEncoder

# class Student:
#     """Student class with information about the student."""
#     def __init__(self, full_name: str, avg_rank: float, courses: list):
#         self.full_name = full_name
#         self.avg_rank = avg_rank
#         self.courses = courses

#     def serialize_to_json(self, filename: str):
#         """
#         Сохраняет объект Student в JSON-файл.
#         **Важно:** для прохождения теста JSON должен быть записан в компактном виде, без отступов.
#         """
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(self, f, cls=StudentEncoder, ensure_ascii=False)

#     @classmethod
#     def from_json(cls, json_file: str):
#         """
#         Создаёт экземпляр Student из JSON-файла.
#         Файл должен содержать JSON-объект (словарь), а не список.
#         """
#         if not os.path.exists(json_file):
#             raise FileNotFoundError(f"File {json_file} not found!")
#         with open(json_file, "r", encoding="utf-8") as f:
#             data = json.load(f)
#         # Если загруженные данные оказались списком, берём первый (на всякий случай).
#         if isinstance(data, list):
#             if not data:
#                 raise ValueError("Empty student list in file")
#             data = data[0]
#         return cls(**data)

#     def __str__(self):
#         # Тесты ожидают вывод вида:
#         # "Student2 from group2 (50.4): ['C++']"
#         return f"{self.full_name} ({self.avg_rank}): {self.courses}"

#     def __repr__(self):
#         return self.__str__()


# class Group:
#     """Класс Group для группы студентов."""
#     def __init__(self, title: str, students: list):
#         self.title = title
#         self.students = students

#     @classmethod
#     def create_group_from_file(cls, students_file: str):
#         """
#         Создаёт экземпляр Group из JSON-файла содержащего информацию о студентах.
#         Название группы берётся из имени файла (без расширения).
        
#         Примечание:
#          - Если файл содержит единственного студента (словарь), то оборачиваем его в список,
#            чтобы работать с данными единообразно.
#         """
#         if not os.path.exists(students_file):
#             raise FileNotFoundError(f"File {students_file} not found")
#         with open(students_file, "r", encoding="utf-8") as f:
#             data = json.load(f)
#         # Если данные – это словарь (один студент), оборачиваем в список.
#         if isinstance(data, dict):
#             data = [data]
#         elif not isinstance(data, list):
#             raise ValueError(f"Expected list or dict in {students_file}, got {type(data).__name__}")
#         students = []
#         for student_data in data:
#             if not isinstance(student_data, dict):
#                 raise TypeError("Each student record must be a dictionary")
#             students.append(Student(**student_data))
#         # Название группы – имя файла без расширения.
#         title = os.path.splitext(os.path.basename(students_file))[0]
#         return cls(title, students)

#     @staticmethod
#     def serialize_to_json(list_of_groups, filename: str):
#         """
#         Сохраняет список групп в JSON-файл.
#         **Важно:** JSON должен быть записан в компактном виде (без отступов), чтобы соответствовать тестам.
#         """
#         groups_data = [
#             {"title": group.title, "students": [student.__dict__ for student in group.students]}
#             for group in list_of_groups
#         ]
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(groups_data, f, ensure_ascii=False)

#     def __str__(self):
#         """
#         Формирует строку в виде:
#         2020_2: ["Student 1 from second Group (98): ['Python']", "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]
#         """
#         # Для каждого студента вызываем __str__ (который уже форматирован по требованиям)
#         students_str = [str(student) for student in self.students]
#         return f"{self.title}: {students_str}"

#     def __repr__(self):
#         return self.__str__()


# class StudentEncoder(JSONEncoder):
#     """Кастомный JSONEncoder для сериализации объектов Student."""
#     def default(self, obj):
#         if isinstance(obj, Student):
#             return obj.__dict__
#         return super().default(obj)

# ## Объяснение исправлений
# ### 1. **Формат JSON в методе `serialize_to_json`**
# **Проблема:**  
# Тесты для метода `Student.serialize_to_json` (и аналогично для `Group.serialize_to_json`) ожидают, что JSON будет записан в компактном виде:  
# {"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}
# а не в многострочном формате с отступами (pretty print), как выдаёт параметр `indent=4`.

# **Решение:**  
# Мы удалили параметр `indent=4` в обоих методах, чтобы при записи использовался компактный (однострочный) формат JSON.

# ### 2. **Вывод строкового представления объектов**
# **Проблема:**  
# – При вызове `print(user1)`, тест ожидает строку вида:  
# `Student2 from group2 (50.4): ['C++']`  
# а если используется только `__repr__`, то вывод мог выглядеть как:  
# `Student(Student2 from group2, 50.4, ['C++'])`

# **Решение:**  
# Мы добавили метод `__str__` в классе `Student`, который возвращает строку в требуемом формате. Аналогично, для класса `Group` реализован метод `__str__`, чтобы при вызове `print(g1)` выводилось:
# 2020_2: ["Student 1 from second Group (98): ['Python']", "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]

# В методе `__repr__` просто вызывается `__str__`, чтобы вывод был единообразным.

# ### 3. **Обработка формата входного файла для группы**
# **Проблема:**  
# Ошибка  
# TypeError: __main__.Student() argument after ** must be a mapping, not str
# возникала при попытке создать группу из файла `"2020-01.json"`, если файл содержал не список студентов, а единственного студента в виде словаря. В этом случае при итерации по словарю вы получались его ключи (строки), а не полноценный словарь с данными.

# **Решение:**  
# В методе `Group.create_group_from_file` добавлена проверка: если данные, загруженные из JSON, являются словарём, они оборачиваются в список:
# ```python
# if isinstance(data, dict):
#     data = [data]
# Это гарантирует, что далее цикл `for student_data in data:` будет итерироваться по списку словарей.

# ## Примеры использования и ожидаемые результаты

# 1. **Для Student.from_json и __str__**
# Файл `"2020-01.json"` (пример содержимого):
# ```json
# {
#     "full_name": "Student2 from group2",
#     "avg_rank": 50.4,
#     "courses": ["C++"]
# }

# Вызов:
# ```python
# user1 = Student.from_json("2020-01.json")
# print(user1)

# Вывод:

# Student2 from group2 (50.4): ['C++']


# 2. **Для Student.serialize_to_json**
# Вызов:
# ```python
# user1 = Student.from_json("2020-01.json")
# Student.serialize_to_json(user1, "test_student.json")
# ```
# Содержимое файла `"test_student.json"` будет:
# ```
# {"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}
# ```
# (Записаны в компактном JSON‑формате, без лишних отступов)

# 3. **Для создания группы из файла**

# Файл `"2020_2.json"` (пример содержимого):
# ```json
# [
#     {"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]},
#     {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": ["Ruby", "Python", "Frontend development"]}
# ]
# ```
# Вызов:
# ```python
# g1 = Group.create_group_from_file("2020_2.json")
# print(g1)
# ```
# Вывод:
# ```
# 2020_2: ["Student 1 from second Group (98): ['Python']", "Student 2 from second Group (70.34): ['Ruby', 'Python', 'Frontend development']"]
# ```

# 4. **Для Group.serialize_to_json**

# Вызов:
# ```python
# g1 = Group.create_group_from_file("2020_2.json")
# g2 = Group.create_group_from_file("2020-01.json")
# Group.serialize_to_json([g1, g2],"g1.json")
# ```
# Содержимое файла `"g1.json"` будет:
# ```json
# [{"title": "2020_2", "students": [{"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]}, {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": ["Ruby", "Python", "Frontend development"]}]}, {"title": "2020-01", "students": [{"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}]}]
# ```
# (Компактный JSON без отступов)

# ---

# ## Вывод

# - **Параметр `indent=4`** был убран из методов сериализации, чтобы JSON записывался в компактном виде (такой формат требуется тестами).
# - Добавлены методы `__str__` в классах **Student** и **Group**, чтобы при выводе через `print()` отображался именно тот формат строк, который ожидается в тестах.
# - В методе `Group.create_group_from_file` добавлена обработка случая, когда в файле содержится не список студентов, а один студент (словарь).