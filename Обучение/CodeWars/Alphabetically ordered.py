'''
Your task is very simple. Just write a function takes an input string of lowercase letters and returns true/false depending on whether the string is in alphabetical order or not.

Examples (input -> output)
"kata" -> false ('a' comes after 'k')
"ant" -> true (all characters are in alphabetical order)
'''

s = "kostia"
def alphabetic(s):
    if s == '':
        return True
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    first_letter_in_s = alphabet.index(s[0])
    print(first_letter_in_s)
    for letter in range(1, len(s)):
        print(s[letter])
        print(alphabet.index(s[letter]))
        if alphabet.index(s[letter]) >= first_letter_in_s:
            first_letter_in_s = alphabet.index(s[letter])
        else:
            return False
    return True

print(alphabetic(s))

''' Еще один вариант.
Строка является списком букв.
Если из этого списка сделать сортированный, то буквы
разместятся по возрастанию в алфавите.
Потом сравнивается два списка и если они отличаются, то упс.'''
def alphabetic(s):
    print(sorted(s))
    print(list(s))
    return sorted(s) == list(s)

print(alphabetic(s))
