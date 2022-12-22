string = input('Введите строку: ')

def solution(string):
    reversed_string = string[::-1]
    return reversed_string

print(solution(string))
print()

''' Второй вариант '''
def solution(string):
  return string[::-1]

print(solution(string))
print()

''' Третий вариант '''
''' В этой случае используется встроенный итератор REVERSED, который берёт каждый символ в обратном порядке.
Из символов в обратном порядке формируется список " [.....] " из букв.
Для получения целого слова / предложения в этом случае нужно допольнительно использовать метод join '''
def solution(string):
  return ''.join(reversed(string))

print(solution(string))
print()
