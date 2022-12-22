a = [1, 2, 2, -1, 5]

def solution(a):
    position = 0
    jumps = 0
    for i in range(len(a)):
        if a[0] < 0:
            return -1
        elif a[position] == 0:
            continue
        elif a[position] < len(a[position:]):
            jumps += 1
            position += a[position]
        else:
            jumps += 1
            return jumps
    return -1

print(solution(a))

''' Второй вариант '''

def solution(a):
    steps = 0
    index = 0
    length = len(a)
    indexes = set()
    while 0 <= index < length:
        if index in indexes:
            return -1
        indexes.add(index)
        index += a[index]
        steps += 1
    return steps

print(solution(a))

''' Трейтий вариант '''
def solution(a):
    if (len(a) == 0):
        return -1
    pos = 0
    jump = 0
    while pos >= 0 and pos < len(a):
        if (a[pos] == 0): return -1
        step = a[pos]
        a[pos] = 0
        pos += step
        jump += 1
    return jump
