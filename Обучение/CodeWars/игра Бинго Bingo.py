card = [
  ['B', 'I', 'N', 'G', 'O'],
  [1,   16,   31, 46,   61],
  [3,   18,   33, 48,   63],
  [5,   20, 'FREE SPACE', 50, 65],
  [7,   22,   37, 52,   67],
  [9,   24,   39, 54,   69]
]

numbers = ['B5', 'I20', 'G50', 'O65']


def bingo(card, numbers):
    cards = []

    for i in range(1, 6):                           # ''' Формируем выиграшные комбинации по вертикали '''
        tmp= []
        for x, y in zip(card[0], card[i]):
            if y == 'FREE SPACE':
                tmp.append('FREE SPACE')
            else:
                tmp.append(str(x) + str(y))
        cards.append(tmp)
        
    for x in range(len(card[0])):                   # ''' Формируем выиграшные комбинации по горизонтали '''
        tmp = []
        for y in range(1, len(card)):
            if card[y][x] == 'FREE SPACE':
                tmp.append('FREE SPACE')
            else:
                tmp.append(str(card[0][x]) + str(card[y][x]))

        cards.append(tmp)

    x = 0
    y = 0
    tmp = []
    for i in range(5):                                      # ''' Формируем выиграшную комбинацию по диагонали из левого верхнего угла вниз '''
        if card[x+1][y] == 'FREE SPACE':
            tmp.append('FREE SPACE')
        else:
            tmp.append(str(card[0][y]) + str(card[x+1][y]))
        x += 1
        y += 1
    cards.append(tmp)

    x = 6
    y = 0
    tmp = []
    for i in range(5):                                      # ''' Формируем выиграшную комбинацию по диагонали из левого нижнего угла вверх '''
        if card[x-1][y] == 'FREE SPACE':
            tmp.append('FREE SPACE')
        else:
            tmp.append(str(card[0][y]) + str(card[x-1][y]))
        x -= 1
        y += 1
    cards.append(tmp)

    tmp = []
    for i in range(1, 6):                                   # ''' Формируем выиграшную комбинацию из всех номером на поле '''
        for y in range(len(card[0])):
            if card[i][y] == 'FREE SPACE':
                tmp.append('FREE SPACE')
            else:
                tmp.append(str(card[0][y]) + str(card[i][y]))
    cards.append(tmp)

    if len(numbers) < 4:
        return False
    if 4 <= len(numbers) < 25:
        for x in range(len(cards)-1):
            count = 0
            for y in range(len(cards[x])):
                if cards[x][y] in numbers:
                    count += 1
                    if count == 5:
                        return True
                    elif count == 4 and 'FREE SPACE' in cards[x]:
                            return True
                    else: continue
    if 25 <= len(numbers):
        if all(cards[13][x] in numbers for x in range(len(cards[13]))):
            return True
    return False

print(bingo(card, numbers))
