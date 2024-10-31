import os

while True:
    site = input('Введте адрес сайта или слово "завершить" для завершения работы: \n')

    if site == 'Завершить' or site == 'завершить':
        break
    
    if 'www.' in site:
        os.system('start ' + site)
        print('if')
        
    else:
        site = 'https://www.' + site
        os.system('start ' + site)
        print('else')
