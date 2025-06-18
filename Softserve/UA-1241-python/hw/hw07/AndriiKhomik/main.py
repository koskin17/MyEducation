# First task

def max_of_two_numbers(num1, num2):
    return num1 if num1 > num2 else num2


print(max_of_two_numbers(3, 8))
print(max_of_two_numbers(10, 8))

# Second task


def calculate_triangle(a, b):
    return (a * b) / 2


def calculate_rectangle(a, b):
    return a * b


def calculate_circle(r):
    PI = 3.14
    return PI * r**2


def main():
    print(calculate_triangle(10, 12))
    print(calculate_rectangle(10, 12))
    print(calculate_circle(10))


main()

# Third task


def calculate_characters(string):
    res = {}
    for char in string:
        if char.lower() in res.keys():
            res[char.lower()] += 1
        else:
            res[char.lower()] = 1
    return res


print(calculate_characters('Hello'))
