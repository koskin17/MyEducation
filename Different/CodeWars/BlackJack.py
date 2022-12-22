'''
Делаем сами "карты": шестерка, семерка, восьмерка, девятка, десятка,
валет (достоинством 2), дама (3), король (4), и туз (11).
'''
koloda = [6,7,8,9,10,2,3,4,11] * 4
'''
Случайным образом перемешаем карты, используя функцию shuffle из модуля random.
'''
import random
random.shuffle(koloda)

'''
Начинаем играть:
'''
while True:
    print('Поиграем в очко?')
    count_pl = 0
    count_comp = 0
    while True:
        choice = input('Будете брать карту? y/n\n')
        if choice == 'y':
            current_pl = koloda.pop()            
            print('Вам попалась карта достоинством %d' %current_pl)
            count_pl += current_pl
            current_comp = koloda.pop()
            print('У компьютера выпала карта достоинство %d' %current_comp)
            count_comp += current_comp
            print('Вы набрали %d очков' %count_pl)
            print('Компьютер набрал %d очков' %count_comp)
            if count_pl > 21:
                print('Извините, у Вас перебор и Вы проиграли')
                break
            elif count_comp > 21:
                print('У компьютера перебор и он проиграл')
            elif count_pl == 21:
                print('Поздравляю, вы набрали 21!')
                break
            elif count_comp == 21:
                print('Компьютер набрал 21!')
                break
            
        else:
                print('У вас %d очков.' %count_pl)
                print('У компьюетра %d очков.' %count_comp)
                if count_pl == count_comp:
                    print('Ничья')
                elif count_pl > count_comp:
                    print('Вы выиграли!')
                elif count_pl < count_comp:
                    print('Вы проиграли.')

    print('До новых встреч!')
