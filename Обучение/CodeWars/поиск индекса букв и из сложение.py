'''
Перевод букв в цифры и нахождение суммы
'''

s = input('Введите слово: ')

def words_to_marks(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    summ = 0
    for i in range(len(s)):
        print(alphabet.index(s[i]))
        summ += alphabet.index(s[i])+1
    return summ

print(words_to_marks(s))

''' Второй вариант '''
def words_to_marks(s):
  return sum(ord(c)-96 for c in s)
