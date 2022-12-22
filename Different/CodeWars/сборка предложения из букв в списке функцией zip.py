arr = [
            ['J','L','L','M'],
            ['u','i','i','a'],
            ['s','v','f','n'],
            ['t','e','e','' ]
        ]

def arr_adder(arr):
    sentence = []
    for x in range(len(arr[0])):
        for y in range(len(arr)):
            sentence.append(arr[y][x])
        sentence.append(' ')
    s = ''.join(sentence)
    
    return s.strip(' ')

print(arr_adder(arr))

''' Второй вариант.
Если надо проитерировать по нескольким спискам одинаковой
длины сразу, то используй функцию ZIP'''
def arr_adder(arr):
    return ' '.join(map(''.join, zip(*arr)))
