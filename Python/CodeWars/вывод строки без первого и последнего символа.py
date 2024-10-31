s = 'привет как дела'

def remove_char(s):
    return s[len(s) - (len(s) - 1):(len(s)-1)]

print(remove_char(s))

''' Второй вариант '''
def remove_char(s):
    return s[1 : -1]
