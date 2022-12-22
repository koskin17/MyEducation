array = [1, 2, 3, 7, 5, 14, 7, 15, 9, 10]

def bingo(array):
    arr = ['B','I','N','G','O']
    word = []
    for letter in array:
        word.append(chr(letter+96))
    word = ''.join(word).upper()
    if all(letter in word for letter in arr):
        return "WIN"
    return "LOSE"

print(bingo(array))

''' Второй вариант.
В этом слйчае коды конкретных букв сразу проверяются на наличие в полученном списке '''
def bingo(array): 
    return "WIN" if {2, 7, 9, 14, 15}.issubset(set(array)) else "LOSE"
