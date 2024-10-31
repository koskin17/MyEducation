'''
Для получения названия дней недели и месяцев на русском нужно
установить локаль.
Для этого:
1. Импортируется модуль local.
2. Устанавливается локаль - local.setlocal(locale.LC_ALL, 'ru_RU').
    Здесь:
            LC_ALL означает, что локальные обозначения применяются ко всему: дни недели, месяцы, деньги и т.д.;
            'ru_RU' означает, что локаль устанавливается русская.
            После 'ru_RU' можно еще добавить кодировку 'ru_RU.UTF-8', но в последних версиях
            Python кодировка UTF-8 по умолчанию и всё работает даже без конкретного указания кодировки.


Для приведения формата времени и даты в привычный режим используется метод strftime с указанием маркеров в нужном порядке.

'''

'''
Пример получения времени из строки и перевода в нормальный формат

from datetime import datetime, date, timedelta
import time

date1 = input('Начало: ')
df_scan_struct_date = time.strptime(date1, '%d.%m.%Y')
df_scan_date = time.strftime('%d.%m.%Y', df_scan_struct_date)
date1 = datetime(int(df_scan_date[6:]), int(df_scan_date[3:5]), int(df_scan_date[:2]))
date2 = input('Конец: ')
df_scan_struct_date = time.strptime(date2, '%d.%m.%Y')
df_scan_date = time.strftime('%d.%m.%Y', df_scan_struct_date)
date2 = datetime(int(df_scan_date[6:]), int(df_scan_date[3:5]), int(df_scan_date[:2]))
print('Разница между датами: ', date2 - date1)
timedelta = date2 - date1 + timedelta(days=1)
print('Предыдущий период: ', date1 - timedelta, date2 - timedelta)
print(type(date1))
date1 = str(date1)
print(type(date1))

'''
