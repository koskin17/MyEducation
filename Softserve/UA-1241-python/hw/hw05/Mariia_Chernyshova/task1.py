l = [5,6,7,8,9,4,85,44,7,15,77]
for i in range(len(l)):
    a=float(l.pop(i))
    l.insert(i,a)
print(l)
