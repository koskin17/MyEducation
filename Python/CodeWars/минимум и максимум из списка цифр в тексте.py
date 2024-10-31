numbers = '1 2 3 4 5'

def high_and_low(numbers):
    minimal = str(min(map(int, numbers.split())))
    maximum = str(max(map(int, numbers.split())))
    sp = [maximum, minimal]
    return ' '.join(sp)

print(high_and_low(numbers))


''' Второй вариант '''
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
