#=============================
def line():
    print("=========================")
#=====Creating four-digit number======================
while True:
    user_input_number = input("Write number netween 1000 and 9000: ")
    
    try:
        if int(user_input_number) < 1000 or int(user_input_number) > 9999:
            print("Try again...")
        elif int(user_input_number) >= 1000 or int(user_input_number) <= 9999:
            break        
    except :
        print("Incorrect input(((\nTry again")
    
#=====Sum of the four-digit number====================
sum_number = 0

for x in str(user_input_number):
    sum_number += int(x)    
    
print(f"Sum of number {user_input_number}: {sum_number}")

line()
#=====Showing the four-digit number in reverse order=====
reserve_mode = int(str(user_input_number)[::-1])

print(reserve_mode)

line()
#=====Sorting the four-digit number in ASC order=========
number_list = list(str(user_input_number))

number_list.sort()

print(number_list)

line()
#=============================
