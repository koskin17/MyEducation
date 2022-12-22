'''
Задача - проверить введенное время и вернуть правильное время в правильном формате
'''



def time_correct(t):
    if not t: return t
    try:
        h, m, s = map(int, t.split(':'))
        if s >= 60: s -= 60; m += 1
        if m >= 60: m -= 60; h += 1
        return '%02d:%02d:%02d' % (h % 24, m, s)
    except: pass

print(time_correct(t))
