"""Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2.
In the alphabet, a and b are also in positions 1 and 2.
Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words,
return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) = [4, 3, 1]"""

arr = ["encode","abc","xyzD","ABmD"]

def solve(arr):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    q = []
    for word in arr:
        count = 0
        for i in range(len(word)):
            if i == alphabet.index(word[i].lower()):
                count += 1
        q.append(count)
    return q

print(solve(arr))

''' Второй вариант
В этом случае берётся каждое слово,
потом каждая буква этого слова и её индексом в слове функцией enumerate
и суммируется кол-во букв, индекс которых равен индексу с системе CHR+индекс этой
буквы в слове.
Т.е. если буква из слова равна букве в системе CHR по индексу 97+i, то буква суммируется
'''
def solve(arr):
    return [ sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr ]
