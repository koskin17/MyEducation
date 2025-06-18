# Task1. Create a list that contains elements of integer type, then use 
# the loop to change the type of these elements to a floating type. 
# (Hint: use the built-in float () function).

list = list(range(5, 25))
print(list)


for i in range(len(list)):
    list[i] = float(list[i])