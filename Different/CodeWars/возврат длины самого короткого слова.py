'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

s = 'строка из нескольких слов, из которых надо найти самое короткое и посчитать его длину'

def find_short(s):
    s = s.split()                               # из строки формируется список слов
    l = len(s[0])                               # считается длина первого слова
    for word in s:                              # в цикле для каждого слова в сформированном списке
        if len(word) < l:                       # считается длина и сравнивается с длиной первого слова
            l = len(word)                       # если длина очередного слова в списке короче уже имеющегося,
    return l                                    # то в качестве самого короткого принимается это слова

print(find_short(s))

''' Второй вариант '''
def find_short(s):
    return min(len(x) for x in s.split())       # цикл из предыдущего варианта записан в одну строку и сразу возвращается
                                                # в качестве результата функции

print(find_short(s))
