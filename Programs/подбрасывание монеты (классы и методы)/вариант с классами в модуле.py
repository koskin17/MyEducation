'''
Импортируем модуль coin, который
мы создали в качестве отдельного файла
с описанием класса Coin для его
последующего использования в программе
'''

import coin


def main():
    my_coin = coin.Coin()
    print('Сейчас монета обращена вверх: ', my_coin.get_sideup())
    my_coin.toss()
    print('Монета легла стороной:', my_coin.get_sideup())

for i in range(10):
    main()
    print()
