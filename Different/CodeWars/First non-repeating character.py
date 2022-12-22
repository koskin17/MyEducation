'''
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
'''

string = 'Go hang a salami, I\'m a lasagna hog!'

def first_non_repeating_letter(string):
    if string == '':
        return string
    new_string = string.lower()
    for i in range(len(new_string)):
        if new_string.count(new_string[i]) == 1:
            return string[i]
    return ''

print(first_non_repeating_letter(string))

''' Второй вариант
В этой варианте итерация идёт сразу по двум спискам
и используется функция enumerate.
Она возвращает сразу и элемент, и его индекс,
т.е. формирует кортежи, состоящие из двух элементов –
индекса элемента и самого элемента:
>>> spisok = [16, 46, 26, 36]
>>> for i in enumerate(spisok):
...     print(i)
... 
(0, 16)
(1, 46)
(2, 26)
(3, 36)'''

def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""
