import random       # для использования модуля random далее
import os

''' Для начала заполняем файлы, чтобы не делать это вручуню '''
''' При открытии файла методом with ... as после окончания работы с ним не требуется метод close для его закрытия'''

with open('spisok1.txt', 'w+', encoding='utf-8') as f1: # если файл не существует, то он заново создаётся в текущей папке
    for i in range(1, 20):
        string1 = 'Человек ' + str(i) + '\n'
        f1.write(string1)

number_for_list2 = list(range(1, 22))       # формируем список номеров для второго списка и для его последующего перемешивания
                                            # до 22 сделано специально, чтобы кол-во номеров совпало с кол-вом строк в списке2
random.shuffle(number_for_list2)            # после перемешивания новый перемешанный список записывается в туже переменную

with open('spisok2.txt', 'w+', encoding='utf-8') as f2: # если файл не существует, то он заново создаётся в текущей папке
    for i in range(1, 20):
        string2 = ' получает данные для Человека ' + str(number_for_list2[i]) + '\n'
        f2.write(string2)

''' Теперь создаём / открываем третий файл и записываем в него соединённые из двух файлов строки
Берём строки из файла 1, сопоставляем со стоками в файле 2 и записываем в файл 3'''

with open('spisok1.txt', 'r+', encoding='utf-8') as f1:
    for line1 in range(1, 20):                                      # кол-во повторений цикла равно кол-ву строк в первом файле  
        line_sp1 = f1.readline()                                    # считываем первую строк из файла1
        pos_probel1 = line_sp1.rfind(' ')                           # определяем позицию пробела в строке от правого конца
        number_spisok1 = line_sp1[pos_probel1:len(line_sp1):]       # считываем весь номер с позиции пробела до конца строки
        number_spisok1 = number_spisok1.strip()                     # обрезаем пробелы от номера, чтобы получить чистое число
        with open('spisok2.txt', 'r+', encoding='utf-8') as f2:                 # открываем второй файл на чтение
            for line2 in range(1, 20):                                  # запускаем цикл перебора строк второго файла по кол-ву строк в нём
                line_sp2 = f2.readline()                                    # считываем строку из второго файла
                pos_probel2 = line_sp2.rfind(' ')                       # определяем позицию пробела в строке от правого конца во втором файле
                number_spisok2 = line_sp2[pos_probel2:len(line_sp2):]       # считываем весь номер из второго файла с позиции пробела до конца строки
                number_spisok2 = number_spisok2.strip()                 # обрезаем пробелы от номера из второго файла, чтобы получить чистое число
                if number_spisok1 == number_spisok2:                    # проверяем, равен ли номер из списка 1 номеру из списка 2
                    with open('general.txt', 'a+', encoding='utf-8') as f3:             # открываем третий файл
                        general_string = line_sp1.strip() + line_sp2
                        f3.write(general_string)
                        print(general_string)

os.startfile(r'general.txt')
