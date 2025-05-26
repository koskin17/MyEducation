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
