shoes = [[0, 23], [1, 21], [1, 23], [0, 21], [1, 22], [0, 22]]

def pair_of_shoes(shoes):
    if len(shoes) % 2 != 0:
        return False
    else:
        shoes.sort()
        for i in range(int(len(shoes) / 2)):
            para = [abs(shoes[i][0]-1), shoes[i][1]]
            if para != shoes[i+int(len(shoes) / 2)]:
                return False
    return True

print(pair_of_shoes(shoes))

''' Второй вариант '''
def pair_of_shoes(shoes):
    right = sorted([j for i, j in shoes if i == 0])
    left = sorted([j for i , j in shoes if i == 1])
    return right == left
