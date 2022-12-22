'''
Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
'''

n = 12
x = 2
y = 6

def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else: return False

print(is_divisible(n,x,y))
