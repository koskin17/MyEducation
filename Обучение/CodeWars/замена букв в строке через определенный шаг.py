text, n, old_value, new_value = "Vader said: No, I am your father!", 2, 'a', 'o'

def replace_nth(text, n, old_value, new_value):
   
    if n == 0 or n > text.count(old_value) or n < 0:    # Проверка списка на пустоту и на отрицательную позицию замены
        return text
    
    newstr = []                                         # создаём пустой список для разиения строки на буквы
    
    for i in range(len(text)):                          # разбиваем строку на буквы
            newstr.append(text[i])
    indexlist = []                                      # создаём список для записи индексов буквы для замены и далее записываем все индексы
    for i in range(len(newstr)):
        if newstr[i] == old_value:
            indexlist.append(i)

    for i in range(n-1, len(indexlist), n):             # создаём цикл с шагом замены и меняем в списке из букв первоначальной строки буквы через шаг
        print(indexlist[i])
        newstr[indexlist[i]] = new_value
    
    return ''.join(newstr)                              # собираем из списка строку

print(replace_nth(text, n, old_value, new_value))

''' Второй вариант '''
def replace_nth(text, n, old, new):
    count = 0                                           # создаётся счетчик повторений
    res = ""                                            # создаётся новая пустая строка
    for c in text:
        if c==old:                                      # если буква в строке равна старой под замену
            count+=1                                    # четчик увеличивается на 1
            if count ==n:                               # если счётчик уже равен шагу замены
                res+=new                                # в новую строку добавляется новая буква
                count=0                                 # и обнуляется счётчик
                continue                                # в противном случае пропускается итерация
        res+=c                                          # и в новую строку просто добавляется буква из старой строки
    return res                                          # возвращается новая собранная строка

print(replace_nth(text, n, old_value, new_value))
