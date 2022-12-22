'''
Нужно прочитать каждую строку файла и из строк создать список
'''
##import os
##
##''' Сначала создаём файл, обращаясь к нему методов "w+", который позволяет создать файл, если его нет '''
##file = open('data_list.txt', 'w+')
##
##'''
##Теперь наполняем файл сами, чтобы не писать всё вручную в файле
##'''
##
##for i in range(1, 16):
##    if i == 15:
##        string = 'Человек ' + str(i)
##    else:
##        string = 'Человек ' + str(i) + '\n'
##    file.write(string)
##file.close()
##
##os.startfile(r'C:\Users\LeaBlankez\Desktop\MyPython\Программы\Список из строк файла\data_list.txt')
'''
Файл с данным создали и верхний код можно закоментировать
'''
'''
Задача - из строк файла создать список
'''
file = open('data_list.txt', 'r+')
##print(sum(1 for line in open('data_list.txt', 'r')))  # данной строкой можно посчитать число строк в файле
line_list = []
for line in file:
    string = line.strip('\n')
    line_list.append(string)

print(line_list)
    

