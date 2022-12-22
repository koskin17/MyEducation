s = 'Lets go to the movies'

def vaporcode(s):
    s = ' '.join(s)
    s = s.split()
    s = ''.join(s)
    return ' '.join(s.upper())

print(vaporcode(s))

''' Второй вариант.
В нём сначала убираются все пробелы в строке.
Потом все буквы переводятся в верхний регистр.
Потом все буквы соединяются в строку через пробел'''
def vaporcode(s):
    return "  ".join(s.replace(" ", "").upper())
