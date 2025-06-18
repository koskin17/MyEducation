#Task2.
#Print Fibonacci numbers up to the entered number n,using cycles.
#Sequence of Fibonacci numbers O, 1, 1, 2, 3, 5, 8, 13, etc.

def fibonacci(n):
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    return fib_sequence

number = int(input("Enter a number: "))
print(f"Fibonacci numbers up to {number}: {fibonacci(number)}")

