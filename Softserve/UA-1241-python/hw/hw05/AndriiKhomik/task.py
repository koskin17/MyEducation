# First task
list_numbers = []

for x in range(50):
    list_numbers.append(x)

transform_to_float = []

for x in list_numbers:
    transform_to_float.append(float(x))

# Second task
def fibonacci_sequence(n):
    fibonacci = [0, 1] 

    while True:
        next_number = fibonacci[-1] + fibonacci[-2]
        if next_number >= n:
            break
        fibonacci.append(next_number)

    return fibonacci

fibonacci_sequence(10)

# Third task
def factorial(n):
    if n <= 1:
        return n
    res = 1
    for i in range(2, n + 1):
        res *= i

    return res

print(factorial(5))