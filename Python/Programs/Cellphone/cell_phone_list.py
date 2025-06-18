import cellphone

def main():
    ''' Получаем список объектов cellphone'''
    phones = make_list()

    ''' Показываем данные в списке '''
    print()
    print('Вот введённые Вами данные:')
    display_list(phones)

'''Функция make_list() получает от пользователя
данные о пяти телефонах, а затем возвращает
список объектов Cellphone, содержащих эти данные. '''
def make_list():
    ''' Создаём пустой список '''
    phone_list = []

    ''' Запрашиваем данные о 5-ти телефонах '''
    for count in range(1,3):
        ''' Получить данные о телефоне '''
        print('Номер телефона ' + str(count) + ': ')
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))

        ''' Создаём новые объект Cellphone в памяти
            и присваивам его переменной phone '''
        phone = cellphone.Cellphone(man, mod, retail)

        ''' Добавляем объект в список '''
        phone_list.append(phone)

    ''' Возвращаем список телефонов '''

    return phone_list

''' Функция display_list принимает список с объектами Cellphone
в качестве аргумента и показывает ханящиеся в каждом объекте данные '''
def display_list(phone_list):
    for phone in phone_list:
        print(phone.get_manufact())
        print(phone.get_model())
        print(phone.get_retail_price())
        print()

''' Вызываем главную функцию '''
main()

    
