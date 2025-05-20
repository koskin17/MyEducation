# Implement a Python function validate_json(data, schema) that validates a JSON object against a structured schema and raises custom exceptions when validation fails.

# ✅ Function Signature
 
# def validate_json(data: dict, schema: dict) -> bool: ...
# 📥 Inputs
# data (dict):
# A dictionary representing the data to be validated.

# schema (dict):
# A dictionary following this structure:

# {
#     "type": "object",
#     "properties": {
#         "name": {"type": "string"},
#         "email": {"type": "string"},
#         ...
#     },
#     "required": ["email"]
# }

# 📤 Output
# Returns True if validation passes.

# Raises a specific custom exception if validation fails.

# ✔️ Validation Rules
# The root schema must be of type "object".

# All fields listed in "required" must be present.

# Each field in "properties" (if present in data) must match the declared "type" (string, integer, boolean, array, object).

# Additional keys in the data are ignored.

## 🎯 Цель задачи
# Написать функцию `validate_json(data, schema)`, которая:

# ✅ Проверяет, соответствует ли `data` — словарь (обычно JSON) — заданной структуре `schema`.

# 📌 При ошибках — выбрасывает **кастомные исключения** (свои собственные классы ошибок).

# 📌 При успехе — возвращает `True`.

## 🔧 Что такое `schema`?
# Пример схемы:
# ```python
{
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["email"]
}
# * `"type": "object"` — это значит, что корневой элемент должен быть словарём.
# * `"properties"` — список ключей, которые могут быть в `data`, и какие типы у них должны быть.
# * `"required"` — какие поля **обязаны** быть в `data`.

## 🧠 Как будет работать функция?
### 1. Проверим, что schema имеет корневой `"type": "object"`
# Если нет — выбросим ошибку `InvalidSchemaType`.
### 2. Проверим, что все поля из `"required"` есть в `data`
# Если чего-то не хватает — выбросим `MissingFieldError`.
### 3. Пройдёмся по `properties` и сравним типы
# Если тип не соответствует — выбросим `InvalidFieldTypeError`.

### 4. Если всё хорошо — `return True`
## 💥 Определим собственные ошибки (кастомные исключения):
class ValidationError(Exception):
    """Базовая ошибка валидации."""
    pass

class InvalidSchemaType(ValidationError):
    """Схема должна быть типа object."""
    pass

class MissingFieldError(ValidationError):
    """Отсутствует обязательное поле."""
    pass

class InvalidFieldTypeError(ValidationError):
    """Поле имеет неверный тип."""
    pass

## 🧪 Как будем проверять типы?
# Мы сделаем простое соответствие:
type_mapping = {
    "string": str,
    "integer": int,
    "boolean": bool,
    "array": list,
    "object": dict
}

## ✅ Полная функция:
def validate_json(data: dict, schema: dict) -> bool:
    # 1. Проверим тип корня схемы
    if schema.get("type") != "object":
        raise InvalidSchemaType("Schema root must be of type 'object'.")

    properties = schema.get("properties", {})
    required = schema.get("required", [])

    # 2. Проверим, что все обязательные поля есть в data
    for field in required:
        if field not in data:
            raise MissingFieldError(f"Required field '{field}' is missing.")

    # 3. Проверим типы всех указанных полей
    type_mapping = {
        "string": str,
        "integer": int,
        "boolean": bool,
        "array": list,
        "object": dict
    }

    for key, value in data.items():
        if key in properties:
            expected_type = properties[key].get("type")
            if expected_type not in type_mapping:
                raise InvalidSchemaType(f"Unknown type '{expected_type}' in schema.")
            if not isinstance(value, type_mapping[expected_type]):
                raise InvalidFieldTypeError(
                    f"Field '{key}' expected to be '{expected_type}', got '{type(value).__name__}'."
                )

    return True

## 🔍 Пример использования:
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["email"]
}

data = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30
}

print(validate_json(data, schema))  # True

## ❌ Пример ошибки:
# data = {
#     "name": "Alice",
#     "age": 30
# }

# validate_json(data, schema)
# 🎯 Выдаст:
# MissingFieldError: Required field 'email' is missing.
## 📌 Вывод:
# * Ты проверяешь JSON как валидатор
# * Пишешь свои исключения — это удобно для дебага и тестирования
# * Код легко расширяется (можно добавить `minLength`, `maxLength`, `pattern`, вложенные объекты)
# Хочешь — могу помочь тебе переписать это с поддержкой вложенных объектов или сделать валидацию списков по схемам 🧠✅
