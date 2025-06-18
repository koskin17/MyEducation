import random
a=input("Input len list:")
if a.isdigit:
    a=int(a)
    list = [random.randint(1, 100) for _ in range(a)]
    print(list)
for i in range(len(list)):
    list[i]=float(list[i])
print(list)

