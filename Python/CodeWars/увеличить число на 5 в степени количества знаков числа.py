''' Нужно умножить число на 5 в степени, равной числу знаков
переданом числе '''
n = int(input('Введите число: '))

def multiply(n):
    lenght = len(str(abs(n)))
    result = n * 5**lenght
    return result

print(multiply(n))
