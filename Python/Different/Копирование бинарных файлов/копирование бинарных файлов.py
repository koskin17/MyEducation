r = open('C:\\Users\\LeaBlankez\\Desktop\\MyPython\\копирование бинарных файлов\\Poedit-2.4.2-setup.exe', 'rb')
y = open('C:\\Users\\LeaBlankez\\Desktop\\MyPython\\копирование бинарных файлов\\Copy_Poedit-2.4.2-setup.exe', 'wb')

while True:
    var = r.read(1024*1024)
    print(var.__sizeof__())
    if var.__sizeof__() == 33:
        break

    y.write(var)

print('Контроль')
r.close
y.close
