import math

def test1(r1, r2):
    r1=3
    r2=2
    V2=(4 * math.pi * r1)/3-(4 * math.pi * r2)/3
    print(round(V2,2))

def test2(r1, r2):
    r1=3
    r2=2
    PI = 3.14
    result = (4 * PI * r1)/3 - (4 * PI * r2)/3
    print(round(result, 2))


r1 = 5
r2 = 10

test1(r1, r2)
test2(r1, r2)