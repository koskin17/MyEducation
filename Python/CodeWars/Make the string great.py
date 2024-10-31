'''
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
'''

chars = ['k','l','n','o','p']               # получаем список из букв

def find_missing_letter(chars):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")    # алфавит, по которому будет поиск пропущенной буквы
    chars_mn = set(chars)               # делаем из полученной строки множество, чтобы потом сравнить два множества
    chars_alphabet = set(alphabet[alphabet.index(chars[0]):alphabet.index(chars[len(chars)-1])])    # Для сравнения строки с алфавитом
                                                                                                    # формируется множество букв с первой по последнюю букву строки 
    letter = chars_alphabet.difference(chars_mn)                # методом difference, которое возвращает отсутствующи�