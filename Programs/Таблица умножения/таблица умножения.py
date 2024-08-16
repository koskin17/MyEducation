import os         # импорт модуля os необходим для запуса стороннего файла методом startfile                                                                   

file = open("table.txt", "w")   # encoding='utf-8'
# если не указывать кодировку, то файл TXT запишется на русском нормально

for col in range(1, 11):
    if col > 1:
        col_write = '\n' + 'Умножение на ' + str(col) + '\n'*2
    else:
        col_write = 'Умножение на ' + str(col) + '\n'*2
    file.write(col_write)
    for row in range(1, 11):
        x = str(col) + ' Х ' + str(row) + ' = ' + str(col * row) + '\n'
        file.write(x)
file.close()

os.startfile(r'C:\Users\LeaBlankez\Desktop\MyPython\Программы\Таблица умножения\table.txt') # в этой строке запускается созданный файл с таблицей умножения


'''Аналогичным образом можно создать файл Word в формате doc'''
file = open("table.doc", "w", encoding='utf-8')
# если указать кодировку, то при открытии файла Word он сразу будет стоять на кодироке UTF-8. Если не указывать, то придётся самому искать и выбирать кодировку
for col in range(1, 11):
    if col > 1:
        col_write = '\n' + 'Умножение на ' + str(col) + '\n'*2
    else:
        col_write = 'Умножение на ' + str(col) + '\n'*2
    file.write(col_write)
    for row in range(1, 11):
        x = str(col) + ' Х ' + str(row) + ' = ' + str(col * row) + '\n'
        file.write(x)
file.close()

os.startfile(r'C:\Users\LeaBlankez\Desktop\MyPython\Программы\Таблица умножения\table.doc') # в этой строке запускается созданный файл с таблицей умножения

'''Аналогичным образом можно создать файл Excel, НО В ФОРМАТЕ XLS. Более современный формат XLSX не поддерживается базовым Python и нужно подключать модули'''
'''Только кодировка в Excel-файле будет отличаться и НАДО РАЗОБРАТЬСЯ '''
file = open("table.xls", "w")
# если не указывать кодировку, то файл Excel запишется на русском нормально
for col in range(1, 11):
    if col > 1:
        col_write = '\n' + 'Умножение на ' + str(col) + '\n'*2
    else:
        col_write = 'Умножение на ' + str(col) + '\n'*2
    file.write(col_write)
    for row in range(1, 11):
        x = str(col) + ' Х ' + str(row) + ' = ' + str(col * row) + '\n'
        file.write(x)
file.close()

os.startfile(r'C:\Users\LeaBlankez\Desktop\MyPython\Программы\Таблица умножения\table.xls') # в этой строке запускается созданный файл с таблицей умножения
