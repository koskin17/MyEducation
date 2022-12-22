'''
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
'''

s = 'asdaas'
print(len(s)/2)
print(int(len(s)/2))

def get_middle(s):
    if len(s)%2 != 0:
        return s[int(len(s)/2)]
    else:
        return str(s[int(len(s)/2-1)])+str(s[int(len(s)/2)])

print(get_middle(s))

''' Второй вариант.
В этом варианте:
- функция divmode принимает 2 числа и возвращает их частное и остаток,
которые присваиваются двум переменным
- при остатке 0 (ноль) переменной как бы не существует,
т.е при проверке в цикле if odd возвращается False.
Таким образом запись после return говорит:
вернуть букву с индексом index, если переменная odd существует, т.е. она больше нуля
в противном случае вернуть срез строки от предыдущей буквы до следующей'''
def get_middle(s):
    index, odd = divmod(len(s), 2)
    print(index)
    print(odd)
    return s[index] if odd else s[index - 1:index + 1]

print(get_middle(s))
