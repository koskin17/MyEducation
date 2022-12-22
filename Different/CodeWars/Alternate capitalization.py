'''
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
'''
s = "codewars"


def capitalize(s):
    string1 = ''
    string2 = ''
    for i in range(len(s)):
        if i % 2 == 0:
            string1 += str(s[i].upper())
        else:
            string1 += str(s[i])
    for i in range(len(s)):
        if i % 2 != 0:
            string2 += str(s[i].upper())
        else:
            string2 += str(s[i])
    return [string1, string2]

print(capitalize(s))

''' Второй вариант.
В нём в строку s объединяются буквы,после проверки функцией enumerate, которая возвращает и индекс, и значение.
Т.е. с добавляется строчной к строке s, если её индекс делится нацело на 2 или же буква перводится в ВЕРХНИЙ регистр и потом добавляется к s
После этого выводится получивщаяся строка и её, но методо swapcase, который меняет все регистры на противоположные'''
def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]
