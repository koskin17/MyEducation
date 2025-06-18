number=int(input("Enter factorial number"))
if number>0:
    a=1
    while a<=number:
        a=a*(a+1)
    print("Factorial", a)
else:
    print("0")