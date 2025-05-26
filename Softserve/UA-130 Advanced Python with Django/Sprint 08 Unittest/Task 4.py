# Ест вот такая задача:
# Create class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size

# Examples:
# triangle = Triangle([3, 3, 3])
# Use classes TriangleNotValidArgumentException and TriangleNotExistException
# Create class TriangleTest with unittest and subTest() context manager for class Triangle. 
# test data:

# valid_test_data = [
#     ((3, 4, 5), 6.0),
#     ((10, 10, 10), 43.30),
#     ((6, 7, 8), 20.33),
#     ((7, 7, 7), 21.21),
#     ((50, 50, 75), 1240.19),
#     ((37, 43, 22), 406.99),
#     ((26, 25, 3), 36.0),
#     ((30, 29, 5), 72.0),
#     ((87, 55, 34), 396.0),
#     ((120, 109, 13), 396.0),
#     ((123, 122, 5), 300.0)
# ]
# not_valid_triangle = [
#     (1, 2, 3),
#     (1, 1, 2),
#     (7, 7, 15),
#     (100, 7, 90),
#     (17, 18, 35),
#     (127, 17, 33),
#     (145, 166, 700),
#     (1000, 2000, 1),
#     (717, 17, 7),
#     (0, 7, 7),
#     (-7, 7, 7)
# ]
# not_valid_arguments = [
#     ('3', 4, 5),
#     ('a', 2, 3),
#     (7, "str", 7),
#     ('1', '1', '1'),
#     'string',
#     (7, 2),
#     (7, 7, 7, 7),
#     'str',
#     10,
#     ('a', 'str', 7)
# ]

# Заготовка кода к ней:
# import unittest

# class TriangleNotValidArgumentException(Exception):
#     pass


# class TriangleNotExistException(Exception):
#     pass


# class Triangle:
#     pass


# class TriangleTest(unittest.TestCase):
#     pass

## 🧠 Суть задачи:

# Тебе нужно:
# 1. Создать **класс `Triangle`**, который:
#    * принимает **список из трёх сторон**,
#    * проверяет валидность данных,
#    * проверяет, может ли существовать треугольник с такими сторонами,
#    * имеет метод `get_area()` — возвращает **площадь** по формуле Герона.

# 2. Создать 2 **исключения**:
#    * `TriangleNotValidArgumentException` — если аргументы невалидны (например, строка вместо числа, не 3 значения и т.п.).
#    * `TriangleNotExistException` — если **треугольник с такими сторонами не существует** (не выполняется неравенство треугольника).

# 3. Написать **юнит-тесты** в `TriangleTest` с помощью `subTest()`.

## 🔣 Проверки в классе `Triangle`
# | Проверка                                | Исключение                          |
# | --------------------------------------- | ----------------------------------- |
# | Аргумент не `list`/`tuple`              | `TriangleNotValidArgumentException` |
# | Длина списка ≠ 3                        | `TriangleNotValidArgumentException` |
# | Элементы не числа или ≤ 0               | `TriangleNotValidArgumentException` |
# | Не выполняется неравенство треугольника | `TriangleNotExistException`         |

## 📐 Формула Герона
# Если три стороны: `a, b, c`, то:
# s = (a + b + c) / 2
# area = sqrt(s * (s - a) * (s - b) * (s - c))

## ✅ Полный рабочий код с комментариями:
import unittest
from math import sqrt

class TriangleNotValidArgumentException(Exception):
    """Exception for invalid triangle arguments"""
    def __init__(self, message="Not valid arguments"):
        self.message = message
        super().__init__(self.message)

class TriangleNotExistException(Exception):
    """Exception when triangle cannot be created with given sides"""
    def __init__(self, message="Can't create triangle with this arguments"):
        self.message = message
        super().__init__(self.message)

# | Компонент                                             | Назначение                                                   |
# | -------------------------------------------------     |--------------------------------------------------------------|
# | `class TriangleNotValidArgumentException(Exception):` | Наследует от базового класса исключений                      |
# | `def __init__(self, message=...)`                     | Позволяет указать сообщение                                  |
# | `self.message = message`                              | Сохраняем сообщение как атрибут                              |
# | `super().__init__(self.message)`                      | Передаём сообщение в родительский `Exception` (чтобы `raise` с этим классом работал как обычное исключение) |


class Triangle:
    def __init__(self, sides):
        # Check the type
        if not isinstance(sides, (list, tuple)):
            raise TriangleNotValidArgumentException()

        # Check the lenght
        if len(sides) != 3:
            raise TriangleNotValidArgumentException()

        a, b, c = sides

        # Chech that all numbers is a number
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise TriangleNotValidArgumentException()
        
        # Check that all numbers is a positive number
        if not all(x > 0 for x in (a, b, c)):
            raise TriangleNotExistException()

        # Triangle inequality
        if a + b <= c or a + c <= b or b + c <= a:
            raise TriangleNotExistException()

        # After all tests save given sides
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return round(area, 2)

class TriangleTest(unittest.TestCase):
    """ Tests with correct parameters / sides """

    def test_valid_triangles(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.3),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        for sides, expected_area in valid_test_data:
            with self.subTest(sides=sides):
                triangle = Triangle(sides)
                self.assertAlmostEqual(triangle.get_area(), expected_area, delta=0.02)
                """
                More correct to use delta=: self.assertAlmostEqual(triangle.get_area(), expected_area, delta=0.02)
                This allows to check that the error does not exceed a certain threshold.
                """

    def test_not_valid_triangle(self):
        """ Tests with not exist triangle"""

        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        for sides in not_valid_triangle:
            with self.subTest(sides=sides):
                with self.assertRaises(TriangleNotExistException):
                    Triangle(sides)

    def test_invalid_arguments(self):
        """ Tests with not correct parameters / sides """

        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]
        for args in not_valid_arguments:
            with self.subTest(args=args):
                with self.assertRaises(TriangleNotValidArgumentException):
                    Triangle(args)


if __name__ == "__main__":
    unittest.main()

## 💬 Что стоит запомнить
# * Класс `Triangle` проверяет ВСЁ на этапе `__init__`
# * Площадь считается через метод `get_area()`
# * Все проверки сделаны по best practice через исключения
# * Тесты покрывают 100% кейсов:
#   * Валидные
#   * Не существующие треугольники
#   * Невалидные аргументы
# * `subTest()` — удобно для множественных проверок без остановки
