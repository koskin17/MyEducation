def facktor(num):
    fact = 1
    if num < 0:
        print("не для мінусів")
    elif num == 0:
        print("від 0 то буде 1")
    else:  
        for i in range(1, n+1):
            fact = fact * i
        print("Факторіал ",num,"is ",fact)                   
    return 'Заглушка'    
n = int(input('Яка довжина? '))
print(facktor(n))