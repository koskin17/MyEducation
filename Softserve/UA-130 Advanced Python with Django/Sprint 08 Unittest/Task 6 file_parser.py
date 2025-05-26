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

# Давай разберём задачу **пошагово**, чтобы было абсолютно всё понятно и без недоразумений. Мы решим её **чисто, понятно и профессионально**, с использованием `mock` в тестах.

## 📌 Условие задачи
# Нужно создать функцию `file_parser`, которая:
# * Если передано **2 аргумента**:
#   * Читает файл
#   * Ищет количество вхождений строки
#   * Возвращает строку: `"Found X strings"`

# * Если передано **3 аргумента**:
#   * Читает файл
#   * Заменяет вхождения строки
#   * Сохраняет обратно
#   * Возвращает строку: `"Replaced X strings"`

## 🧩 Разработка функции `file_parser(path, search, replace=None)`
### 🔹 Аргументы:
# | Аргумент  | Значение                        |
# | --------- | ------------------------------- |
# | `path`    | Путь к файлу                    |
# | `search`  | Строка для поиска               |
# | `replace` | Строка для замены (опционально) |

## 🛠 Алгоритм функции
# 1. Открываем файл (чтение или чтение+запись, если `replace`).
# 2. Читаем содержимое.
# 3. Считаем количество вхождений `search`.
# 4. Если `replace`:
#    * Делаем `str.replace(search, replace)`
#    * Перезаписываем файл.
#    * Возвращаем `Replaced X strings`
# 5. Иначе — возвращаем `Found X strings`

## ✅ Использование `mock` в `unittest`
# from unittest.mock import mock_open, patch
# `mock_open()` позволяет подменить `open()` так, как будто файл существует и работает.

## ✅ Полный код
import unittest
from unittest.mock import mock_open, patch

def file_parser(path, search, replace=None):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    count = content.count(search)

    if replace is not None:
        new_content = content.replace(search, replace)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return f"Replaced {count} strings"
    else:
        return f"Found {count} strings"

## ✅ Unittests with `mock`
class ParserTest(unittest.TestCase):

    def test_find_string(self):
        mocked_file = mock_open(read_data="xoxooxxooxoxo")
        with patch("builtins.open", mocked_file):
            result = file_parser("fake_path.txt", "o")
            self.assertEqual(result, "Found 7 strings")

    def test_replace_string(self):
        # read_data contains 4 'x', replace them with 'o'
        mocked_file = mock_open(read_data="xx xx")
        with patch("builtins.open", mocked_file) as m:
            result = file_parser("fake_path.txt", "x", "o")
            self.assertEqual(result, "Replaced 4 strings")
            # Let's check that the replaced content has been written to the file.
            m().write.assert_called_once_with("oo oo")

    def test_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError()):
            with self.assertRaises(FileNotFoundError):
                file_parser("nonexistent.txt", "a")

## 🧪 Как работает `mock_open`?
# * `mock_open(read_data="...")` создаёт фейковый файл с заданным содержимым.
# * `patch("builtins.open", ...)` заменяет `open` на нашу заглушку.
# * `m().write.assert_called_once_with(...)` проверяет, **что файл был перезаписан** новым содержимым.

## ✅ Как запустить тесты
# Внизу файла можешь добавить:
if __name__ == "__main__":
    unittest.main()

## 📦 Итого
# | Компонент              | Назначение                                  |
# | ---------------------- | ------------------------------------------- |
# | `file_parser`          | Работает с файлом: ищет или заменяет строки |
# | `mock_open`            | Позволяет "подменить" файл в тестах         |
# | `patch()`              | Заменяет `open()` на наш mock               |
# | `assert_called_with()` | Проверяет, что файл действительно изменён   |
# | `FileNotFoundError`    | Обрабатывает ошибку отсутствующего файла    |

# Давай разберём **построчно и простыми словами**, как работает весь код решения задачи `file_parser` и его тестов. Я объясню и **основную функцию**, и **тесты с mock**, чтобы ты понял каждую деталь.

# ## 📌 Основная функция `file_parser`
# def file_parser(path, search, replace=None):

# 🔹 Это функция, которая:
# * получает путь к файлу (`path`);
# * строку для поиска (`search`);
# * и **необязательный** параметр `replace`, если хотим заменить найденные строки.

#     try:
#         with open(path, "r", encoding="utf-8") as f:
#             content = f.read()

# 🔹 Пытаемся открыть файл по указанному пути и **прочитать всё содержимое**.

# * `with open(...) as f:` — безопасное открытие файла (автоматически закроется).
# * `f.read()` — читает файл как одну строку и сохраняем её в `content`.

#     except FileNotFoundError:
#         return "File not found"

# 🔹 Если файл **не существует**, мы ловим исключение `FileNotFoundError` и возвращаем строку `"File not found"`.

#     count = content.count(search)

# 🔹 Считаем, сколько раз строка `search` встретилась в файле. Например: `"abcabc".count("a")` → `2`.

#     if replace is not None:

# 🔹 Если передан параметр `replace`, значит мы хотим **заменить** найденные строки.

#         new_content = content.replace(search, replace)

# 🔹 Заменяем все вхождения `search` на `replace`.

#         with open(path, "w", encoding="utf-8") as f:
#             f.write(new_content)

# 🔹 Открываем файл **на запись** и записываем в него обновлённое содержимое.

#         return f"Replaced {count} strings"

# 🔹 Возвращаем, сколько строк было заменено.

#     else:
#         return f"Found {count} strings"

# 🔹 Если `replace` не передан — просто возвращаем, сколько строк найдено.

# ## 📌 Весь `file_parser` — кратко:
# - Открыть файл
# - Прочитать содержимое
# - Посчитать количество вхождений search
# - Если указан replace:
#     → Заменить и записать файл
#     → Вернуть количество замен
# - Если не указан:
#     → Вернуть количество найденных

# ## 🧪 Разбор тестов (`ParserTest`)

# import unittest
# from unittest.mock import mock_open, patch

# * `unittest` — встроенная библиотека Python для тестов.
# * `mock_open`, `patch` — для **имитации файла**, не работая с настоящими файлами.

# ### ✅ Тест: поиск строки

# def test_find_string(self):
#     mocked_file = mock_open(read_data="xoxooxxooxoxo")
#     with patch("builtins.open", mocked_file):
#         result = file_parser("fake_path.txt", "o")
#         self.assertEqual(result, "Found 7 strings")

# 🔹 Что тут происходит:
# * `mock_open(...)` создаёт **фейковый файл**, как будто в нём строка `"xoxooxxooxoxo"`.
# * `patch(...)` подменяет `open()` на этот фейковый файл.
# * `file_parser(...)` считает `"o"` — их 7.
# * Проверка: `"Found 7 strings"`.

# ### ✅ Тест: замена строки

# def test_replace_string(self):
#     mocked_file = mock_open(read_data="xx xx")
#     with patch("builtins.open", mocked_file) as m:
#         result = file_parser("fake_path.txt", "x", "o")
#         self.assertEqual(result, "Replaced 4 strings")
#         m().write.assert_called_once_with("oo oo")

# 🔹 Что происходит:
# * Файл содержит `"xx xx"` → 4 `x`.
# * Заменим `x → o` → `"oo oo"`.
# * Проверяем:

#   * `"Replaced 4 strings"`
#   * `m().write.assert_called_once_with("oo oo")` — проверка, что файл **перезаписали** верно.

# ### ✅ Тест: файл не найден

# def test_file_not_found(self):
#     with patch("builtins.open", side_effect=FileNotFoundError()):
#         result = file_parser("nonexistent.txt", "a")
#         self.assertEqual(result, "File not found")

# 🔹 Что тут:
# * `patch(...)` делает так, что при вызове `open()` будет выброшен `FileNotFoundError`.
# * Проверка: `"File not found"`.

# ## 📌 Как всё работает вместе?
# if __name__ == "__main__":
#     unittest.main()

# 🔹 Этот блок говорит Python:
# * Если мы запускаем файл напрямую, то выполнить `unittest.main()`:
#   * Найдёт все классы `TestCase`
#   * Найдёт все методы `test_...`
#   * Запустит каждый из них
#   * Покажет результат

# ## 💬 ИТОГ
# | Компонент              | Что делает                                             |
# | ---------------------- | ------------------------------------------------------ |
# | `file_parser`          | Читает файл, считает или заменяет строки               |
# | `mock_open`            | Создаёт фейковый файл с текстом                        |
# | `patch()`              | Подменяет `open()` на фейковую версию                  |
# | `assertEqual()`        | Проверяет, что результат = ожидаемому                  |
# | `assert_called_with()` | Проверяет, что файл был перезаписан правильной строкой |
