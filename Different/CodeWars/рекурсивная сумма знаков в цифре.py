'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''

n = 493193

def digital_root(n):
    if len(str(n)) == 1:
        return int(n)
    else:
        n = list(map(int, str(n)))
        summ = 0
        for i in n:
            summ += int(i)
        return digital_root(summ)
    
print(digital_root(n))

''' Второй вариант.
Возвращается любое однозначное число или
при помощи функции map всем эдементам списка
присваивается тип данных int, а потом они сразу все ссумируются'''
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
