n = "!Hiiiiii! Hhhh! Gggg!!!"


def remove(n):
        tmp = []
        n = n.split()
        
        for word in n:
                if word[-1] != '!':
                        tmp.append(word)
                else:
                        for i in range(len(word)-1, 0, -1):
                                if word[i].isalpha():
                                        print(word[:i+1])
                                        tmp.append(word[:i+1])
                                        break
        return ' '.join(tmp)
                
                

print(remove(n))

''' Второй вариант '''

def remove(n):
        tmp = []
        n = n.split()
        for word in n
                tmp.append(word.rstrip('!'))
        return ' '.join(tmp)              

print(remove(n))
