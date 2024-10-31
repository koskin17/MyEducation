n = int(input('Введите число: '))
list_divisors = []

def divisors(n):
    count = 0
    for i in range(1, n+1):
        if n %i == 0:
            count += 1
            list_divisors.append(i)
    return count

print(divisors(n))
