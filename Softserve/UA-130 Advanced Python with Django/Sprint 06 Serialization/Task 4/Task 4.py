# Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
# This class should contain method serialize for serialize object to filename according to  type. 
# For defining format create enum FileType with values JSON, BYTE.
# Create function serialize(object, filename, filetype).
# This function use SerializeManager and should serialize object to filename according to type.
# For example:
# if user_dict = { 'name': 'Roman', 'id': 8}
# then
# serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
# serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"

# Заготовка кода:
# import json
# import pickle
# from enum import Enum

# // type your code here

# def serialize(object, filename, fileType):
#     with SerializeManager(filename, fileType) as manager:
#         manager.serialize(object)

### **Код решения**
import json
import pickle
from enum import Enum

class FileType(Enum):
    """Перечисление форматов файлов."""
    JSON = "json"
    BYTE = "byte"

    # ### 🔸 `Enum` — це **перелічення (перечисление)**
    # > Уяви, що ти створюєш **обмежений список варіантів**, з якими можна працювати.
    # У цьому випадку:
    # * `FileType` — тип файлу, і він може бути або `"json"`, або `"byte"`.
    # ## 📌 Що таке `class FileType(Enum)`?
    # Це спеціальний клас, який:
    # * не дозволяє створювати нові значення,
    # * дає лише **фіксований список варіантів** (enum = "enumeration" = перелік).
    # ---
    # ## 🟩 Пояснення кожного рядка
    # | Рядок                   | Що означає                                                            |
    # | ----------------------- | --------------------------------------------------------------------- |
    # | `class FileType(Enum):` | Ми створюємо нове перелічення з іменем `FileType`                     |
    # | `JSON = "json"`         | Один із варіантів цього переліку – `JSON`, який має значення `"json"` |
    # | `BYTE = "byte"`         | Інший варіант – `BYTE`, значення `"byte"`                             |
    # ---
    # ## 🔧 Як це працює?
    # ```python
    # print(FileType.JSON)           # FileType.JSON
    # print(FileType.JSON.value)     # "json"
    # print(FileType.BYTE.name)      # "BYTE"
    # ```
    # * `.value` → фактичне значення (те, що ми присвоїли — "json" чи "byte")
    # * `.name` → ім’я елемента переліку ("JSON" чи "BYTE")
    # ---
    # ## ✅ Навіщо так робити?
    # | Без `Enum`               | З `Enum`                            |
    # | ------------------------ | ----------------------------------- |
    # | `file_type = "json"`     | `file_type = FileType.JSON`         |
    # | Легко помилитися в назві | Безпечне автодоповнення + перевірка |
    # | Немає обмежень           | Тільки дозволені значення           |
    # | Код менш зрозумілий      | Код сам каже, які є варіанти        |
    # ---
    # ## 🧁 Простий приклад з реального життя
    # ```python
    # class TrafficLight(Enum):
    #     RED = "Stop"
    #     YELLOW = "Wait"
    #     GREEN = "Go"
    # ```
    # ```python
    # light = TrafficLight.RED
    # print(light.value)  # "Stop"
    # ```
    # ---
    # ## ✨ Підсумок:
    # > `Enum` — це **зручний і безпечний спосіб обмежити набір допустимих значень**, надати їм імена й уникнути помилок у коді.
    # У твоєму прикладі:
    # * `FileType` — перелік допустимих форматів файлів
    # * `"json"` і `"byte"` — єдині допустимі типи
    # * Це допомагає уникнути помилок типу `file_type = "jsn"` чи `"btie"`

class SerializeManager:
    """Context manager for serializing objects."""
    def __init__(self, filename: str, filetype: FileType):
        self.filename = filename
        self.filetype = filetype

    # For a class to work with "with" methods, it must have "enter" and "exit" methods defined in it.
    def __enter__(self):
        """Entering the context."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Out of context."""
        pass  # В данной задаче нет необходимости в специальных действиях при выходе

    def serialize(self, obj):
        """Method for serializing an object to a file according to the specified format."""
        if self.filetype == FileType.JSON:
            self._serialize_json(obj)
        elif self.filetype == FileType.BYTE:
            self._serialize_byte(obj)
        else:
            raise ValueError(f"Unsupported file type: {self.filetype}")

    def _serialize_json(self, obj):
        """Serialize an object to a JSON file."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False)

    def _serialize_byte(self, obj):
        """Serialize an object to a binary file."""
        with open(self.filename, "wb") as f:
            pickle.dump(obj, f)

def serialize(obj, filename, filetype):
    """A function that uses `SerializeManager` to serialize an object."""
    with SerializeManager(filename, filetype) as manager:
        manager.serialize(obj)

# === 🔹 Примеры использования ===
user_dict = { 'name': 'Roman', 'id': 8 }

# Сериализация в байтовый формат
serialize(user_dict, "2", FileType.BYTE)

# Сериализация строки в JSON
serialize("String", "string.json", FileType.JSON)

### **📌 Что реализовано?**
# ✅ **Класс `FileType`** (Enum) для определения допустимых форматов файлов: `JSON` и `BYTE`.  
# ✅ **Класс `SerializeManager`**:
#    - Атрибуты `filename` и `filetype` для хранения имени файла и типа сериализации.
#    - Контекстный менеджер (`__enter__`, `__exit__`) для удобного использования `with ...`.
#    - Метод `serialize(obj)`, который выбирает нужный формат сериализации.
#    - Отдельные методы `_serialize_json()` и `_serialize_byte()` для обработки разных форматов.
# ✅ **Функция `serialize(obj, filename, filetype)`**:
#    - Создаёт экземпляр `SerializeManager` и вызывает `serialize(obj)`, сокращая код.

### **🚀 Как это работает?**
# 📌 Если передаётся объект `user_dict = { 'name': 'Roman', 'id': 8 }`, вызов:
# ```python
# serialize(user_dict, "2", FileType.BYTE)
# ```
# ✔ Создаст файл `"2"`, содержащий объект в бинарном формате (можно прочитать с `pickle.load(f)`).

# 📌 Если передаётся `"String"`, вызов:
# ```python
# serialize("String", "string.json", FileType.JSON)
# ```
# ✔ Создаст файл `"string.json"`, содержащий `"String"` в текстовом JSON.

### **💡 Вывод**
# 🚀 Код корректно реализует сериализацию с использованием **контекстного менеджера** и **перечислений Enum**.  
# Теперь можно легко сохранять объекты в **JSON** или **байтовый формат**, используя единую функцию `serialize()`.  