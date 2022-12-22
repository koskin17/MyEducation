'''
Description
We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
'''

s = "1234"

def string_to_number(s):
    s = int(s)
    return s

print(string_to_number(s))

''' Второй вариант '''
def string_to_number(s):
    return int(s)

print(string_to_number(s))
