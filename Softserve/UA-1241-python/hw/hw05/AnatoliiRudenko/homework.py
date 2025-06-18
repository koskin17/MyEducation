l=[1,2,3,4,5]
for i in l:
    i=float(i)
    print(i)


number=input("Enter number: ")
number=int(number)
first=0
second=1
for i in range(1,number+1):
    print(first)
    next_number=first+second
    first=second
    second=next_number

number2=input("Enter number: ")
number2=int(number2)

product=1
if number==0:
    print(product)
else:
    for i in range(1,number2+1):
        product=product*i
    print(product)
