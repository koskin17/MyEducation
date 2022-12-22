a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    else:
        dif = 0
        for word1 in a1:
            for word2 in a2:
                if abs(len(word1) - len(word2)) > dif:
                    dif = abs(len(word1) - len(word2))
    return dif

print(mxdiflg(a1, a2))


''' Второй вариант '''
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1
