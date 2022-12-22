text = 'The sunset sets at twelve o\'clock.'

def alphabet_position(text):
    alphabet = ['a',	'b',	'c',	'd',	'e',	'f',	'g',	'h',	'i',	'j',	'k',
                'l',	'm',	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',	'x',	'y',	'z']
    alphabet2 = ['A',	'B',	'C',	'D',	'E',	'F',	'G',	'H',	'I',	'J',	'K',
                 'L',	'M',	'N',	'O',	'P',	'Q',	'R',	'S',	'T',	'U',	'V',	'W',	'X',	'Y',	'Z']
    new_text = []
    for letter in text:
        if letter in alphabet:
            l2 = alphabet.index(letter)+1
        elif letter in alphabet2:
            l2 = alphabet2.index(letter)+1
        else: continue
        new_text.append(l2)
    return (" ".join(map(str,new_text)))                        # функция map позволяет применить полученную функцию в качестве первого параметра
                                                                # в данном случае это функция str
                                                                # к каждому элементу итерации. В данном случае это каждый элемент списка new_text
                                                                # т.е. каждый элемент списка преобразуется в строку
                                                                # после этого весь список со строчными элементами преобразуется в строку и выводится

print(alphabet_position(text))
print(type(alphabet_position(text)))

''' Второй вариант '''
def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())  # в этом случае код:
                                                                            # text.lower() переводит все буквы строки в нижний регистр, что использовать один словарь символов,
                                                                            # без символов в ВЕРХНЕМ регистре
                                                                            # для каждой буквы строки уже в нижнем регистре проверяется функцией .isalpha является ли она буквой
                                                                            # если является, то для этого символа запускается функция ord.
                                                                            # функция ord возвращает код символа по системе Юникод
                                                                            # из полученного кода по Юникод вычитается 96 потому-что у английской буквы "а" код 97,
                                                                            # т.е. при вычитании 96 получается 1, что соответствует 1-ой позиции буквы в алфавите

print(alphabet_position2(text))
print(type(alphabet_position2(text)))

''' Еще один вариант. Похож на мой, но лучше и проще '''

alphabet3 = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position3(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet3.index(letter) + 1)
        return result.lstrip(' ')

print(alphabet_position3(text))
print(type(alphabet_position3(text)))
