
import os          # Импортируем модель os.path для проверки наличия файла с ДР


##''' Сначала вводим константы для пунктов меню '''
##LOOK_UP = 1
##ADD = 2
##CHANGE = 3
##DELETE = 4
##SHOW = 5
##QUIT = 6

def finish():
    print('До встречи! :)')
    pass

def open_file():
    os.startfile('birthdays.txt')

''' Функция add() добавлять ДР в файл '''
def add():
    name = input('Введите имя человека: ')
    bday = input('Введите его день рождения: ')
    with open('birthdays.txt', 'r') as f:
        for line in f.readlines():
            if name in line:
                print('День рождения этого человека уже занесен в файл.')
                choice = input('1 - изменить День рождения\n0 - вернуться в главное меню: ')
                if choice == '0':
                    f.close()
                    main()
                else:
                    change(name)

    f.close()
    
    with open('birthdays.txt', 'a') as f:
        f.write(name + ':' + bday[:2] + '.' + bday[2:4] + '.' + bday[4:] + '\n')
        print('День рождения добавлен.')
        f.close()

def change(name):
    bday = input('Введите новый День рождения: ')
    tmp = []
    with open('birthdays.txt', 'r') as f:
        for line in f.readlines():
            tmp.append(line)

    for i in range(len(tmp)):
        if name in tmp[i]:
            print(tmp[i])
            tmp[i] = name + ':' + bday[:2] + '.' + bday[2:4] + '.' + bday[4:] + '\n'
    with open('birthdays.txt', 'w') as f:
        for i in tmp:
            f.write(i)
        
    open_file()
    print('День рождения изменён.')
            
    print(tmp)

''' Функция show() выводит дни рождения в справочнике '''
def show():
    print('Дни рождения в базе: ')
    with open('birthdays.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip('\n'))
    f.close()
            
def get_menu_choice():
    choice = ''         # создаём переменную для выбора пользователя
    while choice != 'q':
        print('')
        print('Что Вы хотите сделать?')
        print('')
        print('1: Добавить новый')
        print('2: Изменить День рождения')
        print('3: Посмотреть все Дни рождения')
        print('4: Открыть файл с Днями рождения')
        print('q: Выйти из программы')
        print()
        choice = input('Введите номер выбранного пункта: ')

        if choice == '1':
            add()
        elif choice == '2':
            name = input('Введите имя человека: ')
            change(name)
        elif choice == '3':
            show()            
        elif choice == '4':
            open_file()


    finish()

''' Создаём главную функцию '''
def main():
    ''' Проверяем, есть ли уже файл с ДР '''
    if os.path.isfile('birthdays.txt') != True:
        print('Файл с Днями рождения еще не был создан.')
        answer = input('Создать файл с Днями рождения? (Y (да)').lower()
        if answer != 'y':
            finish()
        else:
            file = open('birthdays.txt', 'w')
            print('Отлично! Файл создан и можно его заполнять.')
            answer = input('Приступить к заполнению файла? (Y (да)').lower()
            if answer != 'y':
                finish()
            else:
                get_menu_choice()
    else:
        get_menu_choice()


##    
##    while choice != QUIT:
##        ''' Получаем выбранный пользователем пункт меню путём вызова функции get_menu_choice() '''
##        choice = get_menu_choice()
##
##        ''' Обрабатываем полученный вариант действия '''
##        if choice == LOOK_UP:
##            look_up(birthdays)
##        elif choice == ADD:
##            add()
##        elif choice == CHANGE:
##            change(birthdays)
##        elif choice == SHOW:
##            show()
##        elif choice == DELETE:
##            delete(birthdays)
        
##''' Создаём функцию look_up, которая ищет имя пользоваеля в словаре с ДР.
##    В качестве аргумента она получает словарь с ДР, которому далее и будет искать'''
##def look_up(birthdays):
##    name = input('Введите имя: ')
##    print(birthdays.get(name, 'Имя не найдено'))    #    ''' Ищем имя в словаре с ДР или пишем, что имя не найдено.
##                                                        #        Поиск по словарю делаем методом dict.get(), который получаем значение ключа по указанному ключу'''
##

##
##''' Функция change() изменяет существующую запись в справочнике / словаре с ДР '''
##def change(birthdays):
##    ''' Получаем имя, запись по которому нужно изменить '''
##    name = input('Введите имя для изменения Дня рождения: ')
##
##    ''' Проверяем наличие этого имени в словаре.
##        Если оно есть, то методом обращения к ключу в словаре перезаписываем его значение'''
##    if name in birthdays:
##        birthdays[name] = input('Введите новый День рождения человека: ')
##    else:
##        print('Такой человек в справочнике не найдён.')
##

##    
##''' Функция delete() для удаления записи из справочника '''
##def delete(birthdays):
##    ''' Получаем имя человека '''
##    name = input('Введите имя человека для удаления из справочника: ')
##
##    ''' Проверяем наличие человека в справочнике '''
##    if name in birthdays:
##        del birthdays[name]
##    else:
##        print('Такой человек в справочнике не найден.')
##

##
##
##    ''' Начало основной программы или вызов главной функции '''
##    main()
##else:
##    print('Файл с днями рождения еще не был создан.')
##    answer = input('Создать файл с днями рождения? (Введите Y, если да, или N, если нет): ').lower()
##    if answer == 'y':
##        file = open('birthdays.txt', 'w')
##        file.close()
##        main()
##    elif answer == 'n':
##        finish()

main()











    

