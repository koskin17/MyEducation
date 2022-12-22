from functions import *


def main():
    choice = ''
    while choice != 'q':
        print()
        print('Информация по пользователям в базе:')
        print()
        print('1: Полная статистика по пользователям')
        print('2: Дилеры по странам')
        print('3: Монтажники по странам')
        print('4: Авторизация пользователей')
        print('5: Авторизация пользователей за период')
        print('6: Общая информация по баллам на текущий момент')
        print()
        print('Информация по сканам:')
        print()
        print('7. Кол-во сканировавших пользователей в текущем году на данный момент.')
        print('8. Данные по насканированным баллам в текущем году на данный момент.')
        print('9. ТОП дилеров по сканам в текущем году на данный момент.')
        print('10. ТОП монтажников по сканам в текущем году на данный момент.')
        print('11. Кол-во пользователей и насканированных баллов за период.')
        print('12. Кол-во сканировавших пользователей в текущем году по месяцам.')
        print()
        print('Q: Завершить работу')
        print()

        choice = input('Укажите номер пункта: ')
        if choice == '1':
            total_stat()
        elif choice == '2':
            amount_users_by_country('Дилер')
        elif choice == '3':
            amount_users_by_country('Монтажник')
        elif choice == '4':
            last_authorization_in_app()
        elif choice == '5':
            start_date = input('Укажите дату начала периода в формате mm.dd.yyyy (через точку): ')
            try:
                valid_start_date = time.strptime(start_date, '%d.%m.%Y')
                start_date = time.strftime('%d.%m.%Y', valid_start_date)
                end_date = input('Укажите дату конца периода в формате mm.dd.yyyy (через точку): ')
                try:
                    valid_end_date = time.strptime(end_date, '%d.%m.%Y')
                    end_date = time.strftime('%d.%m.%Y', valid_end_date)
                    authorization_during_period(start_date, end_date)
                except ValueError:
                    print('Дата введена неверно!')
            except ValueError:
                print('Дата введена неверно!')
        elif choice == '6':
            points_by_users_and_countries()
        elif choice == '7':
            table_about_scan_users_in_year()
        elif choice == '8':
            data_about_points()
        elif choice == '9':
            country_list = {}
            for i in range(len(countries)):
                print(i, ' - ', countries[i])
                country_list[i] = countries[i]
                i += 1

            country_choice = input('Выберите страну: ')
            top_users_by_scans(country_list[int(country_choice)], 'Дилер')
        elif choice == '10':
            country_list = {}
            for i in range(len(countries)):
                print(i, ' - ', countries[i])
                country_list[i] = countries[i]
                i += 1

            country_choice = input('Выберите страну: ')
            top_users_by_scans(country_list[int(country_choice)], 'Монтажник')
        elif choice == '11':
            start_date = input('Укажите дату начала периода в формате mm.dd.yyyy (через точку): ')
            try:
                valid_start_date = time.strptime(start_date, '%d.%m.%Y')
                start_date = time.strftime('%d.%m.%Y', valid_start_date)
                end_date = input('Укажите дату конца периода в формате mm.dd.yyyy (через точку): ')
                try:
                    valid_end_date = time.strptime(end_date, '%d.%m.%Y')
                    end_date = time.strftime('%d.%m.%Y', valid_end_date)
                    data_about_scans_during_period(start_date, end_date)
                except ValueError:
                    print('Дата введена неверно!')
            except ValueError:
                print('Дата введена неверно!')
        elif choice == '12':
            table_scanned_users_by_months()
        elif choice == 'q' or choice == 'Q':
            finish()


''' НАЧАЛО ОСНОВНОЙ ПРОГРАММЫ '''

if check_file():
    print('Данные успешно загружены.')
    exclude()
    countries_list()
    main()
