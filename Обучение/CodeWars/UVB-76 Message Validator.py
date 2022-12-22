'''
MDZHB 01 213 SKIF 38 87 23 95

or:

MDZHB 80 516 GANOMATIT 21 23 86 25

Message format consists of following parts:

Initial keyword "MDZHB";
Two groups of digits, 2 digits in first and 3 in second ones;
Some keyword of arbitrary length consisting only of uppercase letters;
Final 4 groups of digits with 2 digits in each group.
Your task is to write a function that can validate the correct UVB-76 message. Function should return "True" if message is in correct format and "False" otherwise.
'''

message = 'MDZHB 80 516 GANOMATIT 21 23 86 25'

def validate(message):
    if message == '':
        return False
    message = message.split(' ')
    if len(message) < 8:
        return False
    for i in range(len(message)):
        if message[0] != 'MDZHB':
            return False
        if message[1].isdigit() == False or len(message[1]) !=2 or message[2].isdigit() == False or len(message[2]) != 3:
            return False
        if message[3].isalpha() == False or message[3].isupper() == False:
            return False
        for y in message[4:len(message)]:
            if y.isdigit() == False or len(y) != 2:
                return False
    return True    

print(validate(message))

''' Второй вариант.
В нём вся проверка выполняется при помощи регулярных выражений'''
import re
validate = lambda msg: bool(re.match('^MDZHB \d\d \d\d\d [A-Z]+ \d\d \d\d \d\d \d\d$', msg))
