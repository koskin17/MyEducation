''' Необходимо у полученного номера скрыть все цифры, кроме последних четырех'''
cc = 'Skippy'

def maskify(cc):
    lenght = len(cc)
    if lenght <= 4:
        return cc
    else:
        hid = str('#'*(len(cc)-4)) + str(cc[len(cc)-4:])
    return hid

print(maskify(cc))
