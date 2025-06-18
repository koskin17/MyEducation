list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_int = [float(i) for i in list_int]

print(list_int)

#________________________________________

fibonacci_num = [0, 1]

num = 1

while num <= 100:

    fibonacci_num.append(fibonacci_num[num - 1] + fibonacci_num[num])
    num += 1

print(fibonacci_num)

#________________________________________

def factorial(num):
    if num == 0: return 1

    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    
print(factorial(0))
print(factorial(4))
print(factorial(30))