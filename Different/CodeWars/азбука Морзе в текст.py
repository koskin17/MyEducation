'''
Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will be strings.

Characters should be separated by a single space. Words should be separated by a triple space.

For example, "HELLO WORLD" should return -> ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
'''
morse_code = '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '

def decode_morse(morse_code):
    new_string = []
    morse = {'...---...':'SOS', '...---...!':'SOS!',
'.-':'A',
'-...':'B',
'-.-.':'C',
'-..':'D',
'.':'E',
'..-.':'F',
'--.':'G',
'....':'H',
'..':'I',
'.---':'J',
'-.-':'K',
'.-..':'L',
'--':'M',
'-.':'N',
'---':'O',
'.--.':'P',
'--.-':'Q',
'.-.':'R',
'...':'S',
'-':'T',
'..-':'U',
'...-':'V',
'.--':'W',
'-..-':'X',
'-.--':'Y',
'--..':'Z',
'-----':'0',
'.----':'1',
'..---':'2',
'...--':'3',
'....-':'4',
'.....':'5',
'-....':'6',
'--...':'7',
'---..':'8',
'----.':'9',
'   ':' ',
'.-.-.-':'.',
'−−··−−':'!'}
    morse_code = morse_code.strip(' ')
    morse_code = morse_code.split(' ')

    for i in range(len(morse_code)):
        if morse_code[i] == '' and morse_code[i+1] == '':
            new_string.append(' ')
        else:
            new_string.append(morse.get(morse_code[i]))

    for item in new_string:
        if item == None:
            new_string.remove(item)

    for item in new_string:
        if item == None:
            new_string.remove(item)


    return ''.join(new_string)


print(decode_morse(morse_code))
