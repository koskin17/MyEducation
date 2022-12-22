'''
Задача - создать архив из папки folder, который будет лежать
в самой папке folder
'''

import zipfile
import os

folder_path = 'E:\\Python\\MyPython\\Программы\\Дерево каталога\\folder' # путь к папке, которую мы будем упаковывать
zip_path = 'E:\\Python\\MyPython\\Программы\\Дерево каталога\\adhive_folder.zip' # путь к архиву, который создаётся
zip_name = 'test.zip' # отдельно хранится имя архива

my_zip = zipfile.ZipFile(zip_path, 'w')
'''
При открытии / запуске файла архива его РЕКОМЕНДУЕТСЯ СРАЗУ ЗАКРЫТЬ.
По умолчанию у модуля ZipFile метод сжатия - ZIP_STORED, который
не сжимает файлы, а просто их упаковывает в архив zip.
Рекомендуется использовать метод ZIP_DEFLATED, который стандартно сжимает.
'''

'''
Для записи его-либо в архив используется метод write
'''
##my_zip.write('E:\\Python\\MyPython\\Программы\\Дерево каталога\\folder\\test_1.txt', compress_type = zipfile.ZIP_DEFLATED, arcname = 'test_1.txt')
'''
В этом случае файл архива создаётся, но сохраняется и весь путь к нему по папкам.
Т.е. сохраняются вложенные папки в архив.
Чтобы архивировать только сам файл, без дублирования вложенности папок,
метод write поддерживает параметр arcname, в который нужно указать имя,
под которым мы хотим положить файл в архив.
'''
'''
Также имя, под которым мы хотим упаковать файл в архив, можно указать сразу после пути
'''
##my_zip.write('E:\\Python\\MyPython\\Программы\\Дерево каталога\\folder\\test_1.txt', 'new.txt', compress_type = zipfile.ZIP_DEFLATED)
'''
В этом случае в файл архива добавился новый файл под именем new.txt
'''

'''
Упаковка целого каталога с его содержимым
'''

for folder, subfolders, files in os.walk(folder_path):
    for file in files:
        if file == zip_name:
            continue
        
        print(os.path.join(folder, file))
        '''
        Функция os.path.join объединяет путь и имя файла, который лежит по этому пути.
        В результате print показывает все файлы вместе с полным путём к каждому
        '''
        print(os.path.relpath(os.path.join(folder, file), folder_path))
        '''
        Метод os.path.relpath удаляет из пути то, что нужно.
        В данном случае он удаляет содержимое переменной folder_path, в которой лежит полный путь к подпапке и файлу относительно корня диска С
        '''
        my_zip.write(os.path.join(folder, file),
                     os.path.relpath(os.path.join(folder, file), folder_path),
                     compress_type = zipfile.ZIP_DEFLATED)

print('Архив создан')

my_zip.close()
