# Create a list that contains elements of integer type, then use
# the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).
list_conteiner = [1.1,2,3,4]
for i in range(len(list_conteiner)):
    list_conteiner[i] = float(list_conteiner[i])
print(list_conteiner)    