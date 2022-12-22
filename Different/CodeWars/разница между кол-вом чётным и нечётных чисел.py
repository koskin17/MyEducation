a = [0,1,2,3]

def solve(a):
    even = 0
    letters = 0
    for i in range(len(a)):
        if type(a[i]) != str:
            letters += 1
            if a[i]%2 == 0:
                print(a[i])
                even += 1
        else: continue
    return even - (letters - even)

print(solve(a))

''' Второй вариант.
Всё также, как и в моём, но суммируются единицы и на лету
'''
def solve(a):
    return sum(1 if v % 2 == 0 else -1 for v in a if type(v) == int)
