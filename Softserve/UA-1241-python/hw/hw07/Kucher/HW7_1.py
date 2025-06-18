def func1(n1,n2):
    """ Функція для набільшого введеного + тест док.стрінга"""
    if (n1 > n2):
        print(n1," is greater than ",n2)
    else:
        print(n2," is greater than ",n1)

print(func1.__doc__)
print("Find which number is greater")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
func1(num1, num2)