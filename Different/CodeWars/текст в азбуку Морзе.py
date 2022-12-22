'''
Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will be strings.

Characters should be separated by a single space. Words should be separated by a triple space.

For example, "HELLO WORLD" should return -> ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
'''
string = 'HEY JUDE'

def encryption(string):
    new_string = ''
    morse_dict = {
'A':'. −',
'B':'− . . . ',
'C':'− . − . ',
'D':'− . . ',
'E':'. ',
'F':'. . − . ',
'G':'− − . ',
'H':'. . . . ',
'I':'. . ',
'J':'. − − − ',
'K':'− . − ',
'L':'. − . . ',
'M':'− − ',
'N':'− . ',
'O':'− − − ',
'P':'. − − . ',
'Q':'− − . − ',
'R':'. − . ',
'S':'. . . ',
'T':'− ',
'U':'. . − ',
'V':'. . . − ',
'W':'. − − ',
'X':'− . . − ',
'Y':'− . − − ',
'Z':'− − . . ',
'0':'− − − − − ',
'1':'. − − − − ',
'2':'. . − − − ',
'3':'. . . − − ',
'4':'. . . . − ',
'5':'. . . . . ',
'6':'− . . . . ',
'7':'− − . . . ',
'8':'− − − . . ',
'9':'− − − − . ',
' ':'   '}
    for letter in string:
        new_string += str(morse_dict.get(letter)) + ' '
    return new_string

print(encryption(string))
