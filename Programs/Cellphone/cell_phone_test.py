import cellphone

def main():
    ''' Получаем данные о телефоне '''
    man = input('Введите производителя: ')
    mod = input('Введите номер модели: ')
    retail = input('Введите розничную цену: ')

    ''' Содаём экземпляр класса Cellphone '''
    phone = cellphone.Cellphone(man, mod, retail)

    ''' Показываем введённые данные '''
    print('Введённые Вами данные:')
    print('Производитель:', phone.get_manufact())
    print('Номер модели: ', phone.get_model())
    print('Розничная цена, $: ', phone.get_retail_price())

''' Вызываем главную функцию '''
main()
