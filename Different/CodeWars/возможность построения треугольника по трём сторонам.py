''' Даны три стороны треугольнка.
Необходимо определить, можно ли построить треугольник с
такими сторонами'''

a = 1
b = 2
c = 2


def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        cosalpha = (b**2 + c**2 - a**2) / (2*b*c)
        if -1 < cosalpha < 1:
            return True
        else: return False
    else: return False

print(is_triangle(a, b, c))

''' Второй способ.
Проверка по длине каждой стороны.
У треугольника каждая сторона должна быть меньше суммы двух
других сторон '''
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

print(is_triangle(a, b, c))
