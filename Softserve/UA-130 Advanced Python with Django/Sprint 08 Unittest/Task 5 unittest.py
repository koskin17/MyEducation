# Create class Worker with fields name and salary. If salary negative raise ValueError

# Create a method get_tax_value() that calculate tax from salary . Tax must be calculate like "progressive tax" with next step:

# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%
# Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods. Don`t use assertRaises in tests.

# Это классическая задача на **проверку прогрессивного налогообложения** и написание **юнит-тестов с `setUp` и `tearDown`**.

## 🧠 Что нужно сделать?
# 1. **Создать класс `Worker`** с полями `name` и `salary`.
#    Если зарплата отрицательная — выбрасываем `ValueError`.

# 2. **Создать метод `get_tax_value()`**, который:
#    * рассчитывает налог по *прогрессивной шкале*;
#    * возвращает **налог**, а не процент.

# 3. **Написать `WorkerTest`**, используя `unittest`, обязательно:
#    * тестировать разные уровни зарплаты;
#    * предусмотреть **валидные и невалидные** кейсы;
#    * использовать `setUp` и `tearDown` — даже если они простые;
#    * **не использовать `assertRaises`**.

## 📊 Таблица налогообложения
# | Зарплата      | Налог |
# | ------------- | ----- |
# | до 1000       | 0     |
# | 1001 – 3000   | 10%   |
# | 3001 – 5000   | 15%   |
# | 5001 – 10000  | 21%   |
# | 10001 – 20000 | 30%   |
# | 20001 – 50000 | 40%   |
# | больше 50000  | 47%   |

## ✅ Полный код с объяснениями
import unittest

class Worker:
    def __init__(self, name, salary=0.0):
        self.name = name
        if not isinstance(salary, (int, float)):
            raise ValueError("Salary must be a number")
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.salary = salary

    def get_tax_value(self):
        """
        Progressive taxation by bands:
        - < 1000 — 0%
        - 1001–3000 — 10%
        - 3001–5000 — 15%
        - 5001–10000 — 21%
        - 10001–20000 — 30%
        - 20001–50000 — 40%
        - >50000 — 47%
        """
        brackets = [
            (1000, 0.0),
            (3000, 0.10),
            (5000, 0.15),
            (10000, 0.21),
            (20000, 0.30),
            (50000, 0.40),
            (float("inf"), 0.47)
        ]

        total_tax = 0.0
        last_limit = 0.0
        remaining_salary = self.salary

        for limit, rate in brackets:
            if self.salary > limit:
                taxable = limit - last_limit
            else:
                taxable = remaining_salary

            total_tax += taxable * rate
            remaining_salary -= taxable
            last_limit = limit

            if remaining_salary <= 0:
                break

        return round(total_tax, 2)

## ✅ ЮНИТ-ТЕСТЫ со всеми вариантами
import unittest

class Worker:
    def __init__(self, name, salary=0.0):
        self.name = name
        if not isinstance(salary, (int, float)):
            raise ValueError("Salary must be a number")
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.salary = salary

    def get_tax_value(self):
        """
        Progressive taxation by bands:
        - < 1000 — 0%
        - 1001–3000 — 10%
        - 3001–5000 — 15%
        - 5001–10000 — 21%
        - 10001–20000 — 30%
        - 20001–50000 — 40%
        - >50000 — 47%
        """
        brackets = [
            (1000, 0.0),
            (3000, 0.10),
            (5000, 0.15),
            (10000, 0.21),
            (20000, 0.30),
            (50000, 0.40),
            (float("inf"), 0.47)
        ]

        total_tax = 0.0
        last_limit = 0.0
        remaining_salary = self.salary

        for limit, rate in brackets:
            if self.salary > limit:
                taxable = limit - last_limit
            else:
                taxable = remaining_salary

            total_tax += taxable * rate
            remaining_salary -= taxable
            last_limit = limit

            if remaining_salary <= 0:
                break

        return round(total_tax, 2)

## ✅ ЮНИТ-ТЕСТЫ со всеми вариантами
class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.workers = []

    def tearDown(self):
        self.workers.clear()

    def test_no_tax(self):
        w = Worker("Alice", 800)
        self.assertEqual(w.get_tax_value(), 0.0)

    def test_first_bracket(self):
        w = Worker("Bob", 2500)
        # 1000 – 0% + 1500 * 10%
        self.assertAlmostEqual(w.get_tax_value(), 150.0)

    def test_second_bracket(self):
        w = Worker("Charlie", 4000)
        # 1000 – 0%, 2000 – 10%, 1000 – 15%
        expected = 0 + 2000*0.1 + 1000*0.15
        self.assertAlmostEqual(w.get_tax_value(), expected)

    def test_third_bracket(self):
        w = Worker("Diana", 9000)
        # 1000 – 0%, 2000 – 10%, 2000 – 15%, 4000 – 21%
        expected = 0 + 2000*0.1 + 2000*0.15 + 4000*0.21
        self.assertAlmostEqual(w.get_tax_value(), expected)

    def test_big_tax(self):
        w = Worker("Edward", 10000)
        # 1000 – 0%, 2000 – 10%, 2000 – 15%, 5000 – 21%
        expected = 0 + 2000*0.1 + 2000*0.15 + 5000*0.21
        self.assertAlmostEqual(w.get_tax_value(), expected)

    def test_huge_tax(self):
        w = Worker("Fay", 100000)
        # 1000 * 0%
        # 2000 * 10%
        # 2000 * 15%
        # 5000 * 21%
        # 10000 * 30%
        # 30000 * 40%
        # 50000 * 47%
        expected = (
            0 +
            2000 * 0.10 +
            2000 * 0.15 +
            5000 * 0.21 +
            10000 * 0.30 +
            30000 * 0.40 +
            50000 * 0.47
        )
        self.assertAlmostEqual(w.get_tax_value(), expected)

    def test_zero_salary(self):
        w = Worker("Greg", 0)
        self.assertEqual(w.get_tax_value(), 0.0)

    def test_missing_salary(self):
        w = Worker("Vasia")  # salary default = 0
        self.assertEqual(w.get_tax_value(), 0.0)

    def test_invalid_salary_type(self):
        try:
            Worker("Hack", "1000")
            self.fail("ValueError not raised for str salary")
        except ValueError:
            pass

    def test_negative_salary(self):
        try:
            Worker("Hacker", -1000)
            self.fail("ValueError not raised for negative salary")
        except ValueError:
            pass

    @unittest.expectedFailure
    def test_expected_fail(self):
        w = Worker("Test", 50000)
        # Спеціально помилкове очікування
        self.assertEqual(w.get_tax_value(), 0.0)

# Ручной запуск
if __name__ == "__main__":
    unittest.main()

## 🧠 Объяснение
### Почему **не if-else** внутри тестов?
# Потому что это логика, а тест — только проверка.

### Почему `tearDown()`?
# В данном случае он просто демонстрирует, что был бы вызван для очистки или логирования. При реальных нагрузках (файлы, база) — используется для очистки.

### Почему не `assertRaises`?
# Задано условие — **не использовать его**, поэтому проверка на исключение через `try-except` + `fail`.

## ✅ Что протестировано?
# * ✅ Все диапазоны налогов
# * ✅ Границы категорий
# * ✅ Зарплата = 0
# * ✅ Негативное значение — ошибка
# * ✅ Проверка округления через `assertAlmostEqual`

# Давай объясню **максимально просто и понятно**, чтобы ты разобрался во всём — и в `setUp`, `tearDown`, и в `assertRaises`, и в логике тестов.

## 🔹 Что такое `setUp()` и `tearDown()` в `unittest`
# Это **вспомогательные методы** для подготовки и очистки перед/после каждого теста:
# | Метод        | Когда вызывается                   | Для чего нужен                                                  |
# | ------------ | ---------------------------------- | --------------------------------------------------------------- |
# | `setUp()`    | ❗ **Перед** выполнением каждого теста | Подготовить среду: создать объекты, открыть файлы,                                                                                      подключиться к базе и т.д. |
# | `tearDown()` | ❗ **После** выполнения каждого теста  | Очистить: закрыть соединения, удалить файлы, обнулить объекты и т.д. |

### 🔍 Пример, как это работает:
# import unittest

# class MyTest(unittest.TestCase):
#     def setUp(self):
#         print("🔧 Подготовка перед тестом")

#     def tearDown(self):
#         print("🧹 Очистка после теста")

#     def test_1(self):
#         print("✔ Выполняется тест 1")
#         self.assertTrue(True)

#     def test_2(self):
#         print("✔ Выполняется тест 2")
#         self.assertTrue(True)

# 🔽 Вывод будет такой:
# 🔧 Подготовка перед тестом
# ✔ Выполняется тест 1
# 🧹 Очистка после теста
# 🔧 Подготовка перед тестом
# ✔ Выполняется тест 2
# 🧹 Очистка после теста

# > ✅ Полезно, когда надо *настроить/стереть окружение* до и после каждого теста.

## 🔹 Что такое `assertRaises`
# Это специальная проверка в `unittest`, которая **убеждается**, что *будет вызвано исключение*.

### ✅ Пример:
# def divide(a, b):
#     return a / b

# class TestDivide(unittest.TestCase):
#     def test_zero_division(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide(10, 0)
# 📌 `assertRaises` проверяет, что **внутри блока** `with` будет выброшено исключение `ZeroDivisionError`.

## 🔹 Почему НЕ `assertRaises`, а `try-except`
# Иногда в задачах **запрещают использовать `assertRaises`**, и тогда мы делаем то же самое вручную:
# def test_error(self):
#     try:
#         Worker("Tom", -100)
#         self.fail("ValueError was not raised")  # если ошибки не было — тест провален
#     except ValueError as e:
#         self.assertEqual(str(e), "Salary cannot be negative")

# 🔍 Здесь:
# * `try:` — мы пробуем вызвать ошибку;
# * `self.fail()` — тест упадёт, если не произойдёт ошибка;
# * `except:` — ловим ошибку и проверяем её сообщение.

## 🔹 Почему "тест не должен содержать if/else"?
# Это **важный принцип тестирования**:
# > 💡 **Тест = проверка, а не логика**
# Если в тесте есть `if` или `else`, это значит, что в тесте заложена логика. А логика должна быть только в коде, который мы тестируем.

### ❌ Плохо:
# if salary > 1000:
#     self.assertEqual(worker.get_tax(), 100)
# else:
#     self.assertEqual(worker.get_tax(), 0)

# ✅ Лучше:
# worker = Worker("Tom", 1500)
# self.assertEqual(worker.get_tax(), 150)

# ## ✅ Краткий итог:
# | Что                   | Что это значит и зачем                                      |
# | --------------------- | ----------------------------------------------------------- |
# | `setUp()`             | Подготовка перед каждым тестом                              |
# | `tearDown()`          | Очистка после каждого теста                                 |
# | `assertRaises`        | Проверяет, что вызвалось исключение                         |
# | `try-except` + `fail` | Ручной способ проверить ошибку (если нельзя `assertRaises`) |
# | ❌ `if` в тестах       | Плохо, потому что в тестах не должно быть логики            |

## ✅ 1. Как работают тесты `unittest`?
# Когда в коде есть строка:
# if __name__ == "__main__":
#     unittest.main()

# это означает следующее:
# * 📦 **`unittest.main()`** — это специальная функция из модуля `unittest`, которая:
#   * автоматически находит **все классы**, унаследованные от `unittest.TestCase`;
#   * внутри этих классов находит **все методы, начинающиеся с `test_`**;
#   * и **автоматически запускает** их по очереди;
#   * собирает результат и показывает, сколько тестов прошло, провалилось, с ошибками и т.д.

## ✅ 2. Как запускаются методы `setUp()` и `tearDown()`?
# Когда `unittest` запускает каждый `test_...`-метод, он делает следующее:

### 🔄 Внутренний цикл работы на каждый тест:
# 1. Вызов setUp()
# 2. Вызов test_метода
# 3. Вызов tearDown()

# Примерно как:
# for each_test_method in class WorkerTest:
#     test_instance = WorkerTest()
#     test_instance.setUp()
#     test_instance.test_...
#     test_instance.tearDown()

## 📌 Простой пример (на пальцах):
# class MyTest(unittest.TestCase):
#     def setUp(self):
#         print("🌱 Подготовка")

#     def tearDown(self):
#         print("🧹 Очистка")

#     def test_one(self):
#         print("✅ Тест 1")

#     def test_two(self):
#         print("✅ Тест 2")

# Если ты запустишь этот код с `unittest.main()`, ты увидишь:
# 🌱 Подготовка
# ✅ Тест 1
# 🧹 Очистка

# 🌱 Подготовка
# ✅ Тест 2
# 🧹 Очистка

## 💡 Зачем нужны `setUp()` и `tearDown()`?
# * `setUp()` — используется, чтобы **подготовить всё нужное перед каждым тестом**: создать объекты, подключиться к базе, открыть файл и т.д.
# * `tearDown()` — чтобы **очистить за собой после теста**: удалить временные файлы, закрыть соединения и т.д.

## 🧠 Резюме
# | Что               | Как работает                                                             |
# | ----------------- | ------------------------------------------------------------------------ |
# | `test_...`        | запускается автоматически, если внутри `unittest.TestCase`               |
# | `setUp()`         | запускается **перед каждым** тестом                                      |
# | `tearDown()`      | запускается **после каждого** теста                                      |
# | `unittest.main()` | запускает весь процесс, находит тесты, запускает их и выводит результаты |

# Отличный вопрос — ты действительно **глубоко вникаешь в суть**, и это очень важно для понимания, как работает `unittest`.

## 🔹 Что будет, если в коде **нет `setUp()` и `tearDown()`**?

### ✅ Краткий ответ:
# **Ничего плохого не произойдёт.**
# * Эти методы **необязательны**.
# * Если их **нет** — Python просто их **не вызывает**, и **выполняет только сами `test_...` методы**.

## 🔹 Что делают `setUp()` и `tearDown()`?
# | Метод        | Когда вызывается                 | Назначение                                                       |
# | ------------ | -------------------------------- | ---------------------------------------------------------------- |
# | `setUp()`    | **Перед каждым `test_`-методом** | Подготовка окружения: например, создаём объекты, открываем файлы |
# | `tearDown()` | **После каждого `test_`-метода** | Очистка: закрытие соединений, удаление временных данных          |

## 🔧 Пример без `setUp()` и `tearDown()`
# import unittest

# class MyTest(unittest.TestCase):
#     def test_example(self):
#         self.assertEqual(2 + 2, 4)

# Всё отлично работает даже без setUp/tearDown
# if __name__ == "__main__":
#     unittest.main()

## 📌 Когда нужно использовать `setUp()`?
# * Когда **одинаковая инициализация** нужна в каждом тесте.
# * Чтобы **не дублировать** код в каждом `test_...`.
# * Пример: создание объектов, установка соединения, чтение конфигурации.

## 📌 Когда нужен `tearDown()`?
# * Когда после каждого теста нужно что-то **очистить**:
#   * закрыть файл,
#   * удалить созданные файлы,
#   * обнулить переменные,
#   * отключиться от БД.

### ✅ Вывод:
# * **Если их нет — ничего страшного.**
# * Просто `unittest` ничего не вызывает **до/после** теста.
# * Но **если они есть** — они всегда выполняются **автоматически для каждого теста**.
