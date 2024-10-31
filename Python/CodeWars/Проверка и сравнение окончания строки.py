''' Проверка и сравнение окончания строки '''

string = 'abc'
ending = 'bc'


def solution(string, ending):
    if string[-len(ending):] == ending:
        return True
    if ending == '':
        return True
    return False

print(solution(string, ending))

''' Второй вариант '''
def solution(string, ending):
    return string.endswith(ending)
