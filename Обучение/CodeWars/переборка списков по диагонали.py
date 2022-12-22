arr =   [['M', 'U', 'B', 'B', 'J', 'L', 'V', 'U', 'P', 'G', 'W', 'Z', 'Y', 'B', 'Z', 'S', 'M', 'U', 'Y', 'N', 'Q', 'H'],
         ['Z', 'A', 'L', 'V', 'J', 'H', 'N', 'I', 'X', 'N', 'C', 'S', 'N', 'H', 'Y', 'L', 'C', 'H', 'B', 'C', 'O', 'E'],
         ['T', 'B', 'R', 'J', 'U', 'Y', 'F', 'Y', 'K', 'A', 'M', 'F', 'I', 'T', 'B', 'A', 'Y', 'Q', 'I', 'G', 'F', 'C'],
         ['O', 'Z', 'B', 'H', 'S', 'H', 'D', 'A', 'M', 'C', 'N', 'G', 'Z', 'S', 'K', 'N', 'M', 'Q', 'N', 'L', 'T', 'R'],
         ['K', 'R', 'U', 'Z', 'K', 'F', 'G', 'C', 'N', 'D', 'F', 'I', 'R', 'R', 'H', 'G', 'H', 'P', 'S', 'L', 'W', 'L'],
         ['H', 'X', 'Q', 'V', 'N', 'H', 'B', 'B', 'H', 'W', 'T', 'B', 'V', 'H', 'S', 'A', 'F', 'D', 'F', 'I', 'E', 'I'],
         ['D', 'T', 'J', 'A', 'K', 'K', 'P', 'R', 'F', 'T', 'V', 'V', 'R', 'G', 'V', 'T', 'D', 'B', 'M', 'W', 'K', 'A'],
         ['S', 'I', 'O', 'M', 'W', 'K', 'S', 'S', 'S', 'Y', 'X', 'X', 'W', 'E', 'X', 'I', 'F', 'E', 'E', 'R', 'N', 'U'],
         ['Y', 'Y', 'Z', 'I', 'W', 'P', 'K', 'A', 'V', 'K', 'J', 'Z', 'O', 'R', 'Z', 'Y', 'K', 'Z', 'I', 'D', 'U', 'W'],
         ['S', 'V', 'R', 'K', 'W', 'Y', 'R', 'X', 'W', 'T', 'S', 'Q', 'E', 'C', 'O', 'F', 'Z', 'B', 'H', 'J', 'Y', 'G'],
         ['A', 'V', 'H', 'B', 'S', 'B', 'A', 'O', 'F', 'Z', 'D', 'G', 'E', 'L', 'M', 'C', 'S', 'H', 'X', 'G', 'H', 'U'],
         ['U', 'Q', 'P', 'K', 'U', 'I', 'D', 'I', 'A', 'T', 'H', 'I', 'M', 'F', 'L', 'J', 'I', 'K', 'I', 'S', 'B', 'T'],
         ['N', 'N', 'U', 'A', 'F', 'M', 'T', 'X', 'Y', 'W', 'O', 'I', 'C', 'N', 'T', 'M', 'O', 'Y', 'F', 'Y', 'S', 'K'],
         ['W', 'X', 'D', 'C', 'A', 'O', 'T', 'V', 'F', 'V', 'K', 'L', 'B', 'P', 'Y', 'S', 'W', 'I', 'D', 'X', 'V', 'Q'],
         ['B', 'L', 'D', 'I', 'G', 'R', 'R', 'F', 'B', 'I', 'U', 'E', 'Z', 'E', 'A', 'H', 'R', 'G', 'T', 'B', 'G', 'E'],
         ['E', 'X', 'I', 'Z', 'H', 'P', 'U', 'E', 'U', 'C', 'R', 'A', 'V', 'W', 'X', 'O', 'R', 'S', 'I', 'S', 'K', 'V'],
         ['I', 'C', 'C', 'X', 'D', 'P', 'E', 'W', 'B', 'A', 'X', 'H', 'N', 'J', 'L', 'X', 'D', 'F', 'M', 'K', 'T', 'C'],
         ['M', 'K', 'Y', 'G', 'L', 'X', 'Z', 'F', 'Q', 'J', 'S', 'H', 'U', 'N', 'R', 'Q', 'E', 'X', 'K', 'N', 'Q', 'I'],
         ['Z', 'C', 'N', 'R', 'Z', 'X', 'D', 'I', 'S', 'L', 'V', 'D', 'F', 'Q', 'Z', 'P', 'Q', 'T', 'Y', 'J', 'J', 'I'],
         ['P', 'L', 'O', 'Q', 'A', 'V', 'T', 'J', 'Q', 'U', 'Q', 'X', 'J', 'I', 'H', 'W', 'D', 'W', 'Q', 'U', 'N', 'D'],
         ['Q', 'H', 'B', 'M', 'F', 'R', 'I', 'K', 'G', 'C', 'W', 'G', 'Z', 'T', 'R', 'L', 'Z', 'A', 'Z', 'R', 'F', 'G'],
         ['C', 'J', 'A', 'L', 'Y', 'W', 'H', 'V', 'Z', 'O', 'N', 'M', 'T', 'N', 'R', 'B', 'E', 'H', 'N', 'W', 'M', 'C']]

def is_wristband(arr):
    if len(arr) == 1:
        return True

    for i in range(1, len(arr)):
        if len(arr[0]) != len(arr[i]):
            return False

    if type(arr) != list:
        return False

    
    if arr[0][0] == arr[0][1]:
        for x in range(len(arr)):                                   # проверка по горизонтали
            for y in range(1, len(arr[0])):
                if arr[x][0] == arr[x][y]:
                    continue
                else: return False
        return True

    if arr[0][0] == arr[1][0]:
        for x1 in range(len(arr[0])):                     # проверка по вертикали
            for y1 in range(1, len(arr)):
                if arr[0][x1] == arr[y1][x1]:
                    continue
                else: return False
        return True

    if arr[0][0] == arr[1][1]: 
        for x2 in range(len(arr)):           # проверка по диагонали слева направо, вниз
            for y2 in range(len(arr[0])):
                if y2 == len(arr[0])-1 or x2+1 == len(arr):
                    continue
                else:
                    if arr[x2][y2] == arr[x2+1][y2+1]:
                        continue
                    else: return False
        return True

    if arr[0][len(arr[0])-1] == arr[1][len(arr[1])-2]:
        for x3 in range(len(arr)):           # проверка по диагонали справа налево, вниз
            for y3 in range(len(arr[0])-1, 0, -1):
                if y3-1 < 0 or x3+1 > len(arr)-1:
                    continue
                else:
                    if arr[x3][y3] == arr[x3+1][y3-1]:
                        continue
                    else:
                        return False
        return True

    return False
            

print(is_wristband(arr))
