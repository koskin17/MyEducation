n = int(input('Введите число для расчёта последовательности Фибоначчи: '))
f = [0, 1]
def fibo(n):
    if n <= 1:
        print('0\n1')
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    print(f)

fibo(n)
