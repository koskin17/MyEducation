# Create function file_parser. If function is called with 2 arguments it must count the number of occurrences string in a file, in case of 3 arguments it must replace string in a file to new string

# first argument - path to file
# second argument - find string
# third argument - replace string

# Function must returned string with count of occurrences or count of replaced strings

# Example:
# file_parser("file.txt", 'x', 'o')-> Replaced 8 strings
# file_parser("file.txt", 'o') -> Found 8 strings
# Please, create class ParsesTest and write unittest for file_parser function uses mock object

# Заготовка кода:
# import unittest

# def file_parser():
#     pass

# class ParserTest(unittest.TestCase):
#     pass

Отлично! Давай разберём задачу **пошагово**, чтобы было абсолютно всё понятно и без недоразумений. Мы решим её **чисто, понятно и профессионально**, с использованием `mock` в тестах.

---

## 📌 Условие задачи

Нужно создать функцию `file_parser`, которая:

* Если передано **2 аргумента**:

  * Читает файл
  * Ищет количество вхождений строки
  * Возвращает строку: `"Found X strings"`

* Если передано **3 аргумента**:

  * Читает файл
  * Заменяет вхождения строки
  * Сохраняет обратно
  * Возвращает строку: `"Replaced X strings"`

---

## 🧩 Разработка функции `file_parser(path, search, replace=None)`

### 🔹 Аргументы:

| Аргумент  | Значение                        |
| --------- | ------------------------------- |
| `path`    | Путь к файлу                    |
| `search`  | Строка для поиска               |
| `replace` | Строка для замены (опционально) |

---

## 🛠 Алгоритм функции

1. Открываем файл (чтение или чтение+запись, если `replace`).
2. Читаем содержимое.
3. Считаем количество вхождений `search`.
4. Если `replace`:

   * Делаем `str.replace(search, replace)`
   * Перезаписываем файл.
   * Возвращаем `Replaced X strings`
5. Иначе — возвращаем `Found X strings`

---

## ✅ Использование `mock` в `unittest`

Поскольку мы **не хотим работать с настоящими файлами**, мы используем `unittest.mock`:

```python
from unittest.mock import mock_open, patch
```

`mock_open()` позволяет подменить `open()` так, как будто файл существует и работает.

---

## ✅ Полный код

```python
import unittest
from unittest.mock import mock_open, patch

def file_parser(path, search, replace=None):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return "File not found"

    count = content.count(search)

    if replace is not None:
        new_content = content.replace(search, replace)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return f"Replaced {count} strings"
    else:
        return f"Found {count} strings"
```

---

## ✅ ЮНИТ-ТЕСТЫ с `mock`

```python
class ParserTest(unittest.TestCase):

    def test_find_string(self):
        mocked_file = mock_open(read_data="xoxooxxooxoxo")
        with patch("builtins.open", mocked_file):
            result = file_parser("fake_path.txt", "o")
            self.assertEqual(result, "Found 6 strings")

    def test_replace_string(self):
        # read_data содержит 4 'x', заменим их на 'o'
        mocked_file = mock_open(read_data="xx xx")
        with patch("builtins.open", mocked_file) as m:
            result = file_parser("fake_path.txt", "x", "o")
            self.assertEqual(result, "Replaced 4 strings")
            # Проверим, что в файл записано заменённое содержимое
            m().write.assert_called_once_with("oo oo")

    def test_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError()):
            result = file_parser("nonexistent.txt", "a")
            self.assertEqual(result, "File not found")
```

---

## 🧪 Как работает `mock_open`?

* `mock_open(read_data="...")` создаёт фейковый файл с заданным содержимым.
* `patch("builtins.open", ...)` заменяет `open` на нашу заглушку.
* `m().write.assert_called_once_with(...)` проверяет, **что файл был перезаписан** новым содержимым.

---

## ✅ Как запустить тесты

Внизу файла можешь добавить:

```python
if __name__ == "__main__":
    unittest.main()
```

---

## 📦 Итого

| Компонент              | Назначение                                  |
| ---------------------- | ------------------------------------------- |
| `file_parser`          | Работает с файлом: ищет или заменяет строки |
| `mock_open`            | Позволяет "подменить" файл в тестах         |
| `patch()`              | Заменяет `open()` на наш mock               |
| `assert_called_with()` | Проверяет, что файл действительно изменён   |
| `FileNotFoundError`    | Обрабатывает ошибку отсутствующего файла    |

---

Если хочешь, я покажу как работает это **вживую по шагам** или помогу написать расширенные тесты (например, без перезаписи при `count == 0`).
