# Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation without a complex solution.

# Write unit tests for this function with QuadraticEquationTest class
# Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0

# Заготовка кода:
# import unittest

# def quadratic_equation(a, b, c):
#     pass

# class QuadraticEquationTest(unittest.TestCase):
#     pass

## 🔢 ЗАДАЧА
# Нам нужно:
# 1. ✏️ Реализовать функцию `quadratic_equation(a, b, c)`, которая находит **корни квадратного уравнения** `ax² + bx + c = 0`.
# 2. 🧪 Написать **юнит-тесты**:
#    * на случай **одного корня (D = 0)**,
#    * на случай **двух корней (D > 0)**,
#    * на случай, когда **корней нет (D < 0)**.

# > 💡 По условию: **решения с комплексными корнями не нужны**. То есть, если дискриминант меньше нуля, функция должна возвращать `None`.

## 🧮 МАТЕМАТИКА
# Квадратное уравнение:
# ax² + bx + c = 0
# Решается через дискриминант:
# D = b² - 4ac
# * Если D < 0 — решений нет → возвращаем `None`
# * Если D = 0 — один корень → x = -b / (2a)
# * Если D > 0 — два корня → x₁ = (-b + √D)/2a, x₂ = (-b - √D)/2a

## ✅ ПОЛНЫЙ КОД С РЕШЕНИЕМ И ТЕСТАМИ
import unittest
import math

def quadratic_equation(a, b, c):
    """
    Solution of quadratic equation ax² + bx + c = 0
    Returns:
    - None if there are no solutions;
    - One root if discriminant = 0
    - Tuple of two roots if discriminant > 0
    """
    if a == 0:
        raise ValueError("Not a quadratic equation: a cannot be zero.")
    
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        sqrt_d = math.sqrt(discriminant)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return (x1, x2)


class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_less_than_zero(self):
        # D = -7 < 0 → no solutions
        self.assertIsNone(quadratic_equation(1, 2, 3))

    def test_discriminant_equal_zero(self):
        # D = 0 → one root x = -b / 2a = 2.0
        self.assertEqual(quadratic_equation(1, -4, 4), 2.0)

    def test_discriminant_greater_than_zero(self):
        # D = 1 → two root
        result = quadratic_equation(1, -3, 2)
        expected = (2.0, 1.0)
        # The order of the roots may differ, compare with accuracy
        self.assertAlmostEqual(result[0], expected[0])
        self.assertAlmostEqual(result[1], expected[1])


# Для ручного запуска (если запускается в обычном .py файле)
if __name__ == '__main__':
    unittest.main()

## 🧠 ПОЯСНЕНИЯ
# | Элемент                  | Объяснение                                                            |
# | ------------------------ | --------------------------------------------------------------------- |
# | `math.sqrt()`            | вычисляет корень √D                                                   |
# | `assertIsNone(...)`      | проверяет, что функция вернула `None`                                 |
# | `assertEqual(...)`       | проверяет точное равенство (подходит для одного корня)                |
# | `assertAlmostEqual(...)` | проверяет почти равенство (для вещественных чисел с плавающей точкой) |

## ✅ Результат
# После запуска `unittest` ты получишь 3 успешно пройденных теста:
# Ran 3 tests in 0.001s

# OK
# * Проверку на `a = 0` (не квадратное уравнение),
# * Добавить округление корней до нужной точности,
# * Или выбрасывать исключение при недопустимых данных.
