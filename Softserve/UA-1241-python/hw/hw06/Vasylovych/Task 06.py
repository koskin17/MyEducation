r = range(1,10)

e=[]
o=[]
n=[]

for a in r:
    if a%2 ==0:
        e.append(a)
    elif a%3 ==0:
        o.append(a)
    if a%2 !=0 and a%3 !=0:
        n.append (a)
print(e)            
print(o)
print(n)