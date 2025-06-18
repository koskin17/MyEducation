even=[]
odd=[]
notdivby2and3=[]
for i in range(1,11):
    if i%2==0:
        even.append(i)
    elif i%2==1 and i%3==0:
        odd.append(i)
    elif i%2==1 and not i%3==0:
        notdivby2and3.append(i)
for i in even:
    print("Even: ", i)
for i in odd:
    print("Odd: ", i)
for i in notdivby2and3:
    print("notdivby2and3: ", i)


i=""
while not i=="q":
    i=input("Enter login: ")
    if i=="First":
        print("Correct login")
        break
    else:
        print("Error")
