# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

n = int(input("Please enter number: "))
result = 0
list = [0, 1]

while(result <= n and n >=1):
    temp = list[len(list) - 2] + list[len(list) - 1]
    if (temp <= n):
        list.append(temp)
    result = temp

print(list)