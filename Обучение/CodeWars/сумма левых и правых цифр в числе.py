arr = [9,2,8,7,5,4,0,6]

def min_sum(arr):
    arr = sorted(arr)
    summ = 0
    s1 = arr[:int(len(arr)/2)]
    s2 = sorted(arr, reverse = True)[:int(len(arr)/2)]    
    for i in range(len(s1)):
        summ += s1[i] * s2[i]
    
    return summ

print(min_sum(arr))

''' Второй вариант.
В нём также сортируется список по возрастанию.
А потом крайний слева элемент умножается на крайний справа методом -i-1
сколько раз,сколько равна половина списка,т.е. до его середины'''

def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))
