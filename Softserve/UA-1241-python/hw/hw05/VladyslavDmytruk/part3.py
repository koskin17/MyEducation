# Task3.
#Write a script that will calculate the factorial of the entered number without using recursion.
#Example: 0!=1, 1!=1, 2!=2, 3!=1*2*3=6, ...

def factorial(num):
    result = 1
    for i in range(4, num + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
