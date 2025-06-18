# Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)


def fibonacci_with_list(n):
    fib_series = [0, 1]
    for n in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
n = int(input("Enter a number: "))
result = fibonacci_with_list(n)
print(f"Fibonacci series with {n} elements:", result)