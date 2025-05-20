import os
import json
import csv
import pytest
from university import user_with_department, DepartmentName, InvalidInstanceError

# ----------- Тестовые данные -----------
users = [
    {"id": 1, "name": "Alice", "department_id": 10},
    {"id": 2, "name": "Bob", "department_id": 20}
]

departments = [
    {"id": 10, "name": "Math"},
    {"id": 20, "name": "CS"}
]

users_invalid_schema = [
    {"id": 1, "username": "Alice", "department_id": 10}  # "name" отсутствует
]

departments_missing = [
    {"id": 10, "name": "Math"}
]

users_unknown_department = [
    {"id": 1, "name": "Alice", "department_id": 99}
]

# ---------- Вспомогательные функции ----------
def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def read_csv(filename):
    with open(filename, encoding="utf-8") as f:
        return list(csv.reader(f))

# ---------- Тесты ----------
def test_valid_data(tmp_path):
    user_file = tmp_path / "users.json"
    dept_file = tmp_path / "departments.json"
    out_file = tmp_path / "out.csv"

    save_json(user_file, users)
    save_json(dept_file, departments)

    user_with_department(out_file, user_file, dept_file)

    lines = read_csv(out_file)
    assert lines == [["name", "department"], ["Alice", "Math"], ["Bob", "CS"]]

def test_missing_department(tmp_path):
    user_file = tmp_path / "users.json"
    dept_file = tmp_path / "departments.json"
    out_file = tmp_path / "out.csv"

    save_json(user_file, users_unknown_department)
    save_json(dept_file, departments)

    with pytest.raises(DepartmentName):
        user_with_department(out_file, user_file, dept_file)

def test_invalid_schema(tmp_path):
    user_file = tmp_path / "users.json"
    dept_file = tmp_path / "departments.json"
    out_file = tmp_path / "out.csv"

    save_json(user_file, users_invalid_schema)
    save_json(dept_file, departments)

    with pytest.raises(InvalidInstanceError):
        user_with_department(out_file, user_file, dept_file)

# Запусти тесты:

# pytest test_university.py

## ✅ Что тестирует:

# | Тест                      | Что проверяет                                 |
# | ------------------------- | --------------------------------------------- |
# | `test_valid_data`         | Валидные JSON → создаётся правильный CSV      |
# | `test_missing_department` | Ошибка, если department\_id не существует     |
# | `test_invalid_schema`     | Ошибка, если структура users.json некорректна |
