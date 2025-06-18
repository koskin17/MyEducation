#for number in range(1, 101, 2):
#    print(number)

#for i in range(100):
#    if i % 2 == 0:
#        continue
#    print(i, end=' ')

from random import randint
l = [randint(0,100) for _ in range (100)]
for i in range(len(l)):
    if l[i] % 2:
        isc = True
        position = i
        break
print(f"c o n {isc}{position=}")