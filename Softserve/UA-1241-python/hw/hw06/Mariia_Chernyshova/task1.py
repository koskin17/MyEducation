c1,c2,c3=[],[],[]
for i in range(1,11):
    if i%2==0:
        c1.append(i)
    if i%3==0:
        c2.append(i)
    if i%2==0 and i%3==0:
        c3.append(i)
print(c1,c2,c3)
