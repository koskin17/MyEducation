''' Необходимо из полученной строки кажду букву написано с верхнем регистре
и повторить её число раз, равное её позиции в строке '''

s = input('Введите последовательность букв: ')

def accum(s, string=''):
    for letter in range(len(s)):
        simbol = s[letter].upper() + s[letter]*(letter)
        if letter == 0:
            string += simbol
            continue
        string += '-' + simbol
    return string

print(accum(s))

