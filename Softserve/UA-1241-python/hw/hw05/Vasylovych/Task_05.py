#Change from int to float

number = [100,101,102,103,104,105]
    
for x in number :
    
    x= float(x)
    print((x),type(x))

#Print Fibonacci numbers
n = int(input("Enter number:"))
a, b = 0, 1
mylist = []
while a <= n:
    mylist.append(a)
    a, b = b, a+b

print("Fibonacci number", mylist)

#calculate the factorial of the entered/number without using recursion.
n=int(input("Enter number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of the number is: ")
print(fact)