from datetime import datetime, date, timedelta
import time

date1 = input('Начало: ')
##df_scan_struct_date = 
df_scan_date = time.strftime('%d.%m.%Y', time.strptime(date1, '%d.%m.%Y'))
date1 = datetime(int(df_scan_date[6:]), int(df_scan_date[3:5]), int(df_scan_date[:2]))
date2 = input('Конец: ')
##df_scan_struct_date = 
df_scan_date = time.strftime('%d.%m.%Y', time.strptime(date2, '%d.%m.%Y'))
date2 = datetime(int(df_scan_date[6:]), int(df_scan_date[3:5]), int(df_scan_date[:2]))
print('Разница между датами: ', date2 - date1)
timedelta = date2 - date1 + timedelta(days=1)
print('Предыдущий период: ', date1 - timedelta, date2 - timedelta)
