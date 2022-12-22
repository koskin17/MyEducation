while True:
    pin = input('Введите новый пин-код карты, пожалуйста (только цифры): ')

    try:
        pin = int(pin)
        print('Новый пин-код создан')

        break

    except ValueError:
            print('Пожалуйста, вводите только цифры.')
	
