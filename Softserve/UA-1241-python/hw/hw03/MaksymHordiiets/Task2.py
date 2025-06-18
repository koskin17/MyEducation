#Task 2.1
import random
number = random.randrange(1000,10000)
print(F"Your number is: {number}\n")

digits = [int(digit) for digit in str(number)]
print(sum(digits))

#Task 2.2
print(''.join(reversed(str(digits))))

#Task 2.3
print(sorted(digits))