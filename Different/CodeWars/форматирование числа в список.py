n = 123
result = []

while n > 0:
    result.append(n % 10)
    print(result)
    n //= 10
result.reverse()
print(result)
print(sum(result))
print('---')

''' Второй вариант '''
n2 = 1234
n2 = list(str(n2))
result2 = []

for i in n2:
    result2.append(int(i))
    print(result2)

summ2 = sum(result2)
print(summ2)
print('---')

''' Третий вариант
В этом случае при помощи функции map
каждому элементу списка n3 присваивается тип данных int,
т.е. каждый элемент становится целым числов в списке'''
n3 = 12345
n3 = list(map(int, str(n3)))
print(n3)
