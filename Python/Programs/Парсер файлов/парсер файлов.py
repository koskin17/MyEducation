import os

spisok = []

for address, directory, file in os.walk('E:\Python\MyPython'):   #эта функция позволяет сгенерировать все пути к файлам по указанному пути
    spisok.append(address)
    for file in file:
        full = os.path.join(address, file)
        if '.txt' in full:
            spisok.append(full)

print(spisok)
