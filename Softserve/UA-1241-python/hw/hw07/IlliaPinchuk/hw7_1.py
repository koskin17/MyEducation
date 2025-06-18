def largest_number(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The largest of the two numbers.
    """
    return max(a, b)

def test_largest_number():
    assert largest_number(10, 20) == 20, "Test case 1 failed"

    assert largest_number(-10, -20) == -10, "Test case 2 failed"

    assert largest_number(-10, 20) == 20, "Test case 3 failed"

    assert largest_number(0, 10) == 10, "Test case 4 failed"

    assert largest_number(0, -10) == 0, "Test case 5 failed"

    assert largest_number(10, 10) == 10, "Test case 6 failed"

    assert largest_number(10.5, 20.3) == 20.3, "Test case 7 failed"

    assert largest_number(10, 20.3) == 20.3, "Test case 8 failed"

    assert largest_number(10.5, 10.5) == 10.5, "Test case 9 failed"

    print("All test cases passed!")

test_largest_number()
