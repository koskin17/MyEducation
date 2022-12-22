arr = ["cat",""]

def transpose_two_strings(arr):
    l = []
    s1 = ''
    s2 = ''
    if len(arr[0]) < len(arr[1]) or arr[0] == '':
        s1 = arr[0] + ' '*(len(arr[1]) - len(arr[0]))
        s2 = arr[1]
    elif len(arr[1]) < len(arr[0]) or arr[1] == '':
            s1 = arr[0]
            s2 = arr[1] + ' '*(len(arr[0]) - len(arr[1]))
    else:
        s1 = arr[0]
        s2 = arr[1]
    for x,y in zip(s1, s2):
        tmp = x + ' ' + y
        l.append(tmp)
    return '\n'.join(l)

print(transpose_two_strings(arr))


''' Второй вариант '''

from itertools import zip_longest

def transpose_two_strings(lst):
    return "\n".join(f"{a} {b}" for a, b in zip_longest(*lst, fillvalue=" "))
