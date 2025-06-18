# Task3. Write a script that will calculate the factorial 
# of the entered number without using recursion.
# Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, ....

n = int(input("Please, enter the number: "))

res = 1
while (n > 0):
    res = n * res
    n = n - 1

print(res)
