# Task 1
user_list = []
print("Enter the elements (they should be integers) of your list. If you would like to stop enterint, type 'e': ")
count = 1

while True:
    elem = input(f"№{count}: ")
    if elem == 'e':
        break 
    elif not elem.isdigit():
        print("Element is not a digit. Try again.")
        continue
    else:
        user_list.append(int(elem))
        count += 1

for item in user_list:
    item = float(item)

print(user_list)

# Task 2
n = int(input("Enter n: "))

if n < 1:
    print("Invalid value.")
else: 
    num1 = 0
    num2 = 1
    
    while num2 <= n:
        print(num1)
        num1, num2 = num2, num1+num2

# Task 3
num = int(input("Enter the number, factorial of which you would like to get: "))
factorial = 1

for i in range(2, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")

