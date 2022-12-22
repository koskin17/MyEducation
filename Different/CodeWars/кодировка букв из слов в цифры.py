word = 'heLlo'

def word_pattern(word):
     word = word.lower()
     dic = {}
     string = []
     index = 0
     for i in range(len(word)):
          if word[i] not in word[:i]:
               dic[word[i]] = index
               index += 1
     for i in word:
          string.append(str(dic.get(i)))

     return '.'.join(string)

print(word_pattern(word))

''' Второй вариант '''
def word_pattern(word):
    ret,  box, i = [], {}, 0
    for e in word.lower():
        if e not in box:
            box[e] = str(i)
            i+= 1
        ret.append(box[e])
    return '.'.join(ret)
