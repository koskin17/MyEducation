a=input("Enter a four-digit number: ",)
if len(a) !=4  :
    print("You entered an incorrect number!")
else:
    print("Sum of digits in number:",int(a[0])+int(a[1])+int(a[2])+int(a[3]))
    print("Number in reverse order: ",int(a[3]),int(a[2]),int(a[1]),int(a[0]),sep="")
    print("Numbers in ascending order:",sorted(a))

