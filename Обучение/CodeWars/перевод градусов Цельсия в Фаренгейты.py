celsius = int(input('Введите градусы Цельсия, пожалуйста: '))

def conv(c):
    fahren = 9/5 * c + 32
    return fahren
    

fahrenheit = conv(celsius)
print(fahrenheit)
