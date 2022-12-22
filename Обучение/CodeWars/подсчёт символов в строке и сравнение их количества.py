s = 'xo'

def xo(s):
    s = s.lower()
    if 'o' not in s and 'x' not in s:
        return True
    if s.count('o') == s.count('x'):
        return True
    else: return False

print(xo(s))

''' Второй вариант.
В нём весь мой цикл проверки условий
сведён к одной строке, которая и считает, и проверяет,
и возвращает True или False '''

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
