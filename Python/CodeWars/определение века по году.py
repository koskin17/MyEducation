''' Нужно определить век по полученному году'''
year = int(input('Введите год: '))

def century(year):
    if year %100 == 0:
        return int(year / 100)
    return int(year/100) + 1

print(century(year))
