a = 0
def func():
    global a
    for num in [2, 4, 8]:
        a += 1
        yield num * 0.5
        
array = []
for val in func():
    array.append(int(a == val))
print(sum(array))
