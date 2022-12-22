import coin

def main():
    ''' Создаём несколько эксземпляров класса '''
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    ''' Показываем стороны трёх монет '''
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    ''' Подбрасываем монету '''
    print('Подбрасываем сразу три монеты...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    ''' Показываем три стороны монет после подбрасывания '''
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())


main()
