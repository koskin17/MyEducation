import unittest

class MyExceptions(Exception):
    pass

def sum_slice_array(arr, first, second):
    if not (isinstance(first, int) and isinstance(second, int) and first >= 1 and second >= 1):
        raise MyExceptions("Indexes must be integers ≥ 1")
    
    if first > len(arr) or second > len(arr):
        raise MyExceptions("Indexes out of range")

    elem1 = arr[first - 1]
    elem2 = arr[second - 1]
    if not (isinstance(elem1, (int, float)) and isinstance(elem2, (int, float))):
        raise MyExceptions("Elements must be numbers")

    return float(elem1 + elem2)


class TestSumSliceArray(unittest.TestCase):
    def test_valid_sum(self):
        self.assertEqual(sum_slice_array([1, 2, 3], 1, 2), 3.0)

    def test_valid_sum_floats(self):
        self.assertEqual(sum_slice_array([1.5, 2.5], 1, 2), 4.0)

    def test_negative_index(self):
        with self.assertRaises(MyExceptions):
            sum_slice_array([1, 2, 3], -1, 2)

    def test_index_out_of_range(self):
        with self.assertRaises(MyExceptions):
            sum_slice_array([1, 2, 3], 1, 5)

    def test_element_not_number(self):
        with self.assertRaises(MyExceptions):
            sum_slice_array([1, "two", 3], 1, 2)

    def test_index_not_integer(self):
        with self.assertRaises(MyExceptions):
            sum_slice_array([1, 2, 3], "1", 2)

if __name__ == '__main__':
    unittest.main()

# ✅ Как запустить:
# Сохрани как test_sum_slice_array.py, затем:

# python test_sum_slice_array.py

# Ты увидишь:
# .
# .
# .
# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s

# OK