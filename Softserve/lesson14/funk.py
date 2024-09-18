import math


def cout_chen(a):
    char_cout ={}

    for b in a:
        if b in char_cout:
            char_cout[b] += 1
        else:
            char_cout[b] =1
    return char_cout




# r = cout_chen("hello")
# print(r)


def quadratic_expression(a, b, c):



    d = b**2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        if x1 < x2:
            return x1, x2
        else:
            return x2, x1