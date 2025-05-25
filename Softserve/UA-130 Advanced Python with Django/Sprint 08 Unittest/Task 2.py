# Есть вот такая задача:
# You have function divide
# def divide(num_1, num_2):
# 	return float(num_1) / num_2
	
# Please, write the code with unit tests for the function "divide":
# minimum 3 tests
# must chek all flows
# all test must be pass
# no failures
# no skip

# К ней есть вот такая загатовка кода:
# import unittest

# class DivideTest(unittest.TestCase):
#     #you code

# Задача - учишься **тестировать функции**. Это навык, который отличает настоящих программистов от тех, кто просто пишет "чтобы работало".

## 📌 ЗАДАЧА
# Есть функция:
# def divide(num_1, num_2):
#     return float(num_1) / num_2

# Нужно:
# 1. ✍️ Написать минимум **3 юнит-теста**
# 2. ✅ Протестировать **все ветки** выполнения:

#    * корректное деление
#    * деление на 0 (ошибка)
#    * деление, где один из аргументов строка-число `"10"`
# 3. 🧪 Убедиться, что **все тесты проходят**: нет ошибок, нет пропущенных тестов.

## ✅ ШАГ ЗА ШАГОМ
### 📌 Шаг 1. Что делает `divide()`?
# Она:
# * превращает `num_1` в `float`
# * делит на `num_2`
# Но: **если `num_2 == 0` → будет ошибка** `ZeroDivisionError`.

### ✏ Шаг 2. Что нужно протестировать?
# | Сценарий          | Пример           | Ожидание            |
# | ----------------- | ---------------- | ------------------- |
# | ✅ Обычное деление | `divide(10, 2)`  | `5.0`               |
# | ⚠ Деление на 0    | `divide(10, 0)`  | `ZeroDivisionError` |
# | ✅ Строковое число | `divide("6", 3)` | `2.0`               |

### ✅ Шаг 3. Пишем тесты
import unittest

def divide(num_1, num_2):
    return float(num_1) / num_2

class DivideTest(unittest.TestCase):

    def test_correct_division(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_string_input(self):
        self.assertEqual(divide("6", 3), 2.0)

# Автозапуск тестов
if __name__ == '__main__':
    unittest.main()

## 🔍 ОБЪЯСНЕНИЕ
# | Часть                            | Что делает                                                    |
# | -------------------------------- | ------------------------------------------------------------- |
# | `assertEqual(a, b)`              | Проверяет, что `a == b`. Если нет — тест упал                 |
# | `with self.assertRaises(Error):` | Проверяет, что в этом блоке **возникнет ошибка** типа `Error` |
# | `unittest.main()`                | Запускает тесты, если файл запускается как основная программа |

## ✅ Что в итоге?
# * 3 теста: ✔ обычный, ✔ ошибка, ✔ строка
# * Все **покрывают возможные случаи**
# * Всё работает автоматически
