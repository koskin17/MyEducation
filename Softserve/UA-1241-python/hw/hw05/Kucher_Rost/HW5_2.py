def fin(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

#блок виклику def        
len = int(input('Яка довжина? '))
print(list(fin(len)))