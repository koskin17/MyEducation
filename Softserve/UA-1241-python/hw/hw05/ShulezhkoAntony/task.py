#Task 1
int_list = [1, 2, 3, 4, 5]
float_list = []
for element in int_list:
    float_list.append(float(element))
print("Original list:", int_list)
print("Converted to float list:", float_list)

#Task 2
def fibonacci_number(n):
    a, b = 0, 1
    fibonacci_sequence = []
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
n = int(input("Enter a number: "))
fibonacci_sequence = fibonacci_number(n)
print(f"Fibonacci numbers up to {n}: {fibonacci_sequence}")

#Task 3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")