#Task1
#Create a list that contains elements of integer type, then use
#the loop to change the type of these elements to a floating type.
#(Hint: use the built-in float () function).

list_number = [1, 2, 3]  

float_list = []
for int in list_number:
 float_list.append(float(int))

print(float_list)