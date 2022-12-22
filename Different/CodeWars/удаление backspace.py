import re

s = '[backspace]*3a  [backspace]'

def solve(s):
    tmp = []
    N = '[backspace]'
    M = r'[backspace]*'
##    s = s.replace('.backspace.*', 'M')
    s = re.sub('.backspace.', 'N', s)
    print(s)
    s = re.sub('N.', 'M', s)
    print(s)

    for letter in s:
        if letter == 'N':
            if len(tmp) != 0:
                    tmp.pop()
                    continue
        if letter == 'M':
            for i in range(int(s[s.index(letter)+1])):
                if len(tmp) != 0:
                    tmp.pop()
                else:
                    continue
        
        else:
            tmp.append(letter)
                
    return ''.join(tmp)

print(solve(s))
