import random
number=str(random.randrange(1000,9999))
print(number)
print ("The product of the digits of this number:", int(number[0])+int(number[1])+int(number[2])+int(number[3]))
print ("The number in reverse order:", number[::-1])
print("The digits of the number sorted in ascending order:", sorted(number))
