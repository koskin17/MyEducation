"""Инструкции к заданию
Получите данные по безработице в Москве:
https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv
Найдите, с какого года процент людей с ограниченными возможностями (UnemployedDisabled)
среди всех безработных (UnemployedTotal) стал меньше 2%.
Вопросы к этому заданию
С какого года безработных инвалидов меньше 2% в Москве?
"""
import pandas as pd

data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv",
                   delimiter=";", na_values="NA")
# Смотрим на данные
print()
print(data.head())
# Очищаем данные NaN
data.fillna(0, axis=1, inplace=True)
# Проверяем результат
print()
print(data.head())
# Применение лямбда-функции для расчета процента и заполнения нового столбца полученными данными
# Параметр axis - для применения лямбда-функции построчно
data["Percent"] = data.apply(lambda x: int(x["UnemployedDisabled"] / x["UnemployedTotal"] * 100), axis=1)
# Смотрим на результат - на данные в столбце
print(data["Percent"])
# Теперь фильтруем данные по значению в столбце Percent
data = data[data["Percent"] < 2]
# Смотрим на результат
print(data)
# Для получения года применяем сортировку и добавляем индекс
data = data.set_index("Year")
data = data.sort_index()
# Проверяем результат
print(data)
# Для получения первого года используем срезы
print("Первый год, когда процент безработных опустился ниже 2%: ",
      data.index[1])
