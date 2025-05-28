# 1. Create users and subjects data from files
# get_subjects_from_json(subjects_json) -> List[Subject]
# get_users_with_grades(users_json, subjects_json, grades_json) -> List[User]

# 2. Simulate working with the application
# method User.create_user(username, password, role) creates user
# method user.add_score_for_subject(subject:Subject, score: Score) adds score for subject
# function add_user(user, users) adds user to users (in case of uniqueness username)
# function add_subject(subject, subjects) adds subject to subjects (in case of uniqueness title)
# function get_grades_for_user(username:str, user:User, users:list) returns all grades for the user with username (only own grades or for mentor)

# 3. Rewrite the old json-files with new ones
# users_to_json(users, json_file)
# subjects_to_json(subjects, json_file)
# grades_to_json(users, subjects, json_file)

## 🧩 Завдання коротко:
# 1. Прочитати з `JSON` файлів користувачів, предмети, оцінки.
# 2. Мати логіку створення користувача, додавання предмету, призначення оцінки.
# 3. Можливість отримати оцінки учня.
# 4. Перезаписати JSON-файли новими даними.

## ✅ Структура коду

### 🔸 Enum для ролей
# class Role(Enum):
#     TRAINEE = 0
#     MENTOR = 1

# Щоб уникнути магічних чисел. `Role.TRAINEE` краще, ніж просто `0`.

### 🔸 Модель предмету, оцінки та користувача:
# @dataclass
# class Subject:
#     title: str
#     id: str = field(default_factory=lambda: uuid4().hex)

# @dataclass
# class Score:
#     value: str

# * `Score` — просто обгортка над оцінкою (`A`, `B`, `C`, ...).
# * `Subject` має `title` та `id`.

# @dataclass
# class User:
#     username: str
#     password: str
#     role: Role
#     id: str = field(default_factory=lambda: uuid4().hex)
#     grades: dict = field(default_factory=dict)  # subject_id → Score

# У користувача є метод:
# def add_score_for_subject(self, subject: Subject, score: Score):
#     self.grades[subject.id] = score

### 🔸 Створення користувача:
# @classmethod
# def create_user(cls, username, password, role):
#     return cls(username=username, password=password, role=Role(role))

# `classmethod` зручний для ініціалізації з перетворенням типів (наприклад, role → Enum).

### 🔸 Завантаження з JSON
# def get_subjects_from_json(json_file: str) -> List[Subject]:
#     ...
# def get_users_with_grades(users_json, subjects_json, grades_json) -> List[User]:
#     ...
# 1. Створюємо `map` з `subjects` і `users` за `id`.
# 2. Для кожного запису в `grades.json` знаходимо відповідного користувача і додаємо йому оцінку.

### 🔸 Додавання у список (унікальність):
# def add_user(new_user: User, users: List[User]):
#     if any(u.username == new_user.username for u in users):
#         raise ValueError("Username already exists")
#     users.append(new_user)

# Аналогічно для предметів.

### 🔸 Отримання оцінок користувача:
# def get_grades_for_user(username: str, current_user: User, users: List[User]) -> dict:
#     if current_user.role == Role.MENTOR:
#         ...
#     else:
#         if current_user.username != username:
#             raise PermissionError("Access denied")

# * Учень може бачити тільки свої оцінки.
# * Ментор — будь-якого користувача.

### 🔸 Запис у JSON
# def users_to_json(users: List[User], json_file: str): ...
# def subjects_to_json(subjects: List[Subject], json_file: str): ...
# def grades_to_json(users: List[User], subjects: List[Subject], json_file: str): ...

## ❗ Важливо
# * `users.json` не містить оцінок, тому їх беруть з `grades.json`.
# * `grades.json` зберігає зв’язок `user_id` → `subject_id` → `score`.

## 🧪 Як протестувати?
# 1. Створи 3 JSON-файли (`users.json`, `subjects.json`, `grades.json`) як у прикладі.
# 2. Виклич:
# subjects = get_subjects_from_json("subjects.json")
# users = get_users_with_grades("users.json", "subjects.json", "grades.json")

# 3. Додай нову оцінку:
# u = users[0]
# s = subjects[0]
# u.add_score_for_subject(s, Score("A"))

# 4. Збережи назад:
# users_to_json(users, "new_users.json")
# grades_to_json(users, subjects, "new_grades.json")

# Ось повний код рішення задачі, яку ти описав. Він включає:
# * Класи `User`, `Subject`, `Score` з використанням `@dataclass`.
# * Перерахування `Role` для ролей користувачів.
# * Функції для завантаження та збереження даних з/у JSON.
# * Методи для створення користувачів, додавання оцінок та отримання оцінок.
# * Функції для додавання користувачів та предметів з перевіркою унікальності.
# * Функції для отримання оцінок користувача з урахуванням ролі.

# ## 🔷 Головна мета коду
# Ми працюємо зі шкільною системою:
# * Є **користувачі (Users)** — наприклад, учень або ментор.
# * Є **предмети (Subjects)**.
# * Є **оцінки (Grades)** — які пов'язують учня з певним предметом.
# * Всі ці дані зберігаються у **JSON-файлах**, які треба:
#   * зчитувати;
#   * обробляти в Python;
#   * знову зберігати у файл.

# ## ❓Чому 3 класи з `@dataclass`, а `Role` — ні?

# * `Role` — це Enum. Він не повинен бути data-класом, бо призначений лише для фіксованих значень.
# * Інші (`User`, `Subject`, `Score`) — просто **сховища даних**, тому `@dataclass` допомагає зменшити код.

# ---

import json
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
import os

class Role(Enum):
    TRAINEE = 0
    MENTOR = 1
    # 🔸 Це **перерахування (Enum)** — особливий клас для фіксованого списку значень:
    # * `TRAINEE = 0` — учень.
    # * `MENTOR = 1` — ментор.
    # ➡️ Ми використовуємо Enum, щоб уникати випадкових помилок. Замість того щоб писати `"mentor"` чи `"trainee"`, ми точно знаємо, що можна тільки `Role.TRAINEE` або `Role.MENTOR`.

@dataclass
class Subject:
    title: str
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    # 🔸 Це **предмет**. Має:
    # * `title`: назву предмета (наприклад, "Math").
    # * `id`: унікальний ідентифікатор (генерується автоматично через `uuid`).

    # > ✅ Ми використовуємо **@dataclass**, тому що це простий клас для зберігання даних. Він автоматично створює:
    # * `__init__`
    # * `__repr__`
    # * `__eq__`
    #   та інші методи без потреби писати їх вручну.

@dataclass
class Score:
    subject_id: str
    score: str  # Example, 'A', 'B', 'C'
    # 🔸 Це **оцінка**, яка пов’язує учня з конкретним предметом:
    # * `subject_id` — id предмета.
    # * `score` — оцінка, наприклад, `'A'`, `'B'`.

@dataclass
class User:
    username: str
    password: str
    role: Role
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    scores: List[Score] = field(default_factory=list)
    # 🔸 Це **користувач**:
    # * `username`, `password`, `role`
    # * `id` — унікальний ідентифікатор
    # * `scores` — список об'єктів `Score`, які зберігають оцінки

    @staticmethod
    def create_user(username: str, password: str, role: Role) -> 'User':
        return User(username=username, password=password, role=role)
    # ✅ Це **статичний метод** — створює нового користувача. Ми винесли створення сюди, щоб логіка була зібрана в класі `User`.

    def add_score_for_subject(self, subject: Subject, score: Score):
        self.scores.append(score)
    # ✅ Додає оцінку до списку оцінок користувача.

def get_subjects_from_json(subjects_json_path: str) -> List[Subject]:
    # ## ✅ **Що значить `get_subjects_from_json(path: str) -> List[Subject]:`?**
    # | Частина            | Що це значить                                  |
    # | ------------------ | ---------------------------------------------- |
    # | `path: str`        | параметр `path` повинен бути типу `str`        |
    # | `-> List[Subject]` | функція повертає **список об’єктів `Subject`** |
    # Це теж **аннотації типів** (type hints).
    # Не впливає на виконання, але покращує читабельність, перевірку, автодоповнення.
    with open(subjects_json_path, 'r', encoding='utf-8') as f:
        subjects_data = json.load(f)
    return [Subject(**subject) for subject in subjects_data]
    # 📌 Зчитує список предметів з JSON і створює список об’єктів `Subject`.
    # 🟢 JSON-файли краще читати й писати через `with open(...)` — це безпечніше.

def get_users_with_grades(users_json_path: str, subjects_json_path: str, grades_json_path: str) -> List[User]:
    # def get_users_with_grades(users_json_path, subjects_json_path, grades_json_path):
    # 📌 Зчитує:
    # * список користувачів з `users.json`
    # * список оцінок з `grades.json`
    #   Потім:
    # * створює об'єкти `User`
    # * додає до кожного його оцінки

    with open(users_json_path, 'r', encoding='utf-8') as f:
        users_data = json.load(f)
    #with open(users_json_path, 'r', encoding='utf-8') as f:
    #   users_data = json.load(f)
    # * Відкриваємо JSON-файл із користувачами.
    # * `json.load(f)` читає вміст файлу і перетворює його в **Python-об’єкти** (зазвичай список словників).
    # 🟢 JSON-файли краще читати й писати через `with open(...)` — це безпечніше.

    with open(grades_json_path, 'r', encoding='utf-8') as f:
        grades_data = json.load(f)
    # with open(grades_json_path, 'r', encoding='utf-8') as f:
    #     grades_data = json.load(f)
    # - Аналогічно читаємо JSON-файл з оцінками.
    # 🟢 JSON-файли краще читати й писати через `with open(...)` — це безпечніше.

    # > 🧠 Тепер у тебе два списки:
    # > - `users_data`: список словників із даними про користувачів;
    # > - `grades_data`: список словників з оцінками (де є `user_id`, `subject_id`, `score`).

    users = []
    #     users = []
    # * Створюємо **порожній список**, куди будемо додавати об'єкти `User`.

    for user_data in users_data:
        role = Role(user_data['role'])
        user = User(
            username=user_data['username'],
            password=user_data['password'],
            role=role,
            id=user_data['id']
        )
        user_grades = [grade for grade in grades_data if grade['user_id'] == user.id]
        for grade in user_grades:
            score = Score(subject_id=grade['subject_id'], score=grade['score'])
            user.scores.append(score)
        users.append(user)
    return users

def get_users_with_grades(users_json_path: str, subjects_json_path: str, grades_json_path: str) -> List[User]:
    # - Вона приймає **три шляхи до файлів JSON**:
    #   - `users_json_path` — де зберігаються користувачі;
    #   - `subjects_json_path` — (не використовується у тілі функції 😅 — можливо, для майбутнього);
    #   - `grades_json_path` — де зберігаються оцінки;
    # - `-> List[User]` означає: функція **повертає список об'єктів класу `User`**.

    with open(users_json_path, 'r', encoding='utf-8') as f:
        users_data = json.load(f)
    # * Відкриваємо JSON-файл із користувачами.
    # * `json.load(f)` читає вміст файлу і перетворює його в **Python-об’єкти** (зазвичай список словників).
    # ## ✅ **Як працює `json.load(f)`?**
    # Це функція з модуля `json`.
    # 🔹 Вона **зчитує ВЕСЬ вміст JSON-файлу** одразу й повертає **об’єкт Python**:
    # * список → list
    # * словник → dict
    # * рядки → str
    # ➡️ Тобто `json.load()` працює не построчно, а **весь файл за раз**.
    # 🟢 JSON-файли краще читати й писати через `with open(...)` — це безпечніше.

    with open(grades_json_path, 'r', encoding='utf-8') as f:
        grades_data = json.load(f)
    # - Аналогічно читаємо JSON-файл з оцінками.
    # 🟢 JSON-файли краще читати й писати через `with open(...)` — це безпечніше.

    users = []
    for user_data in users_data:
        # - Ітеруємося по кожному словнику (по одному користувачу).

        role = Role(user_data['role'])
        # * Отримуємо роль користувача (наприклад: `"admin"` або `"student"`).
        # * І створюємо об'єкт класу `Role`.

        user = User(
            username=user_data['username'],
            password=user_data['password'],
            role=role,
            id=user_data['id']
        )
        # - Створюємо **об’єкт класу `User`**, передаючи:
        #   - ім’я користувача (`username`);
        #   - пароль (`password`);
        #   - роль (об’єкт `Role`);
        #   - id (рядок або число).

        user_grades = [grade for grade in grades_data if grade['user_id'] == user.id]
        # * Знаходимо **всі оцінки цього користувача**, фільтруючи список `grades_data`.
        # * Відбираємо тільки ті, де `grade['user_id'] == user.id`.

        for grade in user_grades:
            # - Ітеруємося по оцінках **одного користувача**.
            score = Score(subject_id=grade['subject_id'], score=grade['score'])
            # * Створюємо **об’єкт `Score`** — це, очевидно, клас, який представляє оцінку з певного предмету:
            #   * `subject_id` — id предмета;
            #   * `score` — сама оцінка.
            user.scores.append(score)
            # - Додаємо оцінку до списку `scores` цього користувача.
            # Перед цим у класі `User` має бути щось типу `self.scores = []`.
        users.append(user)
        # * Додаємо повністю сформованого користувача (разом із оцінками) у список `users`.
    return users
    # - Повертаємо готовий список об'єктів `User` із їх оцінками.

# ## 🧠 Схема в голові:
# users.json ➜ \[{'id': 1, 'username': 'Ivan', ...}]
# grades.json ➜ \[{'user\_id': 1, 'subject\_id': 5, 'score': 90}, ...]

# 🔁 Для кожного користувача:
# * створюємо User(...)
# * шукаємо його оцінки
# * створюємо Score(...) для кожної оцінки
# * додаємо Score у user.scores
# * додаємо user до списку

def add_user(user: User, users: List[User]) -> bool:
    # ## ✅ **6. Що значить `-> bool`?**
    # 📌 Це значить, що функція **повертає булеве значення** — `True` або `False`.
    # 📌 Додає користувача в список, якщо ще немає користувача з таким іменем. Повертає `True` або `False`.
    if any(u.username == user.username for u in users):
        return False
    users.append(user)
    return True

def add_subject(subject: Subject, subjects: List[Subject]) -> bool:
    # Аналогічна до `add_user`, тільки для предметів.
    if any(s.title == subject.title for s in subjects):
        return False
    subjects.append(subject)
    return True

def get_grades_for_user(username: str, current_user: User, users: List[User]) -> Optional[List[Score]]:
    # ## ✅ **7. Пояснення до `Optional[List[Score]]`**
    # | Елемент                    | Що це означає                                  |
    # | -------------------------- | ---------------------------------------------- |
    # | `username: str`            | параметр `username` — рядок                    |
    # | `current_user: User`       | об’єкт класу `User`                            |
    # | `users: List[User]`        | список об’єктів `User`                         |
    # | `-> Optional[List[Score]]` | функція повертає або список оцінок, або `None` |
    # 📦 `Optional[X]` — це означає: **може бути `X`, а може бути `None`**.
    # 📌 Повертає оцінки:
    # * або **тільки свої**, якщо користувач — Trainee
    # * або **будь-якого**, якщо користувач — Mentor
    if current_user.role == Role.MENTOR:
        for user in users:
            if user.username == username:
                return user.scores
    elif current_user.username == username:
        return current_user.scores
    return None

def users_to_json(users: List[User], json_file: str):
    # записують назад у JSON:
    # * тільки потрібні поля
    # * без зайвих атрибутів (`scores`, `Role` обробляється вручну як `.value`)

    users_data = []
    for user in users:
        users_data.append({
            'username': user.username,
            'password': user.password,
            'role': user.role.value,
            'id': user.id
        })
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(users_data, f, indent=4)
        # ## ✅ **Як працює `json.dump(...)`**
        # json.dump(users_data, f, indent=4)
        # 🔹 `dump()` — це **запис у файл**.
        # | Параметр     | Пояснення                                           |
        # | ------------ | --------------------------------------------------- |
        # | `users_data` | що саме ми записуємо                                |
        # | `f`          | відкритий файл                                      |
        # | `indent=4`   | форматування: відступи 4 пробіли (щоб було красиво) |
        # ➡️ Усі дані з `users_data` перетворюються в JSON і записуються у файл **одним блоком**, не построчно.
        # 🟢 JSON-файли краще читати й писати через `with open(...)` — це безпечніше.

def subjects_to_json(subjects: List[Subject], json_file: str):
    # записують назад у JSON:
    # * тільки потрібні поля
    # * без зайвих атрибутів (`scores`, `Role` обробляється вручну як `.value`)

    subjects_data = []
    for subject in subjects:
        subjects_data.append({
            'title': subject.title,
            'id': subject.id
        })
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(subjects_data, f, indent=4)
        # ## ✅ **Як працює `json.dump(...)`**
        # json.dump(users_data, f, indent=4)
        # 🔹 `dump()` — це **запис у файл**.
        # | Параметр     | Пояснення                                           |
        # | ------------ | --------------------------------------------------- |
        # | `users_data` | що саме ми записуємо                                |
        # | `f`          | відкритий файл                                      |
        # | `indent=4`   | форматування: відступи 4 пробіли (щоб було красиво) |
        # ➡️ Усі дані з `users_data` перетворюються в JSON і записуються у файл **одним блоком**, не построчно.
        # 🟢 JSON-файли краще читати й писати через `with open(...)` — це безпечніше.

def grades_to_json(users: List[User], subjects: List[Subject], json_file: str):
    # записують назад у JSON:
    # * тільки потрібні поля
    # * без зайвих атрибутів (`scores`, `Role` обробляється вручну як `.value`)

    grades_data = []
    for user in users:
        for score in user.scores:
            grades_data.append({
                'user_id': user.id,
                'subject_id': score.subject_id,
                'score': score.score
            })
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(grades_data, f, indent=4)
        # ## ✅ **Як працює `json.dump(...)`**
        # json.dump(users_data, f, indent=4)
        # 🔹 `dump()` — це **запис у файл**.
        # | Параметр     | Пояснення                                           |
        # | ------------ | --------------------------------------------------- |
        # | `users_data` | що саме ми записуємо                                |
        # | `f`          | відкритий файл                                      |
        # | `indent=4`   | форматування: відступи 4 пробіли (щоб було красиво) |
        # ➡️ Усі дані з `users_data` перетворюються в JSON і записуються у файл **одним блоком**, не построчно.
        # 🟢 JSON-файли краще читати й писати через `with open(...)` — це безпечніше.

# ## ❓ Чому частина функцій не в класі?
# ➡️ Бо вони працюють з **усіма користувачами або всіма предметами**, а не з одним об'єктом.
# Тому краще зробити їх окремими функціями, щоб не навантажувати клас зайвою відповідальністю.

# Example of use
if __name__ == "__main__":
    current_dir = os.getcwd() # Get the current directory of the py-script run
    folder = "Softserve/UA-130 Advanced Python with Django/Sprint 08 Unittest/Bonus task with description" # We indicate where exactly the files are located that the script will work with
    base_path = os.path.join(current_dir, folder) # Connecting the path to files

    # Fixing full paths to paths
    # * 🟢 Використовуй `os.path.join(...)` замість ручного зшивання рядків → це кросплатформенно.
    users_json = os.path.join(base_path, "users.json")
    subjects_json = os.path.join(base_path, "subjects.json")
    grades_json = os.path.join(base_path, "grades.json")

    users = get_users_with_grades(users_json, subjects_json, grades_json)
    subjects = get_subjects_from_json(subjects_json)

    # Example: show the current ratings
    current_user = users[0]
    grades = get_grades_for_user(current_user.username, current_user, users)
    if grades is not None:
        for score in grades:
            print(f"Subject ID: {score.subject_id}, Score: {score.score}")
    else:
        print("No grades available.")

    # Saving data to JSON
    users_to_json(users, f"{base_path}/new_users.json")
    subjects_to_json(subjects, f"{base_path}/new_subjects.json")
    grades_to_json(users, subjects, f"{base_path}/new_grades.json")

# ## 🔚 Підсумок
# | Компонент                 | Навіщо                                                      |
# | ------------------------- | ----------------------------------------------------------- |
# | `@dataclass`              | Короткий, зручний спосіб створити клас для зберігання даних |
# | `Enum Role`               | Безпечне представлення ролей                                |
# | `create_user`             | Зручне створення юзера                                      |
# | `get_users_with_grades()` | Збірка користувачів + їх оцінок з файлів                    |
# | `get_grades_for_user()`   | Доступ до оцінок з перевіркою ролі                          |
# | `add_user`, `add_subject` | Перевірка унікальності                                      |
# | `..._to_json()`           | Збереження змін назад                                       |


# ## ✅ **Що означає `title: str`?**
# Це **аннотація типу**.
# 🔹 Це **не обов'язково**, але дуже корисно. Python сам по собі не вимагає вказувати тип змінної. Але ми **підказуємо інтерпретатору та IDE**, що `title` — це рядок (`str`).
# > Такі підказки:
# * використовуються для **перевірки типів** (типу mypy або IDE)
# * не впливають на виконання програми
# 👀 Приклад:
# name: str = "Olga"   # означає, що name має бути рядком
# age: int = 20        # має бути ціле число

# ## ✅ **Що означає `id: str = field(default_factory=...)`?**
# id: str = field(default_factory=lambda: uuid.uuid4().hex)
# 📌 Пояснення по частинах:
# | Частина                    | Що це таке                                                               |
# | -------------------------- | ------------------------------------------------------------------------ |
# | `id: str`                  | аннотація типу — id повинен бути рядком                                  |
# | `field(...)`               | спеціальна функція з `dataclasses`, яка дозволяє вказати деталі для поля |
# | `default_factory=...`      | генератор значення **за замовчуванням**                                  |
# | `lambda: uuid.uuid4().hex` | **лямбда-функція**, яка генерує унікальний hex-ідентифікатор             |
# 📦 Тобто, якщо ми не передали `id`, то воно **автоматично створиться** через `uuid`.

# ## ✅ **Чому `password: str`, а далі `scores: List[Score] = field(...)`?**
# Бо:
# * `password: str` — це простий тип. Достатньо аннотації.
# * `scores: List[Score] = field(default_factory=list)` — це **змінна з мутабельним значенням (список)**.
# 🧠 Якщо писати просто так:
# scores: List[Score] = []
# то цей список буде **один на всіх об'єктах**, що дуже погано ❗
# ✅ Тому ми пишемо:
# scores: List[Score] = field(default_factory=list)
# Це означає: кожному новому `User` буде створено **новий, свій список оцінок**.

# | Синтаксис        | Що означає                             |
# | ---------------- | -------------------------------------- |
# | `var: str`       | аннотація типу                         |
# | `= field(...)`   | задає поведінку поля у dataclass       |
# | `Optional[X]`    | значення може бути або `X`, або `None` |
# | `-> int`         | тип повернення функції                 |
# | `json.load(f)`   | читає весь JSON-файл у Python об’єкт   |
# | `json.dump(...)` | записує об’єкт у файл у форматі JSON   |


# ## ✅ **Для повторення синтаксису (type hints, field)**
# `name: str` - `name: str = "Bob"` - `name` має бути рядком (`str`)
# `scores: List[int]` - `scores: List[int] = [5, 4, 3]` - список цілих чисел
# `-> int` - `def get_age() -> int:` - функція повертає `int`
# `-> Optional[str]` - `def get_name() -> Optional[str]:` - може повернути `str` або `None`
# `List[Score]` - `scores: List[Score] = [...]` - список об'єктів типу `Score` - кожному об’єкту — свій список, а не загальний
# `field(default_factory=lambda: uuid...)` - `id: str = field(default_factory=lambda: uuid...)`
# `field(default_factory=...)` - `scores: List[Score] = field(default_factory=list)` - автоматично генерує унікальний ID 

# ## ✅ **Що таке `field()` із `dataclasses`?**
# from dataclasses import field
# 📌 `field()` — це **функція з модуля `dataclasses`**, яка дозволяє:
# | Мета                                    | Приклад                                           |
# | --------------------------------------- | ------------------------------------------------- |
# | Встановити значення за замовчуванням    | `field(default=0)`                                |
# | Згенерувати значення автоматично        | `field(default_factory=lambda: uuid.uuid4().hex)` |
# | Уникнути спільного списку між об'єктами | `field(default_factory=list)`                     |

# **Чому не можна просто `scores = []`?**
# Тому що всі об’єкти будуть **розділяти один і той самий список**, а `field()` дає **свій список кожному об’єкту**.

# ## ✅ **3. Схема — спрощена візуалізація**
# Ось як виглядає логіка у коді з класами:
# Клас User:
#     - username: str
#     - password: str
#     - role: Role (Enum)
#     - id: str = uuid
#     - scores: List[Score] = []

# Клас Score:
#     - subject_id: str
#     - score: str

# Клас Subject:
#     - title: str
#     - id: str

# Клас Role (Enum):
#     - TRAINEE = 0
#     - MENTOR = 1

# @dataclass
# class User:
#     username: str
#     password: str
#     role: Role
#     id: str = field(default_factory=lambda: uuid.uuid4().hex)
#     scores: List[Score] = field(default_factory=list)

# ## ✅ **4. Приклади з кодом**
# ### ➤ Простий клас без `dataclass`:
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

# ### ➤ Те саме з `dataclass`:
# from dataclasses import dataclass
# @dataclass
# class Person:
#     name: str
#     age: int

# `dataclass` сам створить `__init__`, `__repr__`, `__eq__` тощо. Менше писати руками ✅

# ## ✅ **5. Optional / Union — пояснення**
# from typing import Optional
# def get_email() -> Optional[str]:
#     return "example@email.com"

# 🔹 `Optional[str]` == `Union[str, None]`
# Тобто функція може повернути рядок або `None`.


# ## ✅ Відповіді на твої запитання:
# `title: str` — це аннотація типу? - Так ✅. Це *type hint*, підказка Python (і IDE), що `title` має бути `str`.
# `id: str = field(default_factory=lambda: uuid.uuid4().hex)` -  `id` — поле типу `str`, яке автоматично отримає значення, створене `lambda`. `field()` використовується з `dataclass` і дозволяє встановлювати **фабрику значення за замовчуванням**.
# `username: str` vs `scores: List[Score] = field(...)` - У першому випадку просто аннотація без дефолтного значення. У другому — задається початкове значення через `field(...)` (наприклад, щоб уникнути спільного списку).
# `json.load(f)` — як працює? - Він одразу читає весь файл, парсить його як JSON і повертає **структуру Python**: список, словник тощо. Не читає "построчно" — одразу весь файл.
# `def get_subjects_from_json(path: str) -> List[Subject]` - `: str` — аннотація типу аргументу. `-> List[Subject]` — тип повертаного значення. 
# `-> bool` - Функція повертає `True` або `False`.
# `Optional[List[Score]]` - **`Optional`** = або `List[Score]`, або `None`. Це підказка, що функція може не повернути значення. `List[Score]` = список елементів типу `Score`.
# `json.dump(data, f, indent=4)` - Пише у файл `f` **весь** об'єкт `data` у вигляді форматованого JSON. `indent=4` — відступ 4 пробіли, для зручності читання.

# ## ✅ Таблиця по синтаксису
# | Синтаксис                     | Опис                                                      |
# | ----------------------------- | --------------------------------------------------------- |
# | `x: str`                      | Підказка: `x` — це рядок                                  |
# | `x: int = 0`                  | `x` — ціле число, значення за замовчуванням — 0           |
# | `x: List[str] = field(...)`   | `x` — список рядків, `field()` створює новий список       |
# | `-> bool`                     | Функція повертає `True` або `False`                       |
# | `Optional[str]`               | Або `str`, або `None`                                     |
# | `field(default_factory=list)` | Для `dataclass`, створює новий список для кожного об’єкта |

# ## ✅ Простий приклад `dataclass` + field
# from dataclasses import dataclass, field
# from typing import List
# import uuid

# @dataclass
# class User:
#     username: str
#     password: str
#     role: int
#     id: str = field(default_factory=lambda: uuid.uuid4().hex)
#     scores: List[int] = field(default_factory=list)
