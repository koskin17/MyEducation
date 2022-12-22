text1 = list(input('Введите первый текст: '))
text2 = list(input('Введите второй текст: '))
total = []
d = max(len(text1), len(text2))
'''
Первый вариант соединения строк по каждой букве
'''
for i in range(0, d):
        try:
            total.append(text1[i])
        except:
            total.append('')
        try:
            total.append(text2[i])
        except:
            total.append('')

print(total)
total2 = []
for i in range(0, len(total)):
        if total[i] == ' ':
                continue
        total2.append(total[i])

print(total2)
print(''.join(total2))
'''
##Второй вариант соединения строк по каждой букве
##'''
total3 = []
if len(text1) > len(text2):
        dif = ' ' * (len(text1) - len(text2))
        text2.extend(dif)
elif len(text2) > len(text1):
        dif = ' ' * (len(text2) - len(text1))
        text1.extend(dif)
for i in range(0, d):
        total3.append(text1[i])
        total3.append(text2[i])
print(total3)
total4 = []
for i in range(0, len(total3)):
        if total3[i] == ' ':
                continue
        total4.append(total[i])

print(total4)
print(''.join(total4))
