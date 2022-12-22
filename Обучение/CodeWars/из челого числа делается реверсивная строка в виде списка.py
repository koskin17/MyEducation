''' Given a random non-negative number, you have to return the digits of this number within an array in reverse order.'''

n = 348597

def digitize(n):
    x = [int(a) for a in str(n)]
    x.reverse()
    return x

print(digitize(n))

''' Второй способ '''
def digitize(n):
    return map(int, str(n)[::-1])
