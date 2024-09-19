import unittest
from funk import cout_chen


"""Создание собственного класса тестов.
Он должен обязательно наследоваться от класса TestCase.
После этого в середне этого класса мы сможем писать тесты."""

"""Также есть дополнительная библиотека, которая проверяет, все ли варианты покрыты тестами,
все ли варианты проверены: Coverage.
Запускается она из терминала командой coverage run -m unittest discover """
class CountChenTests(unittest.TestCase):
    """Собственный класс тестов"""
    
    """В собственном классе тестов мы просто создаем функции / методы,
    которые должны начинаться со слова test_* и после этого вызываются методы self.assert"""
    def test_1(self):
        actual = cout_chen("hello")
        expected = {"h": 1, "e": 1, "l": 2, "o": 1}
        self.assertEqual(actual, expected)
    def test_2(self):
        actual = cout_chen("hello")
        expected = {"h": 1, "e": 1, "l": 2, "o": 1}
        self.assertIn('h', actual)
    def test_3(self):
        actual = cout_chen("hello")
        expected = {"h": 1, "e": 4, "l": 2, "r": 1}
        self.assertEqual(actual, expected)
        
        
if __name__ == '__main__':
    unittest.main()
    