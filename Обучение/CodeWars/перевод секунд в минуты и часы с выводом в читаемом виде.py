seconds = 0

def make_readable(seconds):
    if seconds == 0:
        return '00:00:00'
    h = seconds // 3600
    m = (seconds - (h * 3600)) // 60
    s = seconds - (h * 3600) - (m * 60)
    if len(str(h)) < 2:
        h = str(0) + str(h)
    if len(str(m)) < 2:
        m = str(0) + str(m)
    if len(str(s)) < 2:
        s = str(0) + str(s)
    return '{}:{}:{}'.format(h, m, s)

print(make_readable(seconds))

''' Второй вариант '''
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
