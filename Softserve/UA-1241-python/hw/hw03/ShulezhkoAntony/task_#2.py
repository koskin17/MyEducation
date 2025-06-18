#2.1
import random
number = random.randrange(1000, 10000)
print(F"Your number is: {number}\n")
sumarize = [int(digit) for digit in str(number)]
print(sum(sumarize))
#2.2
print("".join(reversed(str(number))))
#2.3
print("".join(sorted(str(number))))

