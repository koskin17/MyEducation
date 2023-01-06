import pandas as pd
import os
from datetime import datetime

# pd.set_option('display.max_columns', None) # вывод всех колонок DataFrame в консоли
# pd.set_option('display.max_row', None) # вывод всех строк DataFrame в консоли
# data = pd.read_csv('USvideos.csv', delimiter=",", na_values="NA", converters={"publish_time": pd.to_datetime})
data = pd.read_excel('user_admin.xlsx', na_values="NA",
                     converters={"ID": int, "Баллы": int, "Последняя авторизация в приложении": pd.to_datetime,
                                 "Количество сеансов": int})
data.fillna('')
# Смотрим на колонки
# print(data.columns)
"""['ID', 'Баллы', 'Последняя авторизация в приложении',
       'Количество сеансов', 'Город работы', 'Страна', 'Логин',
       'Тип пользователя', 'Активность', 'Дата регистрации', 'Фамилия', 'Имя',
       'Отчество', 'E-Mail', 'Последняя авторизация', 'Дата изменения',
       'Город проживания', 'Личный телефон', 'Компания', 'Назва дилера',
       'СПК 1', 'СПК 2', 'СПК 3', 'СПК 4', 'СПК 5']"""
print(len(data["ID"]))
data1 = data[(data["Страна"] == "Украина") & (data["Тип пользователя"] == "Монтажник")]
print(len(data1["ID"]))
# print(data.dtypes) # просмотр типов данных в столбцах и определяем столбец с timezone
# data['publish_time'] = data['publish_time'].dt.tz_localize(None)  # удаляем timezone из столбца
# print(data['publish_time'].dtypes)
# new_data = data[['video_id', 'title', 'tags']]
# new_data.to_excel(f'new_data_{date.today()}.xlsx')
# print(data.dtypes) # проверяем форматы данных
# data.to_excel('data.xlsx') # отправляем DataFrame в excel

# os.startfile('data.xlsx')
# # Сортируем по колонке likes
# print(data.sort_values(by='likes', ascending=False))
